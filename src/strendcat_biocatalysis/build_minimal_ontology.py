"""Build a minimal OWL ontology from any LinkML schema, using ROBOT/MIREOT.

For every class in a LinkML schema, this script mints an ``owl:Class`` in the
schema's own namespace and links it into two hierarchies:

* the schema's own ``is_a`` tree (mirrors ``gen-owl``'s convention), and
* if the class carries a ``class_uri`` pointing at an *existing* term in an
  external ontology (e.g. ``CHEBI:35233``), the full ancestor chain of that
  term up to ``owl:Thing``, extracted from the source ontology with
  `ROBOT <https://robot.obolibrary.org/>`_'s MIREOT method and merged in.

Enum ``permissible_values`` become ``owl:NamedIndividual``s (with the same
external-ancestor treatment for their ``meaning`` URIs); slots become
``owl:ObjectProperty``/``owl:DatatypeProperty`` declarations, minted flatly in
the schema's namespace without external ancestor extraction.

This script is schema-agnostic: it takes a LinkML schema path as its only
required argument and does not import anything strendcat_biocatalysis-specific,
so it can be copied unmodified into other LinkML projects.

Usage as a script::

    python -m strendcat_biocatalysis.build_minimal_ontology \\
        src/strendcat_biocatalysis/schema/strendcat_biocatalysis.yaml \\
        -o ontology/strendcat_biocatalysis.owl.ttl -v

Requires a Java 11+ runtime on PATH; the ROBOT jar itself is downloaded
on demand into ``--robot-jar-dir`` (default: ``~/.robot-tool-cache``).
"""

from __future__ import annotations

import argparse
import logging
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Optional

import requests
import yaml
from linkml_runtime.utils.formatutils import camelcase
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import OWL, RDF, RDFS, Graph, Literal, Namespace, URIRef
from rdflib.namespace import SKOS

logger = logging.getLogger(__name__)

DEFAULT_ROBOT_VERSION = "1.9.10"
ROBOT_JAR_URL_TEMPLATE = "https://github.com/ontodev/robot/releases/download/v{version}/robot.jar"
# Generic OBO Foundry PURL pattern -- tried for every external prefix that has
# no entry in the override config. Not an allowlist: if a prefix does not
# actually resolve this way, the MIREOT call for it simply fails and the
# affected terms are skipped with a warning (see `resolve_uri`/`run_mireot`).
OBO_PURL_TEMPLATE = "http://purl.obolibrary.org/obo/{prefix_lower}.owl"


# =============================================================================
# URI classification: local (schema's own namespace) vs. external (needs MIREOT)
# =============================================================================


@dataclass
class UriResolution:
    """The result of classifying one class_uri/slot_uri/meaning value."""

    term_iri: str  # fully expanded IRI
    curie: str  # value as declared in the schema (for skos:exactMatch bookkeeping)
    is_external: bool
    source_iri: Optional[str] = None  # ontology to MIREOT `term_iri` from, if resolvable
    skip_reason: Optional[str] = None  # why no source could be resolved, if is_external


def parse_curie(value: str) -> Optional[tuple[str, str]]:
    """Split ``prefix:local_id`` into its parts, or None if not a CURIE.

    A value that is already an absolute URI (contains ``://``) or has no
    ``:`` at all is not a CURIE and has no prefix to resolve.
    """
    if not value or "://" in value:
        return None
    if ":" not in value:
        return None
    prefix, _, local_id = value.partition(":")
    if not prefix or not local_id:
        return None
    return prefix, local_id


def resolve_uri(
    value: Optional[str],
    default_prefix: str,
    namespaces: Mapping[str, str],
    overrides: dict,
) -> Optional[UriResolution]:
    """Classify a class_uri/slot_uri/meaning value.

    Returns None if `value` is falsy. Otherwise always returns a resolution;
    callers check `.is_external` and `.source_iri` to decide whether an
    ancestor chain should be linked in.
    """
    if not value:
        return None
    parsed = parse_curie(value)
    if parsed is None:
        return UriResolution(
            term_iri=value,
            curie=value,
            is_external=True,
            skip_reason="not a recognised CURIE (no registered prefix); MIREOT source unknown",
        )
    prefix, local_id = parsed
    base = namespaces.get(prefix)
    if base is None:
        return UriResolution(
            term_iri=value,
            curie=value,
            is_external=True,
            skip_reason=f"prefix {prefix!r} is not declared under this schema's prefixes:",
        )
    term_iri = base + local_id
    if prefix == default_prefix:
        return UriResolution(term_iri=term_iri, curie=value, is_external=False)
    override = overrides.get(prefix)
    if override is not None and override.get("skip"):
        reason = override.get("note") or f"prefix {prefix!r} marked skip in override config"
        return UriResolution(term_iri=term_iri, curie=value, is_external=True, skip_reason=reason)
    source_iri = override["iri"] if override else OBO_PURL_TEMPLATE.format(prefix_lower=prefix.lower())
    return UriResolution(term_iri=term_iri, curie=value, is_external=True, source_iri=source_iri)


