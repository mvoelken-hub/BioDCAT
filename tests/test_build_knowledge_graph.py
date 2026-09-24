"""Unit tests for build_knowledge_graph.py's structural helper functions.

Deliberately hermetic: none of these construct a real SchemaView (which would
resolve chem_dcat_ap.yaml's remote DCAT-AP+ import over the network) or need
ontology/strendcat_biocatalysis.owl.ttl / tests/data/valid to exist.
"""
from rdflib import OWL, RDF, RDFS, Graph, Literal, Namespace, URIRef
from rdflib.namespace import SKOS

from strendcat_biocatalysis.build_knowledge_graph import (
    BACKLINK_PROPERTY_NAME,
    add_dataset_backlinks,
    dataset_family_type_uris,
    declare_backlink_property,
)

EX = Namespace("https://example.org/")
BACKLINK = EX[BACKLINK_PROPERTY_NAME]


def _synthetic_record_graph():
    """Dataset -was_generated_by-> Reaction -has_yield-> Yield, plus one
    external reference (never a subject) and one nested Dataset (guarded).
    """
    g = Graph()
    dataset, reaction, yield_ind = EX.dataset1, EX.reaction1, EX.yield1
    external_unit = EX.mole_percent  # only ever a slot value, never a subject
    other_dataset = EX.dataset2  # e.g. reachable via has_version/source

    g.add((dataset, RDF.type, EX.EnzymeMLDocument))
    g.add((dataset, EX.was_generated_by, reaction))
    g.add((reaction, RDF.type, EX.BiocatalyticReaction))
    g.add((reaction, EX.has_yield, yield_ind))
    g.add((yield_ind, RDF.type, EX.Yield))
    g.add((yield_ind, EX.has_unit, external_unit))
    g.add((yield_ind, EX.value, Literal(0.85)))
    g.add((dataset, EX.has_version, other_dataset))
    g.add((other_dataset, RDF.type, EX.EnzymeMLDocument))
    return g, dataset, reaction, yield_ind, external_unit, other_dataset


def test_add_dataset_backlinks_tags_nested_individuals_only():
    g, dataset, reaction, yield_ind, external_unit, other_dataset = _synthetic_record_graph()
    dataset_type_uris = {EX.EnzymeMLDocument}

    add_dataset_backlinks(g, dataset, BACKLINK, dataset_type_uris)

    assert (reaction, BACKLINK, dataset) in g
    assert (yield_ind, BACKLINK, dataset) in g
    assert (dataset, BACKLINK, dataset) not in g
    assert (external_unit, BACKLINK, dataset) not in g
    assert (other_dataset, BACKLINK, dataset) not in g
    assert len(list(g.subject_objects(BACKLINK))) == 2


def test_add_dataset_backlinks_guard_is_load_bearing():
    # Without the guard set, the nested Dataset WOULD be (wrongly) tagged --
    # confirms the exclusion above is actually caused by the guard.
    g, dataset, *_, other_dataset = _synthetic_record_graph()
    add_dataset_backlinks(g, dataset, BACKLINK, dataset_type_uris=set())
    assert (other_dataset, BACKLINK, dataset) in g


class _FakeSchemaView:
    """Duck-typed stand-in for the 3 SchemaView methods `dataset_family_type_uris`
    calls -- avoids constructing a real SchemaView, which resolves
    chem_dcat_ap.yaml's remote DCAT-AP+ import over the network.
    """

    def __init__(self, class_uris: dict, ancestors: dict):
        self._class_uris = class_uris
        self._ancestors = ancestors

    def all_classes(self):
        return self._class_uris

    def class_ancestors(self, cls_name):
        return self._ancestors[cls_name]

    def get_uri(self, cls_name, expand=True):
        return self._class_uris[cls_name]


def test_dataset_family_type_uris_includes_subclasses_and_both_type_forms():
    sv = _FakeSchemaView(
        class_uris={
            "Dataset": "https://example.org/dcat_Dataset",
            "EnzymeMLDocument": "https://example.org/00025",
            "BiocatalyticReaction": "https://example.org/reaction_class_uri",
        },
        ancestors={
            "Dataset": ["Dataset"],
            "EnzymeMLDocument": ["EnzymeMLDocument", "Dataset"],
            "BiocatalyticReaction": ["BiocatalyticReaction", "ChemicalReaction"],
        },
    )
    result = dataset_family_type_uris(sv, EX)

    assert URIRef("https://example.org/00025") in result       # EnzymeMLDocument's own class_uri
    assert EX.EnzymeMLDocument in result                          # local dual type
    assert URIRef("https://example.org/dcat_Dataset") in result  # Dataset's own class_uri
    assert EX.Dataset in result
    assert URIRef("https://example.org/reaction_class_uri") not in result
    assert EX.BiocatalyticReaction not in result


def test_declare_backlink_property_adds_minimal_tbox_triples():
    g = Graph()
    declare_backlink_property(g, BACKLINK, EX.Dataset)

    assert (BACKLINK, RDF.type, OWL.ObjectProperty) in g
    assert (BACKLINK, RDFS.range, EX.Dataset) in g
    assert list(g.objects(BACKLINK, RDFS.label)) == [Literal(BACKLINK_PROPERTY_NAME)]
    assert len(list(g.objects(BACKLINK, SKOS.definition))) == 1
