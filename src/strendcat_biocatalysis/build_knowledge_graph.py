"""Combine BioDCAT instance data with the minimal ontology into a knowledge graph.

Loads every ``*.yaml`` file in ``tests/data/valid/`` as a BioDCAT instance (class
resolved from the filename, same convention as ``tests/test_data.py``), dumps each
to RDF via LinkML's ``RDFLibDumper``, and merges the result into
``ontology/strendcat_biocatalysis.owl.ttl`` (the minimal ontology built by
``build_minimal_ontology.py``). Every typed node additionally gets the local
``strendcat_biocatalysis:<ClassName>`` ``rdf:type`` alongside whatever external
``class_uri`` ``RDFLibDumper`` already set, so the graph is queryable by local
class name without walking the ontology's ``rdfs:subClassOf`` chain.

Every individual nested at any depth within a record's own object tree -- a
Reaction, a Yield, an EnzymeMeasurement, a MeasurementTimepoint, and so on --
also gets one ``strendcat_biocatalysis:part_of_dataset`` triple back to that
record's own Dataset root URI, regardless of Dataset subclass or how many
hops of modeled object properties separate the two (this chain differs per
Dataset subclass -- e.g. EnzymeMLDocument vs. ReactionMonitoringDataset --
and there is otherwise no backward link at all). This is computed generically
by walking each record's own RDF graph (see ``add_dataset_backlinks``), not by
hardcoding per-class paths, so it needs no LinkML schema change and requires
no per-class wiring for future Dataset subclasses or content classes. It is a
KG-build-time convenience shortcut for SPARQL, kept separate from the modeled
domain chain, which remains the semantically authoritative relationship.

Unlike ``build_minimal_ontology.py``, this script is BioDCAT-specific: the schema,
ontology and data-directory paths are fixed constants below, not CLI arguments.

Usage as a script::

    python -m strendcat_biocatalysis.build_knowledge_graph -o ontology/strendcat_biocatalysis_kg.ttl -v

Requires ``ontology/strendcat_biocatalysis.owl.ttl`` to already exist (run
``just build-ontology`` first).
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

import strendcat_biocatalysis.datamodel.strendcat_biocatalysis
from linkml_runtime.dumpers.rdflib_dumper import RDFLibDumper
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.formatutils import camelcase
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import OWL, RDF, RDFS, Graph, Literal, Namespace, URIRef
from rdflib.namespace import SKOS

logger = logging.getLogger(__name__)

SCHEMA_PATH = Path("src/strendcat_biocatalysis/schema/strendcat_biocatalysis.yaml")
ONTOLOGY_PATH = Path("ontology/strendcat_biocatalysis.owl.ttl")
DATA_DIR = Path("tests/data/valid")
DEFAULT_OUTPUT = Path("ontology/strendcat_biocatalysis_kg.ttl")

# Local name of the generic content-individual -> Dataset backlink property
# minted by `declare_backlink_property` (see `add_dataset_backlinks`).
BACKLINK_PROPERTY_NAME = "part_of_dataset"


# =============================================================================
# Dual-typing: mint the local class URI alongside whatever RDFLibDumper set
# =============================================================================


def dual_type_local_classes(sv: SchemaView, ns: Namespace, graph: Graph) -> None:
    """Add ``rdf:type ns:<ClassName>`` to every node RDFLibDumper already typed.

    RDFLibDumper types each node via ``schemaview.get_uri(cn, expand=True)``,
    which returns the *external* class_uri when a class has one -- so this adds
    the local minted type back in, independent of whatever RDFLibDumper set.
    Reverse-lookup instead of re-walking the object tree: for a class without a
    class_uri, ``get_uri`` already resolves to ``ns[camelcase(name)]``, so both
    cases map back to the class name through the same dict.
    """
    reverse = {URIRef(sv.get_uri(cls_name, expand=True)): cls_name for cls_name in sv.all_classes()}
    for subject, obj in list(graph.subject_objects(RDF.type)):
        cls_name = reverse.get(obj)
        if cls_name is not None:
            graph.add((subject, RDF.type, ns[camelcase(cls_name)]))


# =============================================================================
# Dataset backlinks: generic structural "part of dataset" shortcut
# =============================================================================


def dataset_family_type_uris(sv: SchemaView, ns: Namespace) -> set:
    """Collect every rdf:type URI that marks a node as a ``Dataset`` instance.

    Includes ``Dataset`` itself and every one of its schema subclasses
    (``EnzymeMLDocument``, ``AnalysisDataset``, ...), in both forms a node
    might carry that type: the URI RDFLibDumper actually writes
    (``schemaview.get_uri(cls_name, expand=True)`` -- the class_uri, local or
    external) and the local dual type `dual_type_local_classes` adds
    alongside it (``ns[camelcase(cls_name)]``).

    Used by `add_dataset_backlinks` to guard against tagging a *different*
    Dataset instance -- reachable e.g. through the DCAT-AP boilerplate slots
    ``has_version``/``source`` that ``Dataset`` inherits -- as if it were
    content belonging to the *current* record's Dataset.
    """
    type_uris: set = set()
    for cls_name in sv.all_classes():
        if "Dataset" not in sv.class_ancestors(cls_name):
            continue
        type_uris.add(URIRef(sv.get_uri(cls_name, expand=True)))
        type_uris.add(ns[camelcase(cls_name)])
    return type_uris


def add_dataset_backlinks(
    record_graph: Graph, dataset_uri: URIRef, backlink_pred: URIRef, dataset_type_uris: set
) -> None:
    """Add ``(node, backlink_pred, dataset_uri)`` for every individual `record_graph` describes.

    A "described individual" (a Reaction, a Yield, an EnzymeMeasurement, a
    MeasurementTimepoint blank node, ...) is any node that appears as the
    *subject* of at least one triple in `record_graph` -- that is exactly
    how RDFLibDumper recursively dumps a nested object: it emits triples
    *about* that node. A bare external reference used only as a slot value
    (a CHEBI term, a QUDT unit, an enum permissible value's meaning URI) is
    only ever an *object* in `record_graph`, never also a subject there, so
    checking subject-membership cleanly separates the two -- without needing
    to know which classes/predicates are involved, which matters because
    predicates here are frequently ambiguous external terms reused across
    unrelated slots (e.g. both has_measurement_species_data and
    has_timepoint dump as BFO:0000051; see module docstring).

    Two kinds of node are excluded even though they pass that check:

    * `dataset_uri` itself -- it does not need a backlink to itself.
    * Any node whose rdf:type is in `dataset_type_uris`, i.e. a *different*
      Dataset (or subclass) instance reachable through one of the generic
      DCAT-AP slots Dataset inherits (``has_version``, ``source``,
      ``in_series``, ...). Without this guard, populating one of those slots
      would wrongly claim that other Dataset's root is "part of" this one.

      Known limitation: this only guards that *other* Dataset's own root
      node. If that nested Dataset in turn carried its own rich nested
      content (through its own was_generated_by/... chain), those deeper
      nodes would still be backlinked to *this* record's dataset_uri, since
      they are subjects of `record_graph` too and are not themselves
      Dataset-typed. Accepted for now: no current schema usage populates
      has_version/source/in_series with a populated Dataset instance. A
      fully correct fix would stop the walk at any Dataset-typed node
      (a reachability/partition problem) rather than filtering post-hoc by
      node type; revisit if this ever gets exercised.
    """
    subjects = set(record_graph.subjects())
    for node in set(record_graph.objects()):
        if isinstance(node, Literal) or node == dataset_uri:
            continue
        if node not in subjects:
            continue
        if any(t in dataset_type_uris for t in record_graph.objects(node, RDF.type)):
            continue
        record_graph.add((node, backlink_pred, dataset_uri))


def declare_backlink_property(graph: Graph, backlink_pred: URIRef, dataset_class_uri: URIRef) -> None:
    """Mint a minimal ``owl:ObjectProperty`` declaration for `backlink_pred` in `graph`.

    Added once to the combined graph (not per-record) by `main`, directly in
    this script -- not via the LinkML schema or `build_minimal_ontology.py`,
    which is deliberately schema-agnostic and must stay that way (see its
    module docstring). This property is a KG-build-time convenience shortcut
    for SPARQL, kept distinct from the modeled, semantically authoritative
    path from a content individual back to its Dataset (the existing forward
    object-property chain, e.g. Dataset -was_generated_by-> ... -> Yield --
    see module docstring). No rdfs:domain is declared: "any nested content
    individual" is not itself a named class in the schema.
    """
    graph.add((backlink_pred, RDF.type, OWL.ObjectProperty))
    graph.add((backlink_pred, RDFS.label, Literal(BACKLINK_PROPERTY_NAME)))
    graph.add((backlink_pred, RDFS.range, dataset_class_uri))
    graph.add((backlink_pred, SKOS.definition, Literal(
        "KG-build-time convenience link from a content individual nested at any depth "
        "within a Dataset record back to that Dataset's own root URI. Added "
        "automatically for every record by build_knowledge_graph.py, independent of "
        "Dataset subclass or content class. Distinct from the modeled, semantically "
        "authoritative forward chain connecting them (e.g. "
        "Dataset -was_generated_by-> ... -> Yield)."
    )))


# =============================================================================
# Merge with IRI-collision warnings
# =============================================================================


def merge_record(combined: Graph, record_graph: Graph, filename: str, first_seen: dict) -> None:
    """Merge `record_graph` into `combined`, warning if a subject IRI it
    describes already carries a *different* rdf:type from an earlier file.
    Always merges regardless (rdflib unions triples losslessly either way).
    """
    for subject in {s for s in record_graph.subjects(RDF.type, None)}:
        new_types = set(record_graph.objects(subject, RDF.type))
        existing_types = set(combined.objects(subject, RDF.type))
        if existing_types and existing_types != new_types:
            logger.warning(
                "IRI collision: %s already has rdf:type %s from %s; %s adds %s",
                subject, sorted(existing_types), first_seen.get(subject, "?"), filename, sorted(new_types),
            )
        first_seen.setdefault(subject, filename)
    combined += record_graph


# =============================================================================
# CLI
# =============================================================================


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "-o", "--output", type=Path, default=DEFAULT_OUTPUT,
        help=f"Output Turtle path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable INFO-level logging")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s: %(message)s")

    sv = SchemaView(str(SCHEMA_PATH))
    ns = Namespace(sv.namespaces()[sv.schema.default_prefix])
    backlink_pred = ns[BACKLINK_PROPERTY_NAME]
    dataset_type_uris = dataset_family_type_uris(sv, ns)

    if not ONTOLOGY_PATH.exists():
        raise SystemExit(f"Ontology file not found: {ONTOLOGY_PATH} -- run `just build-ontology` first.")

    combined = Graph()
    combined.parse(str(ONTOLOGY_PATH), format="turtle")
    declare_backlink_property(combined, backlink_pred, ns[camelcase("Dataset")])
    tbox_triples = len(combined)
    for prefix, uri in dict(sv.namespaces()).items():
        combined.bind(prefix, uri)

    if not DATA_DIR.exists():
        raise SystemExit(f"Data directory not found: {DATA_DIR}")

    data_files = sorted(DATA_DIR.glob("*.yaml"))
    if not data_files:
        raise SystemExit(f"No *.yaml files found in {DATA_DIR} -- nothing to build a knowledge graph from.")

    dumper = RDFLibDumper()
    first_seen: dict = {}
    loaded: list[str] = []
    skipped: list[str] = []

    for path in data_files:
        class_name = path.stem.split("-")[0]
        target_class = getattr(strendcat_biocatalysis.datamodel.strendcat_biocatalysis, class_name, None)
        if target_class is None:
            logger.warning("%s: no class %r in datamodel -- skipping", path.name, class_name)
            skipped.append(path.name)
            continue
        try:
            obj = yaml_loader.load(str(path), target_class=target_class)
            # @base is unset in a plain SchemaView; without it, RDFLibDumper raises on any
            # slot value that is a bare local id rather than a URI/CURIE (e.g. a unit "ml").
            record_graph = dumper.as_rdf_graph(obj, sv, prefix_map={"@base": str(ns)})
            # Mirrors RDFLibDumper's own root-URI computation (schemaview.uri_for),
            # so this stays correct even if obj.id is ever a bare CURIE rather than
            # an absolute URI. Computed inside the try block: a class lacking an
            # `id` (e.g. a future non-Dataset entry under DATA_DIR) should be
            # skipped-with-warning like any other load failure, not crash the run.
            dataset_uri = sv.namespaces().uri_for(str(obj.id))
        except Exception as exc:
            logger.warning("%s: failed to load/convert as %s -- %s", path.name, class_name, exc)
            skipped.append(path.name)
            continue

        dual_type_local_classes(sv, ns, record_graph)
        if dataset_uri in record_graph.subjects():
            add_dataset_backlinks(record_graph, dataset_uri, backlink_pred, dataset_type_uris)
        else:
            logger.warning(
                "%s: computed dataset URI %s is not a subject of its own record graph -- skipping backlinks",
                path.name, dataset_uri,
            )
        merge_record(combined, record_graph, path.name, first_seen)
        loaded.append(path.name)

    if not loaded:
        raise SystemExit(f"No data file in {DATA_DIR} could be loaded -- refusing to write a TBox-only file.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    combined.serialize(destination=str(args.output), format="turtle")

    print(f"Wrote {args.output}", file=sys.stderr)
    print(
        f"{len(data_files)} data file(s) found, {len(loaded)} loaded, {len(skipped)} skipped; "
        f"{len(combined)} triples total ({tbox_triples} from the TBox).",
        file=sys.stderr,
    )
    if skipped:
        print(f"Skipped: {', '.join(skipped)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