def collect_external_terms(
    sv: SchemaView,
    default_prefix: str,
    namespaces: Mapping[str, str],
    overrides: dict,
) -> dict[str, set[str]]:
    """Group every externally-resolvable class_uri/meaning by source ontology."""
    registry: dict[str, set[str]] = defaultdict(set)
    for cls in sv.all_classes().values():
        res = resolve_uri(cls.class_uri, default_prefix, namespaces, overrides)
        if res is not None and res.is_external and res.source_iri:
            registry[res.source_iri].add(res.term_iri)
    for enum in sv.all_enums().values():
        for pv in (enum.permissible_values or {}).values():
            meaning = getattr(pv, "meaning", None)
            res = resolve_uri(meaning, default_prefix, namespaces, overrides)
            if res is not None and res.is_external and res.source_iri:
                registry[res.source_iri].add(res.term_iri)
    return dict(registry)


# =============================================================================
# Local fragment: mint classes/enums/slots, link in successfully-MIREOT'd terms
# =============================================================================


def build_local_graph(
    sv: SchemaView,
    default_prefix: str,
    namespaces: Mapping[str, str],
    overrides: dict,
    failed_sources: set[str],
) -> tuple[Graph, list[str]]:
    """Mint the schema's own classes/enums/slots and connect them to any
    successfully-extracted external ancestor chains.

    `failed_sources` are source ontology IRIs whose MIREOT call did not
    succeed (or was never attempted, e.g. in --dry-run); terms belonging to
    them still get an owl:Class/skos:exactMatch, just without an
    rdfs:subClassOf/rdf:type edge into the (missing) external fragment.
    Returns the graph plus a list of human-readable warnings for such cases.
    """
    g = Graph()
    ns = Namespace(namespaces[default_prefix])
    g.bind(default_prefix, ns)
    g.bind("skos", SKOS)
    g.bind("owl", OWL)
    warnings: list[str] = []

    ontology_iri = URIRef(sv.schema.id.rstrip("/") + "/ontology")
    g.add((ontology_iri, RDF.type, OWL.Ontology))
    if sv.schema.title:
        g.add((ontology_iri, RDFS.label, Literal(sv.schema.title)))
    if sv.schema.description:
        g.add((ontology_iri, RDFS.comment, Literal(sv.schema.description)))

    def link_external(subject: URIRef, res: UriResolution, rel) -> None:
        g.add((subject, SKOS.exactMatch, URIRef(res.term_iri)))
        if res.source_iri and res.source_iri not in failed_sources:
            g.add((subject, rel, URIRef(res.term_iri)))
        else:
            reason = res.skip_reason or "MIREOT extraction failed for this source ontology"
            warnings.append(f"{subject}: {res.curie} -> {reason}")

    # --- classes -------------------------------------------------------
    for cls_name, cls in sv.all_classes().items():
        class_iri = ns[camelcase(cls_name)]
        g.add((class_iri, RDF.type, OWL.Class))
        g.add((class_iri, RDFS.label, Literal(cls_name)))
        if cls.description:
            g.add((class_iri, SKOS.definition, Literal(cls.description)))
        if cls.is_a:
            g.add((class_iri, RDFS.subClassOf, ns[camelcase(cls.is_a)]))
        res = resolve_uri(cls.class_uri, default_prefix, namespaces, overrides)
        if res is not None:
            if res.is_external:
                link_external(class_iri, res, RDFS.subClassOf)
            else:
                g.add((class_iri, SKOS.exactMatch, URIRef(res.term_iri)))

    # --- enums -> owl:Class + permissible_values -> owl:NamedIndividual ----
    for enum_name, enum in sv.all_enums().items():
        enum_iri = ns[camelcase(enum_name)]
        g.add((enum_iri, RDF.type, OWL.Class))
        g.add((enum_iri, RDFS.label, Literal(enum_name)))
        if enum.description:
            g.add((enum_iri, SKOS.definition, Literal(enum.description)))
        for pv_name, pv in (enum.permissible_values or {}).items():
            slug = re.sub(r"[^A-Za-z0-9_]", "_", pv_name)
            ind_iri = ns[f"{camelcase(enum_name)}_{slug}"]
            g.add((ind_iri, RDF.type, OWL.NamedIndividual))
            g.add((ind_iri, RDF.type, enum_iri))
            g.add((ind_iri, RDFS.label, Literal(pv_name)))
            description = getattr(pv, "description", None)
            if description:
                g.add((ind_iri, SKOS.definition, Literal(description)))
            meaning = getattr(pv, "meaning", None)
            res = resolve_uri(meaning, default_prefix, namespaces, overrides)
            if res is not None:
                if res.is_external:
                    link_external(ind_iri, res, RDF.type)
                else:
                    g.add((ind_iri, SKOS.exactMatch, URIRef(res.term_iri)))

    # --- slots -> owl:ObjectProperty | owl:DatatypeProperty -------------
    class_names = set(sv.all_classes())
    enum_names = set(sv.all_enums())
    for slot_name, slot in sv.all_slots().items():
        slot_iri = ns[slot_name]
        range_name = slot.range or sv.schema.default_range or "string"
        prop_type = OWL.ObjectProperty if range_name in class_names or range_name in enum_names else OWL.DatatypeProperty
        g.add((slot_iri, RDF.type, prop_type))
        g.add((slot_iri, RDFS.label, Literal(slot_name)))
        if slot.description:
            g.add((slot_iri, SKOS.definition, Literal(slot.description)))
        if slot.is_a:
            g.add((slot_iri, RDFS.subPropertyOf, ns[slot.is_a]))
        if slot.slot_uri:
            # Slots deliberately do NOT get external MIREOT ancestor chains
            # (see plan) -- only the alignment annotation.
            res = resolve_uri(slot.slot_uri, default_prefix, namespaces, overrides)
            if res is not None:
                g.add((slot_iri, SKOS.exactMatch, URIRef(res.term_iri)))

    return g, warnings


# =============================================================================
# ROBOT orchestration
# =============================================================================


def check_java_available() -> None:
    try:
        subprocess.run(["java", "-version"], capture_output=True, timeout=15, check=True)
    except FileNotFoundError as exc:
        raise SystemExit(
            "Java was not found on PATH. ROBOT requires Java 11 or later -- "
            "see https://robot.obolibrary.org/ for setup instructions."
        ) from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"`java -version` failed unexpectedly: {exc}") from exc


def ensure_robot_jar(version: str, tools_dir: Path) -> Path:
    """Download robot.jar into `tools_dir` if not already cached there."""
    tools_dir.mkdir(parents=True, exist_ok=True)
    jar_path = tools_dir / f"robot-{version}.jar"
    if jar_path.exists():
        logger.info("Using cached ROBOT %s at %s", version, jar_path)
        return jar_path
    url = ROBOT_JAR_URL_TEMPLATE.format(version=version)
    logger.info("Downloading ROBOT %s from %s", version, url)
    tmp_path = jar_path.with_suffix(".jar.part")
    with requests.get(url, stream=True, timeout=120) as response:
        response.raise_for_status()
        with open(tmp_path, "wb") as fh:
            for chunk in response.iter_content(chunk_size=1 << 20):
                fh.write(chunk)
    tmp_path.rename(jar_path)
    logger.info("Saved ROBOT jar to %s", jar_path)
    return jar_path


def run_mireot(java_jar: Path, source_iri: str, term_iris: set[str], out_path: Path) -> bool:
    """Extract the ancestor closure (up to owl:Thing) of `term_iris` from
    `source_iri` into `out_path`. Returns False (and logs a WARNING) instead
    of raising, so one bad source ontology never aborts the whole run.
    """
    terms_file = out_path.with_suffix(".terms.txt")
    terms_file.write_text("\n".join(sorted(term_iris)) + "\n", encoding="utf-8")
    cmd = [
        "java", "-jar", str(java_jar),
        "extract", "--method", "MIREOT",
        "--input-iri", source_iri,
        "--lower-terms", str(terms_file),
        "--output", str(out_path),
    ]
    logger.info("Running: %s", " ".join(cmd))
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=1800)
    except subprocess.CalledProcessError as exc:
        tail = (exc.stderr or str(exc))[-2000:]
        logger.warning("MIREOT extraction failed for %s (%d term(s)): %s", source_iri, len(term_iris), tail)
        return False
    except subprocess.TimeoutExpired:
        logger.warning("MIREOT extraction timed out for %s (%d term(s))", source_iri, len(term_iris))
        return False
    return True


def run_merge(java_jar: Path, fragment_paths: list[Path], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["java", "-jar", str(java_jar), "merge"]
    for p in fragment_paths:
        cmd += ["--input", str(p)]
    cmd += ["--output", str(output_path)]
    logger.info("Running: %s", " ".join(cmd))
    subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=1800)


# =============================================================================
# CLI
# =============================================================================


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("schema", type=Path, help="Path to a LinkML schema YAML file")
    parser.add_argument(
        "-o", "--output", type=Path, default=None,
        help="Output Turtle path (default: ontology/<schema-stem>.owl.ttl)",
    )
    parser.add_argument(
        "--config", type=Path, default=None,
        help="Override YAML mapping external prefixes to MIREOT sources "
             "(default: ontology_sources.yaml next to --output, if it exists)",
    )
    parser.add_argument("--robot-version", default=DEFAULT_ROBOT_VERSION, help="ROBOT release version to download/use")
    parser.add_argument(
        "--robot-jar-dir", type=Path, default=Path.home() / ".robot-tool-cache",
        help="Directory to cache the downloaded robot.jar (default: ~/.robot-tool-cache)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Resolve terms and write the local fragment, but do not invoke ROBOT/network at all",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable INFO-level logging")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s: %(message)s")

    output_path = args.output or Path("ontology") / f"{args.schema.stem}.owl.ttl"
    config_path = args.config or (output_path.parent / "ontology_sources.yaml")
    overrides: dict = yaml.safe_load(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
    overrides = overrides or {}

    sv = SchemaView(str(args.schema))
    default_prefix = sv.schema.default_prefix
    namespaces = dict(sv.namespaces())

    registry = collect_external_terms(sv, default_prefix, namespaces, overrides)
    logger.info("%d external source ontolog(y/ies) to MIREOT: %s", len(registry), ", ".join(sorted(registry)) or "-")

    work_dir = output_path.parent / "build" / args.schema.stem
    work_dir.mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        for source_iri, terms in sorted(registry.items()):
            print(f"# would MIREOT {len(terms)} term(s) from {source_iri}")
            for term in sorted(terms):
                print(f"  {term}")
        graph, warnings = build_local_graph(sv, default_prefix, namespaces, overrides, failed_sources=set(registry))
        local_path = work_dir / "local_fragment.ttl"
        graph.serialize(destination=str(local_path), format="turtle")
        print(f"# dry run: wrote local fragment to {local_path}; no ROBOT commands were executed.", file=sys.stderr)
        for warning in warnings:
            logger.warning(warning)
        return 0

    check_java_available()
    jar_path = ensure_robot_jar(args.robot_version, args.robot_jar_dir)

    failed_sources: set[str] = set()
    fragment_paths: list[Path] = []
    for index, (source_iri, terms) in enumerate(sorted(registry.items())):
        fragment_path = work_dir / f"fragment_{index}.ttl"
        if run_mireot(jar_path, source_iri, terms, fragment_path):
            fragment_paths.append(fragment_path)
        else:
            failed_sources.add(source_iri)

    graph, warnings = build_local_graph(sv, default_prefix, namespaces, overrides, failed_sources)
    local_path = work_dir / "local_fragment.ttl"
    graph.serialize(destination=str(local_path), format="turtle")

    run_merge(jar_path, [local_path, *fragment_paths], output_path)

    print(f"Wrote {output_path}", file=sys.stderr)
    print(
        f"{len(sv.all_classes())} classes, {len(sv.all_slots())} slots, {len(sv.all_enums())} enums processed.",
        file=sys.stderr,
    )
    print(f"{len(registry)} external source ontologies queried, {len(failed_sources)} failed/skipped.", file=sys.stderr)
    if warnings:
        print(f"{len(warnings)} term(s) without an external ancestor chain:", file=sys.stderr)
        for warning in warnings:
            print(f"  - {warning}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
