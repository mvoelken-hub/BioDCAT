# Auto generated from strendcat_biocatalysis.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-09-02T11:14:12
# Schema: StrenDCAT-Biocatalysis
#
# id: https://w3id.org/mvoelken-hub/StrenDCAT-Biocatalysis
# description: This is an application profile for biocatalytic experiments based on the
#   STRENDA Biocatalysis Guidelines (https://github.com/Strenda-biocatalysis/Strenda-biocatalysis).
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Decimal, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Decimal, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Namespaces
AFE = CurieNamespace('AFE', 'http://purl.allotrope.org/ontologies/equipment#AFE_')
AFP = CurieNamespace('AFP', 'http://purl.allotrope.org/ontologies/process#AFP_')
AFQ = CurieNamespace('AFQ', 'http://purl.allotrope.org/ontologies/quality#AFQ_')
AFR = CurieNamespace('AFR', 'http://purl.allotrope.org/ontologies/result#AFR_')
AFX = CurieNamespace('AFX', 'http://purl.allotrope.org/ontologies/property#AFX_')
BAO = CurieNamespace('BAO', 'http://www.bioassayontology.org/bao#BAO_')
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CAO = CurieNamespace('CAO', 'http://champ-project.org/images/ontology/cao.owl#CAO_')
CHEBI = CurieNamespace('CHEBI', 'http://purl.obolibrary.org/obo/CHEBI_')
CHEMINF = CurieNamespace('CHEMINF', 'http://semanticscience.org/resource/CHEMINF_')
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
EDAM = CurieNamespace('EDAM', 'http://edamontology.org/data_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MOP = CurieNamespace('MOP', 'http://purl.obolibrary.org/obo/MOP_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
NPO = CurieNamespace('NPO', 'http://purl.bioontology.org/ontology/npo#NPO_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PROCO = CurieNamespace('PROCO', 'http://purl.obolibrary.org/obo/PROCO_')
REX = CurieNamespace('REX', 'http://purl.obolibrary.org/obo/REX_')
RO = CurieNamespace('RO', 'http://purl.obolibrary.org/obo/RO_')
RXNO = CurieNamespace('RXNO', 'http://purl.obolibrary.org/obo/RXNO_')
SBO = CurieNamespace('SBO', 'https://biomodels.net/SBO/SBO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
SNOMED = CurieNamespace('SNOMED', 'http://snomed.info/id/')
UO = CurieNamespace('UO', 'https://purl.obolibrary.org/obo/UO_')
VOC4CAT = CurieNamespace('VOC4CAT', 'https://w3id.org/nfdi4cat/voc4cat_')
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
CHEMDCATAP = CurieNamespace('chemdcatap', 'https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/')
CHEMICAL_ENTITIES_AP = CurieNamespace('chemical_entities_ap', 'https://w3id.org/nfdi-de/dcat-ap-plus/chemistry/entity/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCATAP = CurieNamespace('dcatap', 'http://data.europa.eu/r5r/')
DCATAP_PLUS = CurieNamespace('dcatap_plus', 'https://w3id.org/nfdi-de/dcat-ap-plus/')
DCATAPPLUS = CurieNamespace('dcatapplus', 'https://w3id.org/nfdi-de/dcat-ap-plus/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
ELI = CurieNamespace('eli', 'http://data.europa.eu/eli/ontology#')
EPOS = CurieNamespace('epos', 'https://www.epos-eu.org/epos-dcat-ap#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
MATERIAL_ENTITIES_AP = CurieNamespace('material_entities_ap', 'https://w3id.org/nfdi-de/dcat-ap-plus/materials/')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms#')
STRENDCAT_BIOCATALYSIS = CurieNamespace('strendcat_biocatalysis', 'https://w3id.org/mvoelken-hub/StrenDCAT-Biocatalysis/')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = STRENDCAT_BIOCATALYSIS


# Types
class Duration(str):
    """ The datatype that represents durations of time. """
    type_class_uri = XSD["duration"]
    type_class_curie = "xsd:duration"
    type_name = "duration"
    type_model_uri = STRENDCAT_BIOCATALYSIS.Duration


class HexBinary(str):
    """ The datatype that represents arbitrary hex-encoded binary data. """
    type_class_uri = XSD["hexBinary"]
    type_class_curie = "xsd:hexBinary"
    type_name = "hexBinary"
    type_model_uri = STRENDCAT_BIOCATALYSIS.HexBinary


class NonNegativeInteger(int):
    """ The datatype that represents non-negative integers. """
    type_class_uri = XSD["nonNegativeInteger"]
    type_class_curie = "xsd:nonNegativeInteger"
    type_name = "nonNegativeInteger"
    type_model_uri = STRENDCAT_BIOCATALYSIS.NonNegativeInteger


# Class references
class ActivityId(URIorCURIE):
    pass


class AgenticEntityId(URIorCURIE):
    pass


class DataGeneratingActivityId(ActivityId):
    pass


class BiocatalyticExperimentId(DataGeneratingActivityId):
    pass


class SubstanceSampleCharacterizationId(DataGeneratingActivityId):
    pass


class ReactionMonitoringId(DataGeneratingActivityId):
    pass


class DataAnalysisId(DataGeneratingActivityId):
    pass


class DatasetId(URIorCURIE):
    pass


class EnzymeMLDocumentId(DatasetId):
    pass


class SubstanceSampleCharacterizationDatasetId(DatasetId):
    pass


class ReactionMonitoringDatasetId(DatasetId):
    pass


class AnalysisDatasetId(DatasetId):
    pass


class DefinedTermId(URIorCURIE):
    pass


class DeviceId(AgenticEntityId):
    pass


class MixingImpellerId(DeviceId):
    pass


class ShakerId(DeviceId):
    pass


class GasSupplySystemId(DeviceId):
    pass


class TemperatureControlDeviceId(DeviceId):
    pass


class EntityId(URIorCURIE):
    pass


class EvaluatedActivityId(ActivityId):
    pass


class PlannedProcessId(EvaluatedActivityId):
    pass


class TemperatureShiftProcessId(PlannedProcessId):
    pass


class TemperatureGradientId(PlannedProcessId):
    pass


class PHShiftProcessId(PlannedProcessId):
    pass


class PHGradientId(PlannedProcessId):
    pass


class SamplingProcessId(PlannedProcessId):
    pass


class MaterialProcessingId(PlannedProcessId):
    pass


class DryingProcessId(MaterialProcessingId):
    pass


class BiocatalystProductionProcessId(MaterialProcessingId):
    pass


class SamplePreparationProcessId(MaterialProcessingId):
    pass


class QuenchingProcessId(MaterialProcessingId):
    pass


class SampleTreatmentProcessId(MaterialProcessingId):
    pass


class MeasurementProcessId(PlannedProcessId):
    pass


class PHMeasurementProcessId(MeasurementProcessId):
    pass


class EnzymeMeasurementId(MeasurementProcessId):
    pass


class EvaluatedEntityId(EntityId):
    pass


class AnalysisSourceDataId(EvaluatedEntityId):
    pass


class SoftwareId(AgenticEntityId):
    pass


class DocumentId(URIorCURIE):
    pass


class LegalResourceId(URIorCURIE):
    pass


class LicenseDocumentId(URIorCURIE):
    pass


class ResourceId(URIorCURIE):
    pass


class ChemicalEntityId(EntityId):
    pass


class StorageAdditiveId(ChemicalEntityId):
    pass


class BiocatalyticComponentId(ChemicalEntityId):
    pass


class MolecularComplexId(ChemicalEntityId):
    pass


class AtomId(EntityId):
    pass


class ChemicalReactionId(EvaluatedActivityId):
    pass


class BiocatalyticReactionId(ChemicalReactionId):
    pass


class DissolvingSubstanceId(AgenticEntityId):
    pass


class CatalystId(AgenticEntityId):
    pass


class ReactorId(DeviceId):
    pass


class ReactionVesselId(ReactorId):
    pass


class VialId(ReactionVesselId):
    pass


class PlateId(ReactionVesselId):
    pass


class StirredTankReactorId(ReactionVesselId):
    pass


class TubularFlowReactorId(ReactionVesselId):
    pass


class MaterialEntityId(EntityId):
    pass


class BiocatalystId(MaterialEntityId):
    pass


class ReactionMediumId(MaterialEntityId):
    pass


class LiquidPhaseId(MaterialEntityId):
    pass


class SolidPhaseId(MaterialEntityId):
    pass


class GasPhaseId(MaterialEntityId):
    pass


class StartingMaterialId(MaterialEntityId):
    pass


class ReagentId(MaterialEntityId):
    pass


class ChemicalProductId(MaterialEntityId):
    pass


class MaterialSampleId(EvaluatedEntityId):
    pass


class SubstanceSampleId(MaterialSampleId):
    pass


class BiocatalystPreparationId(SubstanceSampleId):
    pass


class PurifiedEnzymePreparationId(BiocatalystPreparationId):
    pass


class CrudeCellExtractPreparationId(BiocatalystPreparationId):
    pass


class WholeCellPreparationId(BiocatalystPreparationId):
    pass


class SecretedEnzymePreparationId(BiocatalystPreparationId):
    pass


class CellFreePreparationId(BiocatalystPreparationId):
    pass


class ImmobilisedPreparationId(BiocatalystPreparationId):
    pass


class PolymerSampleId(SubstanceSampleId):
    pass


@dataclass(repr=False)
class Activity(YAMLRoot):
    """
    See [DCAT-AP specs:Activity](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Activity)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Activity

    id: Union[str, ActivityId] = None
    title: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    had_input_entity: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    had_output_entity: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    had_input_activity: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    carried_out_by: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    part_of: Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]] = empty_dict()
    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ActivityId):
            self.id = ActivityId(self.id)

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="other_identifier", slot_type=Identifier, key_name="notation", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Activity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_input_entity", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_output_entity", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="had_input_activity", slot_type=Activity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="carried_out_by", slot_type=AgenticEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_qualitative_attribute", slot_type=QualitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_quantitative_attribute", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Activity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Agent(YAMLRoot):
    """
    See [DCAT-AP specs:Agent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Agent)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Agent"]
    class_class_curie: ClassVar[str] = "foaf:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Agent

    name: Union[str, list[str]] = None
    type: Optional[Union[dict, "Concept"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, list):
            self.name = [self.name] if self.name is not None else []
        self.name = [v if isinstance(v, str) else str(v) for v in self.name]

        if self.type is not None and not isinstance(self.type, Concept):
            self.type = Concept(**as_dict(self.type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnzymeMLCreator(Agent):
    """
    An author or contributor of an EnzymeML document, with the given/family name split and email address EnzymeML
    captures.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["person"]
    class_class_curie: ClassVar[str] = "schema:person"
    class_name: ClassVar[str] = "EnzymeMLCreator"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnzymeMLCreator

    name: Union[str, list[str]] = None
    given_name: Optional[Union[str, list[str]]] = empty_list()
    family_name: Optional[Union[str, list[str]]] = empty_list()
    mail: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.given_name, list):
            self.given_name = [self.given_name] if self.given_name is not None else []
        self.given_name = [v if isinstance(v, str) else str(v) for v in self.given_name]

        if not isinstance(self.family_name, list):
            self.family_name = [self.family_name] if self.family_name is not None else []
        self.family_name = [v if isinstance(v, str) else str(v) for v in self.family_name]

        if not isinstance(self.mail, list):
            self.mail = [self.mail] if self.mail is not None else []
        self.mail = [v if isinstance(v, str) else str(v) for v in self.mail]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AgenticEntity(YAMLRoot):
    """
    An entity that is somehow responsible for an Activity to take place.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "AgenticEntity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.AgenticEntity

    id: Union[str, AgenticEntityId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]] = empty_dict()
    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AgenticEntityId):
            self.id = AgenticEntityId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="other_identifier", slot_type=Identifier, key_name="notation", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_qualitative_attribute", slot_type=QualitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_quantitative_attribute", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=AgenticEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=AgenticEntity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class Catalogue(YAMLRoot):
    """
    See [DCAT-AP specs:Catalogue](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Catalogue)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Catalog"]
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "Catalogue"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Catalogue

    description: Union[str, list[str]] = None
    publisher: Union[dict, Agent] = None
    title: Union[str, list[str]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    catalogue: Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]] = empty_list()
    creator: Optional[Union[dict, Agent]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    has_dataset: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    has_part: Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]] = empty_list()
    homepage: Optional[Union[dict, "Document"]] = None
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    modification_date: Optional[Union[str, XSDDate]] = None
    record: Optional[Union[Union[dict, "CatalogueRecord"], list[Union[dict, "CatalogueRecord"]]]] = empty_list()
    release_date: Optional[Union[str, XSDDate]] = None
    rights: Optional[Union[dict, "RightsStatement"]] = None
    service: Optional[Union[Union[dict, "DataService"], list[Union[dict, "DataService"]]]] = empty_list()
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()
    themes: Optional[Union[Union[dict, "ConceptScheme"], list[Union[dict, "ConceptScheme"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.publisher):
            self.MissingRequiredField("publisher")
        if not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="catalogue", slot_type=Catalogue, key_name="description", keyed=False)

        if self.creator is not None and not isinstance(self.creator, Agent):
            self.creator = Agent(**as_dict(self.creator))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        self._normalize_inlined_as_list(slot_name="has_dataset", slot_type=Dataset, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Catalogue, key_name="description", keyed=False)

        if self.homepage is not None and not isinstance(self.homepage, Document):
            self.homepage = Document(**as_dict(self.homepage))

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        self._normalize_inlined_as_list(slot_name="record", slot_type=CatalogueRecord, key_name="modification_date", keyed=False)

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self.rights is not None and not isinstance(self.rights, RightsStatement):
            self.rights = RightsStatement(**as_dict(self.rights))

        self._normalize_inlined_as_list(slot_name="service", slot_type=DataService, key_name="title", keyed=False)

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        self._normalize_inlined_as_list(slot_name="themes", slot_type=ConceptScheme, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalogueRecord(YAMLRoot):
    """
    See [DCAT-AP specs:CatalogueRecord](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#CatalogueRecord)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["CatalogRecord"]
    class_class_curie: ClassVar[str] = "dcat:CatalogRecord"
    class_name: ClassVar[str] = "CatalogueRecord"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.CatalogueRecord

    modification_date: Union[str, XSDDate] = None
    primary_topic: Union[dict, Any] = None
    application_profile: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    change_type: Optional[Union[dict, "Concept"]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    listing_date: Optional[Union[str, XSDDate]] = None
    source_metadata: Optional[Union[dict, "CatalogueRecord"]] = None
    title: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.modification_date):
            self.MissingRequiredField("modification_date")
        if not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if not isinstance(self.application_profile, list):
            self.application_profile = [self.application_profile] if self.application_profile is not None else []
        self.application_profile = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.application_profile]

        if self.change_type is not None and not isinstance(self.change_type, Concept):
            self.change_type = Concept(**as_dict(self.change_type))

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.listing_date is not None and not isinstance(self.listing_date, XSDDate):
            self.listing_date = XSDDate(self.listing_date)

        if self.source_metadata is not None and not isinstance(self.source_metadata, CatalogueRecord):
            self.source_metadata = CatalogueRecord(**as_dict(self.source_metadata))

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Checksum(YAMLRoot):
    """
    See [DCAT-AP specs:Checksum](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Checksum)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["Checksum"]
    class_class_curie: ClassVar[str] = "spdx:Checksum"
    class_name: ClassVar[str] = "Checksum"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Checksum

    algorithm: Union[dict, "ChecksumAlgorithm"] = None
    checksum_value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.algorithm):
            self.MissingRequiredField("algorithm")
        if not isinstance(self.algorithm, ChecksumAlgorithm):
            self.algorithm = ChecksumAlgorithm(**as_dict(self.algorithm))

        if self._is_empty(self.checksum_value):
            self.MissingRequiredField("checksum_value")
        if not isinstance(self.checksum_value, str):
            self.checksum_value = str(self.checksum_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ClassifierMixin(YAMLRoot):
    """
    A mixin with which an entity of this schema can be classified via an additional rdf:type or dcterms:type assertion.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCATAPPLUS["ClassifierMixin"]
    class_class_curie: ClassVar[str] = "dcatapplus:ClassifierMixin"
    class_name: ClassVar[str] = "ClassifierMixin"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ClassifierMixin

    type: Optional[Union[dict, "DefinedTerm"]] = None
    rdf_type: Optional[Union[dict, "DefinedTerm"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataGeneratingActivity(Activity):
    """
    An Activity (process) that has the objective to produce information (in form of a dataset) about another Activity
    or Entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "DataGeneratingActivity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DataGeneratingActivity

    id: Union[str, DataGeneratingActivityId] = None
    evaluated_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()
    evaluated_activity: Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, "EvaluatedActivity"]], list[Union[dict, "EvaluatedActivity"]]]] = empty_dict()
    realized_plan: Optional[Union[dict, "Plan"]] = None
    occurred_in: Optional[Union[dict, "Surrounding"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataGeneratingActivityId):
            self.id = DataGeneratingActivityId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="evaluated_activity", slot_type=EvaluatedActivity, key_name="id", keyed=True)

        if self.realized_plan is not None and not isinstance(self.realized_plan, Plan):
            self.realized_plan = Plan(**as_dict(self.realized_plan))

        if self.occurred_in is not None and not isinstance(self.occurred_in, Surrounding):
            self.occurred_in = Surrounding(**as_dict(self.occurred_in))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiocatalyticExperiment(DataGeneratingActivity):
    """
    A DataGeneratingActivity representing a biocatalytic experiment carried out according to the STRENDA Biocatalysis
    Guidelines. The BiocatalyticReaction is the evaluated activity; all STRENDA modules (biocatalyst, components,
    vessel, operation mode, conditions, sampling, results) attach to or via this class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000066"]
    class_class_curie: ClassVar[str] = "OBI:0000066"
    class_name: ClassVar[str] = "BiocatalyticExperiment"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.BiocatalyticExperiment

    id: Union[str, BiocatalyticExperimentId] = None
    has_operation_mode: Union[str, "OperationModeEnum"] = None
    used_biocatalyst_preparation: Optional[Union[dict[Union[str, BiocatalystPreparationId], Union[dict, "BiocatalystPreparation"]], list[Union[dict, "BiocatalystPreparation"]]]] = empty_dict()
    has_biocatalytic_component: Optional[Union[dict[Union[str, BiocatalyticComponentId], Union[dict, "BiocatalyticComponent"]], list[Union[dict, "BiocatalyticComponent"]]]] = empty_dict()
    used_reaction_vessel: Optional[Union[dict[Union[str, ReactionVesselId], Union[dict, "ReactionVessel"]], list[Union[dict, "ReactionVessel"]]]] = empty_dict()
    has_sampling_process: Optional[Union[dict[Union[str, SamplingProcessId], Union[dict, "SamplingProcess"]], list[Union[dict, "SamplingProcess"]]]] = empty_dict()
    has_enzyme_measurement: Optional[Union[dict[Union[str, EnzymeMeasurementId], Union[dict, "EnzymeMeasurement"]], list[Union[dict, "EnzymeMeasurement"]]]] = empty_dict()
    has_molecular_complex: Optional[Union[dict[Union[str, MolecularComplexId], Union[dict, "MolecularComplex"]], list[Union[dict, "MolecularComplex"]]]] = empty_dict()
    evaluated_activity: Optional[Union[dict[Union[str, BiocatalyticReactionId], Union[dict, "BiocatalyticReaction"]], list[Union[dict, "BiocatalyticReaction"]]]] = empty_dict()
    occurred_in: Optional[Union[dict, "Laboratory"]] = None
    carried_out_by: Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, AgenticEntity]], list[Union[dict, AgenticEntity]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiocatalyticExperimentId):
            self.id = BiocatalyticExperimentId(self.id)

        if self._is_empty(self.has_operation_mode):
            self.MissingRequiredField("has_operation_mode")
        if not isinstance(self.has_operation_mode, OperationModeEnum):
            self.has_operation_mode = OperationModeEnum(self.has_operation_mode)

        self._normalize_inlined_as_list(slot_name="used_biocatalyst_preparation", slot_type=BiocatalystPreparation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_biocatalytic_component", slot_type=BiocatalyticComponent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_reaction_vessel", slot_type=ReactionVessel, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_sampling_process", slot_type=SamplingProcess, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_enzyme_measurement", slot_type=EnzymeMeasurement, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_molecular_complex", slot_type=MolecularComplex, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="evaluated_activity", slot_type=BiocatalyticReaction, key_name="id", keyed=True)

        if self.occurred_in is not None and not isinstance(self.occurred_in, Laboratory):
            self.occurred_in = Laboratory(**as_dict(self.occurred_in))

        self._normalize_inlined_as_list(slot_name="carried_out_by", slot_type=AgenticEntity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubstanceSampleCharacterization(DataGeneratingActivity):
    """
    A DataGeneratingActivity that produces data about a SubstanceSample, such as a spectroscopic measurement, a
    physical property determination, or a combined measurement-and-analysis workflow. This is a coarse-grained
    convenience shape that does not distinguish between raw data acquisition and subsequent data processing or
    analysis. Domain-specific sub-profiles that need this distinction should define their own DataGeneratingActivity
    subclasses and use the DCAT-AP+ DataAnalysis chain to separate raw measurement from derived results.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "SubstanceSampleCharacterization"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SubstanceSampleCharacterization

    id: Union[str, SubstanceSampleCharacterizationId] = None
    evaluated_entity: Optional[Union[dict[Union[str, SubstanceSampleId], Union[dict, "SubstanceSample"]], list[Union[dict, "SubstanceSample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubstanceSampleCharacterizationId):
            self.id = SubstanceSampleCharacterizationId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=SubstanceSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReactionMonitoring(DataGeneratingActivity):
    """
    A DataGeneratingActivity that produces data about a ChemicalReaction, such as reaction monitoring, experimental
    documentation, or a combined recording-and-evaluation workflow. This is a coarse-grained convenience shape that
    does not distinguish between raw experimental recording and subsequent data evaluation. Domain-specific
    sub-profiles that need this distinction should define their own DataGeneratingActivity subclasses and use the
    DCAT-AP+ DataAnalysis chain to separate raw data from derived results.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "ReactionMonitoring"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ReactionMonitoring

    id: Union[str, ReactionMonitoringId] = None
    evaluated_activity: Optional[Union[dict[Union[str, ChemicalReactionId], Union[dict, "ChemicalReaction"]], list[Union[dict, "ChemicalReaction"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionMonitoringId):
            self.id = ReactionMonitoringId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_activity", slot_type=ChemicalReaction, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataAnalysis(DataGeneratingActivity):
    """
    An Activity that evaluates the data produced by another Activity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "DataAnalysis"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DataAnalysis

    id: Union[str, DataAnalysisId] = None
    evaluated_entity: Optional[Union[dict[Union[str, AnalysisSourceDataId], Union[dict, "AnalysisSourceData"]], list[Union[dict, "AnalysisSourceData"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataAnalysisId):
            self.id = DataAnalysisId(self.id)

        self._normalize_inlined_as_list(slot_name="evaluated_entity", slot_type=AnalysisSourceData, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataService(YAMLRoot):
    """
    See [DCAT-AP specs:DataService](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DataService)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DataService"]
    class_class_curie: ClassVar[str] = "dcat:DataService"
    class_name: ClassVar[str] = "DataService"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DataService

    endpoint_URL: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()
    title: Union[str, list[str]] = None
    access_rights: Optional[Union[dict, "RightsStatement"]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    conforms_to: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    description: Optional[Union[str, list[str]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    endpoint_description: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    format: Optional[Union[Union[dict, "MediaTypeOrExtent"], list[Union[dict, "MediaTypeOrExtent"]]]] = empty_list()
    keyword: Optional[Union[str, list[str]]] = empty_list()
    landing_page: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    publisher: Optional[Union[dict, Agent]] = None
    serves_dataset: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    theme: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.endpoint_URL):
            self.MissingRequiredField("endpoint_URL")
        self._normalize_inlined_as_list(slot_name="endpoint_URL", slot_type=Resource, key_name="id", keyed=True)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self.access_rights is not None and not isinstance(self.access_rights, RightsStatement):
            self.access_rights = RightsStatement(**as_dict(self.access_rights))

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.conforms_to, list):
            self.conforms_to = [self.conforms_to] if self.conforms_to is not None else []
        self.conforms_to = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.conforms_to]

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="endpoint_description", slot_type=Resource, key_name="id", keyed=True)

        if not isinstance(self.format, list):
            self.format = [self.format] if self.format is not None else []
        self.format = [v if isinstance(v, MediaTypeOrExtent) else MediaTypeOrExtent(**as_dict(v)) for v in self.format]

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        self._normalize_inlined_as_list(slot_name="landing_page", slot_type=Document, key_name="id", keyed=True)

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        self._normalize_inlined_as_list(slot_name="serves_dataset", slot_type=Dataset, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="theme", slot_type=Concept, key_name="preferred_label", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A collection of data, published or curated by a single agent, and available for access or download in one or more
    representations.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Dataset

    id: Union[str, DatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]] = empty_dict()
    access_rights: Optional[Union[dict, "RightsStatement"]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    conforms_to: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    creator: Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]] = empty_list()
    dataset_distribution: Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    frequency: Optional[Union[dict, "Frequency"]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    has_version: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    identifier: Optional[Union[str, list[str]]] = empty_list()
    in_series: Optional[Union[Union[dict, "DatasetSeries"], list[Union[dict, "DatasetSeries"]]]] = empty_list()
    is_referenced_by: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    keyword: Optional[Union[str, list[str]]] = empty_list()
    landing_page: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    modification_date: Optional[Union[str, XSDDate]] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    provenance: Optional[Union[Union[dict, "ProvenanceStatement"], list[Union[dict, "ProvenanceStatement"]]]] = empty_list()
    publisher: Optional[Union[dict, Agent]] = None
    qualified_attribution: Optional[Union[Union[dict, "Attribution"], list[Union[dict, "Attribution"]]]] = empty_list()
    qualified_relation: Optional[Union[Union[dict, "Relationship"], list[Union[dict, "Relationship"]]]] = empty_list()
    related_resource: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    release_date: Optional[Union[str, XSDDate]] = None
    sample: Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]] = empty_list()
    source: Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]] = empty_dict()
    spatial_resolution: Optional[Decimal] = None
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()
    temporal_resolution: Optional[str] = None
    theme: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()
    type: Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]] = empty_list()
    version: Optional[str] = None
    version_notes: Optional[Union[str, list[str]]] = empty_list()
    is_about_entity: Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, "EvaluatedEntity"]], list[Union[dict, "EvaluatedEntity"]]]] = empty_dict()
    is_about_activity: Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, "EvaluatedActivity"]], list[Union[dict, "EvaluatedActivity"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self._is_empty(self.was_generated_by):
            self.MissingRequiredField("was_generated_by")
        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataGeneratingActivity, key_name="id", keyed=True)

        if self.access_rights is not None and not isinstance(self.access_rights, RightsStatement):
            self.access_rights = RightsStatement(**as_dict(self.access_rights))

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.conforms_to, list):
            self.conforms_to = [self.conforms_to] if self.conforms_to is not None else []
        self.conforms_to = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.conforms_to]

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        self._normalize_inlined_as_list(slot_name="creator", slot_type=Agent, key_name="name", keyed=False)

        if not isinstance(self.dataset_distribution, list):
            self.dataset_distribution = [self.dataset_distribution] if self.dataset_distribution is not None else []
        self.dataset_distribution = [v if isinstance(v, Distribution) else Distribution(**as_dict(v)) for v in self.dataset_distribution]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        if self.frequency is not None and not isinstance(self.frequency, Frequency):
            self.frequency = Frequency(**as_dict(self.frequency))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        self._normalize_inlined_as_list(slot_name="has_version", slot_type=Dataset, key_name="id", keyed=True)

        if not isinstance(self.identifier, list):
            self.identifier = [self.identifier] if self.identifier is not None else []
        self.identifier = [v if isinstance(v, str) else str(v) for v in self.identifier]

        self._normalize_inlined_as_list(slot_name="in_series", slot_type=DatasetSeries, key_name="description", keyed=False)

        self._normalize_inlined_as_list(slot_name="is_referenced_by", slot_type=Resource, key_name="id", keyed=True)

        if not isinstance(self.keyword, list):
            self.keyword = [self.keyword] if self.keyword is not None else []
        self.keyword = [v if isinstance(v, str) else str(v) for v in self.keyword]

        self._normalize_inlined_as_list(slot_name="landing_page", slot_type=Document, key_name="id", keyed=True)

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        self._normalize_inlined_as_list(slot_name="other_identifier", slot_type=Identifier, key_name="notation", keyed=False)

        if not isinstance(self.provenance, list):
            self.provenance = [self.provenance] if self.provenance is not None else []
        self.provenance = [v if isinstance(v, ProvenanceStatement) else ProvenanceStatement(**as_dict(v)) for v in self.provenance]

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if not isinstance(self.qualified_attribution, list):
            self.qualified_attribution = [self.qualified_attribution] if self.qualified_attribution is not None else []
        self.qualified_attribution = [v if isinstance(v, Attribution) else Attribution(**as_dict(v)) for v in self.qualified_attribution]

        if not isinstance(self.qualified_relation, list):
            self.qualified_relation = [self.qualified_relation] if self.qualified_relation is not None else []
        self.qualified_relation = [v if isinstance(v, Relationship) else Relationship(**as_dict(v)) for v in self.qualified_relation]

        self._normalize_inlined_as_list(slot_name="related_resource", slot_type=Resource, key_name="id", keyed=True)

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if not isinstance(self.sample, list):
            self.sample = [self.sample] if self.sample is not None else []
        self.sample = [v if isinstance(v, Distribution) else Distribution(**as_dict(v)) for v in self.sample]

        self._normalize_inlined_as_list(slot_name="source", slot_type=Dataset, key_name="id", keyed=True)

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, Decimal):
            self.spatial_resolution = Decimal(self.spatial_resolution)

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, str):
            self.temporal_resolution = str(self.temporal_resolution)

        self._normalize_inlined_as_list(slot_name="theme", slot_type=Concept, key_name="preferred_label", keyed=False)

        self._normalize_inlined_as_list(slot_name="type", slot_type=Concept, key_name="preferred_label", keyed=False)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.version_notes, list):
            self.version_notes = [self.version_notes] if self.version_notes is not None else []
        self.version_notes = [v if isinstance(v, str) else str(v) for v in self.version_notes]

        self._normalize_inlined_as_list(slot_name="is_about_entity", slot_type=EvaluatedEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_activity", slot_type=EvaluatedActivity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnzymeMLDocument(Dataset):
    """
    A Dataset that represents a converted EnzymeML document: a container for a biocatalytic experiment's vessels,
    species, reactions, measurements and kinetic model, expressed as STRENDA-Biocatalysis metadata.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["EnzymeMLDocument"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:EnzymeMLDocument"
    class_name: ClassVar[str] = "EnzymeMLDocument"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnzymeMLDocument

    id: Union[str, EnzymeMLDocumentId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Union[dict[Union[str, BiocatalyticExperimentId], Union[dict, BiocatalyticExperiment]], list[Union[dict, BiocatalyticExperiment]]] = empty_dict()
    is_about_activity: Optional[Union[dict[Union[str, BiocatalyticReactionId], Union[dict, "BiocatalyticReaction"]], list[Union[dict, "BiocatalyticReaction"]]]] = empty_dict()
    creator: Optional[Union[Union[dict, EnzymeMLCreator], list[Union[dict, EnzymeMLCreator]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnzymeMLDocumentId):
            self.id = EnzymeMLDocumentId(self.id)

        if self._is_empty(self.was_generated_by):
            self.MissingRequiredField("was_generated_by")
        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=BiocatalyticExperiment, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_activity", slot_type=BiocatalyticReaction, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="creator", slot_type=EnzymeMLCreator, key_name="name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubstanceSampleCharacterizationDataset(Dataset):
    """
    A Dataset about a SubstanceSample that was produced by a SubstanceSampleCharacterization activity. This is a
    coarse-grained convenience shape that conflates measurement and analysis into a single data-generating activity.
    Domain-specific sub-profiles that need to distinguish raw measurement from post-processing or structure assignment
    should define their own Dataset subclasses, potentially using the DCAT-AP+ DataAnalysis/AnalysisDataset chain
    instead of reusing this class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "SubstanceSampleCharacterizationDataset"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SubstanceSampleCharacterizationDataset

    id: Union[str, SubstanceSampleCharacterizationDatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Optional[Union[dict[Union[str, SubstanceSampleCharacterizationId], Union[dict, SubstanceSampleCharacterization]], list[Union[dict, SubstanceSampleCharacterization]]]] = empty_dict()
    is_about_entity: Optional[Union[dict[Union[str, SubstanceSampleId], Union[dict, "SubstanceSample"]], list[Union[dict, "SubstanceSample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubstanceSampleCharacterizationDatasetId):
            self.id = SubstanceSampleCharacterizationDatasetId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=SubstanceSampleCharacterization, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_entity", slot_type=SubstanceSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReactionMonitoringDataset(Dataset):
    """
    A Dataset about a ChemicalReaction that was produced by a ReactionMonitoring activity. This is a coarse-grained
    convenience shape that conflates experimental documentation and analysis into a single data-generating activity.
    Domain-specific sub-profiles that need to distinguish reaction monitoring from subsequent data evaluation should
    define their own Dataset subclasses, potentially using the DCAT-AP+ DataAnalysis/AnalysisDataset chain instead of
    reusing this class.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "ReactionMonitoringDataset"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ReactionMonitoringDataset

    id: Union[str, ReactionMonitoringDatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Optional[Union[dict[Union[str, ReactionMonitoringId], Union[dict, ReactionMonitoring]], list[Union[dict, ReactionMonitoring]]]] = empty_dict()
    is_about_activity: Optional[Union[dict[Union[str, ChemicalReactionId], Union[dict, "ChemicalReaction"]], list[Union[dict, "ChemicalReaction"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionMonitoringDatasetId):
            self.id = ReactionMonitoringDatasetId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=ReactionMonitoring, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="is_about_activity", slot_type=ChemicalReaction, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalysisDataset(Dataset):
    """
    A Dataset that was generated by an analysis of some previously generated data. For example, a dataset that
    contains the data of an assignment of a chemical structure to a sample based on the spectral data obtained from
    the sample is an AnalyticalDataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Dataset"]
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "AnalysisDataset"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.AnalysisDataset

    id: Union[str, AnalysisDatasetId] = None
    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    was_generated_by: Optional[Union[dict[Union[str, DataAnalysisId], Union[dict, DataAnalysis]], list[Union[dict, DataAnalysis]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisDatasetId):
            self.id = AnalysisDatasetId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataAnalysis, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatasetSeries(YAMLRoot):
    """
    See [DCAT-AP specs:DatasetSeries](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#DatasetSeries)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["DatasetSeries"]
    class_class_curie: ClassVar[str] = "dcat:DatasetSeries"
    class_name: ClassVar[str] = "DatasetSeries"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DatasetSeries

    description: Union[str, list[str]] = None
    title: Union[str, list[str]] = None
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    contact_point: Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]] = empty_list()
    frequency: Optional[Union[dict, "Frequency"]] = None
    geographical_coverage: Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]] = empty_list()
    modification_date: Optional[Union[str, XSDDate]] = None
    publisher: Optional[Union[dict, Agent]] = None
    release_date: Optional[Union[str, XSDDate]] = None
    temporal_coverage: Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if not isinstance(self.contact_point, list):
            self.contact_point = [self.contact_point] if self.contact_point is not None else []
        self.contact_point = [v if isinstance(v, Kind) else Kind(**as_dict(v)) for v in self.contact_point]

        if self.frequency is not None and not isinstance(self.frequency, Frequency):
            self.frequency = Frequency(**as_dict(self.frequency))

        if not isinstance(self.geographical_coverage, list):
            self.geographical_coverage = [self.geographical_coverage] if self.geographical_coverage is not None else []
        self.geographical_coverage = [v if isinstance(v, Location) else Location(**as_dict(v)) for v in self.geographical_coverage]

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if self.publisher is not None and not isinstance(self.publisher, Agent):
            self.publisher = Agent(**as_dict(self.publisher))

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if not isinstance(self.temporal_coverage, list):
            self.temporal_coverage = [self.temporal_coverage] if self.temporal_coverage is not None else []
        self.temporal_coverage = [v if isinstance(v, PeriodOfTime) else PeriodOfTime(**as_dict(v)) for v in self.temporal_coverage]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DefinedTerm(YAMLRoot):
    """
    A word, name, acronym or phrase that is defined in a controlled vocabulary (CV) and that is used to provide an
    additional rdf:type or dcterms:type of a class within this schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DefinedTerm"]
    class_class_curie: ClassVar[str] = "schema:DefinedTerm"
    class_name: ClassVar[str] = "DefinedTerm"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DefinedTerm

    id: Union[str, DefinedTermId] = None
    title: Optional[str] = None
    from_CV: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DefinedTermId):
            self.id = DefinedTermId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.from_CV is not None and not isinstance(self.from_CV, URIorCURIE):
            self.from_CV = URIorCURIE(self.from_CV)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Device(AgenticEntity):
    """
    A material instrument that is designed to perform a function primarily by means of its mechanical or electrical
    nature.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Device

    id: Union[str, DeviceId] = None
    has_part: Optional[Union[dict[Union[str, DeviceId], Union[dict, "Device"]], list[Union[dict, "Device"]]]] = empty_dict()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Device, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="other_identifier", slot_type=Identifier, key_name="notation", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MixingImpeller(Device):
    """
    The category of mechanical or magnetic agitation device used to ensure homogeneous mixing within a reaction system
    or mixing vessel, such as a magnetic stirrer or an overhead mechanical (steel shaft) stirrer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0008113"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0008113"
    class_name: ClassVar[str] = "MixingImpeller"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MixingImpeller

    id: Union[str, MixingImpellerId] = None
    stirring_type: Optional[Union[str, list[str]]] = empty_list()
    stirrer_material: Optional[Union[str, list[str]]] = empty_list()
    supplied_by: Optional[Union[dict, Agent]] = None
    number_of_stirrers: Optional[int] = None
    distance_between_stirrers: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    blade_pitch_angle: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    number_of_blades: Optional[int] = None
    blade_size: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    stirrer_geometry: Optional[Union[str, list[str]]] = empty_list()
    stirrer_speed: Optional[Union[Union[dict, "AngularVelocity"], list[Union[dict, "AngularVelocity"]]]] = empty_list()
    height_above_vessel_base: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    power_per_volume_input: Optional[Union[Union[dict, "PowerPerVolume"], list[Union[dict, "PowerPerVolume"]]]] = empty_list()
    stir_bar_size: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    stir_bar_shape: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MixingImpellerId):
            self.id = MixingImpellerId(self.id)

        if not isinstance(self.stirring_type, list):
            self.stirring_type = [self.stirring_type] if self.stirring_type is not None else []
        self.stirring_type = [v if isinstance(v, str) else str(v) for v in self.stirring_type]

        if not isinstance(self.stirrer_material, list):
            self.stirrer_material = [self.stirrer_material] if self.stirrer_material is not None else []
        self.stirrer_material = [v if isinstance(v, str) else str(v) for v in self.stirrer_material]

        if self.supplied_by is not None and not isinstance(self.supplied_by, Agent):
            self.supplied_by = Agent(**as_dict(self.supplied_by))

        if self.number_of_stirrers is not None and not isinstance(self.number_of_stirrers, int):
            self.number_of_stirrers = int(self.number_of_stirrers)

        self._normalize_inlined_as_list(slot_name="distance_between_stirrers", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="blade_pitch_angle", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        if self.number_of_blades is not None and not isinstance(self.number_of_blades, int):
            self.number_of_blades = int(self.number_of_blades)

        self._normalize_inlined_as_list(slot_name="blade_size", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        if not isinstance(self.stirrer_geometry, list):
            self.stirrer_geometry = [self.stirrer_geometry] if self.stirrer_geometry is not None else []
        self.stirrer_geometry = [v if isinstance(v, str) else str(v) for v in self.stirrer_geometry]

        self._normalize_inlined_as_list(slot_name="stirrer_speed", slot_type=AngularVelocity, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="height_above_vessel_base", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="power_per_volume_input", slot_type=PowerPerVolume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="stir_bar_size", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        if not isinstance(self.stir_bar_shape, list):
            self.stir_bar_shape = [self.stir_bar_shape] if self.stir_bar_shape is not None else []
        self.stir_bar_shape = [v if isinstance(v, str) else str(v) for v in self.stir_bar_shape]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Shaker(Device):
    """
    A laboratory equipment with a platform that oscillates in two or three directions. It is used to move and mix the
    mostly liquid contents of different vessels.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("http://opendata.inrae.fr/PO2/Ontology/TransformON/c_uO2UNi")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Shaker"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Shaker

    id: Union[str, ShakerId] = None
    shaking_type: Optional[Union[str, list[str]]] = empty_list()
    deflection: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    shaking_speed: Optional[Union[Union[dict, "AngularVelocity"], list[Union[dict, "AngularVelocity"]]]] = empty_list()
    shaking_position: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ShakerId):
            self.id = ShakerId(self.id)

        if not isinstance(self.shaking_type, list):
            self.shaking_type = [self.shaking_type] if self.shaking_type is not None else []
        self.shaking_type = [v if isinstance(v, str) else str(v) for v in self.shaking_type]

        self._normalize_inlined_as_list(slot_name="deflection", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="shaking_speed", slot_type=AngularVelocity, key_name="value", keyed=False)

        if not isinstance(self.shaking_position, list):
            self.shaking_position = [self.shaking_position] if self.shaking_position is not None else []
        self.shaking_position = [v if isinstance(v, str) else str(v) for v in self.shaking_position]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GasSupplySystem(Device):
    """
    A device that supplies gas to a StirredTankReactor, forming a part of it via has_part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SNOMED["285707009"]
    class_class_curie: ClassVar[str] = "SNOMED:285707009"
    class_name: ClassVar[str] = "GasSupplySystem"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.GasSupplySystem

    id: Union[str, GasSupplySystemId] = None
    has_gas_phase: Optional[Union[dict[Union[str, GasPhaseId], Union[dict, "GasPhase"]], list[Union[dict, "GasPhase"]]]] = empty_dict()
    gas_supply_method: Optional[Union[str, list[str]]] = empty_list()
    has_flow_rate: Optional[Union[Union[dict, "FlowRate"], list[Union[dict, "FlowRate"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GasSupplySystemId):
            self.id = GasSupplySystemId(self.id)

        self._normalize_inlined_as_list(slot_name="has_gas_phase", slot_type=GasPhase, key_name="id", keyed=True)

        if not isinstance(self.gas_supply_method, list):
            self.gas_supply_method = [self.gas_supply_method] if self.gas_supply_method is not None else []
        self.gas_supply_method = [v if isinstance(v, str) else str(v) for v in self.gas_supply_method]

        self._normalize_inlined_as_list(slot_name="has_flow_rate", slot_type=FlowRate, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemperatureControlDevice(Device):
    """
    Equipment used for controlling and/or monitoring the temperature in various parts of a reactor. This can include
    hot plates, heating elements and cryostats.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0000151"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0000151"
    class_name: ClassVar[str] = "TemperatureControlDevice"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.TemperatureControlDevice

    id: Union[str, TemperatureControlDeviceId] = None
    temperature_control_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TemperatureControlDeviceId):
            self.id = TemperatureControlDeviceId(self.id)

        if not isinstance(self.temperature_control_method, list):
            self.temperature_control_method = [self.temperature_control_method] if self.temperature_control_method is not None else []
        self.temperature_control_method = [v if isinstance(v, str) else str(v) for v in self.temperature_control_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Distribution(YAMLRoot):
    """
    See [DCAT-AP specs:Distribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Distribution)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Distribution"]
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "Distribution"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Distribution

    access_URL: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()
    access_service: Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]] = empty_list()
    applicable_legislation: Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]] = empty_dict()
    availability: Optional[Union[dict, "Concept"]] = None
    byte_size: Optional[int] = None
    checksum: Optional[Union[dict, Checksum]] = None
    compression_format: Optional[Union[dict, "MediaType"]] = None
    description: Optional[Union[str, list[str]]] = empty_list()
    documentation: Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]] = empty_dict()
    download_URL: Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]] = empty_dict()
    format: Optional[Union[dict, "MediaTypeOrExtent"]] = None
    has_policy: Optional[Union[dict, "Policy"]] = None
    language: Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]] = empty_list()
    licence: Optional[Union[dict, "LicenseDocument"]] = None
    linked_schemas: Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]] = empty_list()
    media_type: Optional[Union[dict, "MediaType"]] = None
    modification_date: Optional[Union[str, XSDDate]] = None
    packaging_format: Optional[Union[dict, "MediaType"]] = None
    release_date: Optional[Union[str, XSDDate]] = None
    rights: Optional[Union[dict, "RightsStatement"]] = None
    spatial_resolution: Optional[Decimal] = None
    status: Optional[Union[dict, "Concept"]] = None
    temporal_resolution: Optional[str] = None
    title: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.access_URL):
            self.MissingRequiredField("access_URL")
        self._normalize_inlined_as_list(slot_name="access_URL", slot_type=Resource, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="access_service", slot_type=DataService, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="applicable_legislation", slot_type=LegalResource, key_name="id", keyed=True)

        if self.availability is not None and not isinstance(self.availability, Concept):
            self.availability = Concept(**as_dict(self.availability))

        if self.byte_size is not None and not isinstance(self.byte_size, int):
            self.byte_size = int(self.byte_size)

        if self.checksum is not None and not isinstance(self.checksum, Checksum):
            self.checksum = Checksum(**as_dict(self.checksum))

        if self.compression_format is not None and not isinstance(self.compression_format, MediaType):
            self.compression_format = MediaType(**as_dict(self.compression_format))

        if not isinstance(self.description, list):
            self.description = [self.description] if self.description is not None else []
        self.description = [v if isinstance(v, str) else str(v) for v in self.description]

        self._normalize_inlined_as_list(slot_name="documentation", slot_type=Document, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="download_URL", slot_type=Resource, key_name="id", keyed=True)

        if self.format is not None and not isinstance(self.format, MediaTypeOrExtent):
            self.format = MediaTypeOrExtent(**as_dict(self.format))

        if self.has_policy is not None and not isinstance(self.has_policy, Policy):
            self.has_policy = Policy(**as_dict(self.has_policy))

        if not isinstance(self.language, list):
            self.language = [self.language] if self.language is not None else []
        self.language = [v if isinstance(v, LinguisticSystem) else LinguisticSystem(**as_dict(v)) for v in self.language]

        if self.licence is not None and not isinstance(self.licence, LicenseDocument):
            self.licence = LicenseDocument(**as_dict(self.licence))

        if not isinstance(self.linked_schemas, list):
            self.linked_schemas = [self.linked_schemas] if self.linked_schemas is not None else []
        self.linked_schemas = [v if isinstance(v, Standard) else Standard(**as_dict(v)) for v in self.linked_schemas]

        if self.media_type is not None and not isinstance(self.media_type, MediaType):
            self.media_type = MediaType(**as_dict(self.media_type))

        if self.modification_date is not None and not isinstance(self.modification_date, XSDDate):
            self.modification_date = XSDDate(self.modification_date)

        if self.packaging_format is not None and not isinstance(self.packaging_format, MediaType):
            self.packaging_format = MediaType(**as_dict(self.packaging_format))

        if self.release_date is not None and not isinstance(self.release_date, XSDDate):
            self.release_date = XSDDate(self.release_date)

        if self.rights is not None and not isinstance(self.rights, RightsStatement):
            self.rights = RightsStatement(**as_dict(self.rights))

        if self.spatial_resolution is not None and not isinstance(self.spatial_resolution, Decimal):
            self.spatial_resolution = Decimal(self.spatial_resolution)

        if self.status is not None and not isinstance(self.status, Concept):
            self.status = Concept(**as_dict(self.status))

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, str):
            self.temporal_resolution = str(self.temporal_resolution)

        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    A physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Entity

    id: Union[str, EntityId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()
    has_qualitative_attribute: Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]] = empty_list()
    has_quantitative_attribute: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    part_of: Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]] = empty_dict()
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="other_identifier", slot_type=Identifier, key_name="notation", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_qualitative_attribute", slot_type=QualitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_quantitative_attribute", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Entity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="part_of", slot_type=Entity, key_name="id", keyed=True)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluatedActivity(Activity):
    """
    An activity or process that is being evaluated in a DataGeneratingActivity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "EvaluatedActivity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EvaluatedActivity

    id: Union[str, EvaluatedActivityId] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluatedActivityId):
            self.id = EvaluatedActivityId(self.id)

        self._normalize_inlined_as_list(slot_name="other_identifier", slot_type=Identifier, key_name="notation", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlannedProcess(EvaluatedActivity):
    """
    A process that realizes a plan — i.e. it is carried out with the intention of achieving a specified objective.
    (OBI:0000011 stub)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000011"]
    class_class_curie: ClassVar[str] = "OBI:0000011"
    class_name: ClassVar[str] = "PlannedProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PlannedProcess

    id: Union[str, PlannedProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlannedProcessId):
            self.id = PlannedProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemperatureShiftProcess(PlannedProcess):
    """
    A PlannedProcess representing an event-based change in temperature during a biocatalytic reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["TemperatureShiftProcess"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:TemperatureShiftProcess"
    class_name: ClassVar[str] = "TemperatureShiftProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.TemperatureShiftProcess

    id: Union[str, TemperatureShiftProcessId] = None
    has_temperature_before: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_temperature_after: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_trigger_event: Optional[Union[str, list[str]]] = empty_list()
    has_temperature_at_timepoint: Optional[Union[Union[dict, "TemperatureTimepoint"], list[Union[dict, "TemperatureTimepoint"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TemperatureShiftProcessId):
            self.id = TemperatureShiftProcessId(self.id)

        self._normalize_inlined_as_list(slot_name="has_temperature_before", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_temperature_after", slot_type=Temperature, key_name="value", keyed=False)

        if not isinstance(self.has_trigger_event, list):
            self.has_trigger_event = [self.has_trigger_event] if self.has_trigger_event is not None else []
        self.has_trigger_event = [v if isinstance(v, str) else str(v) for v in self.has_trigger_event]

        self._normalize_inlined_as_list(slot_name="has_temperature_at_timepoint", slot_type=TemperatureTimepoint, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemperatureGradient(PlannedProcess):
    """
    A PlannedProcess representing a dynamic temperature gradient applied over distance or time in a tubular flow
    reactor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["TemperatureGradient"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:TemperatureGradient"
    class_name: ClassVar[str] = "TemperatureGradient"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.TemperatureGradient

    id: Union[str, TemperatureGradientId] = None
    has_temperature_start: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_temperature_end: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_gradient_length: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    has_measurement_points: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TemperatureGradientId):
            self.id = TemperatureGradientId(self.id)

        self._normalize_inlined_as_list(slot_name="has_temperature_start", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_temperature_end", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_gradient_length", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        if not isinstance(self.has_measurement_points, list):
            self.has_measurement_points = [self.has_measurement_points] if self.has_measurement_points is not None else []
        self.has_measurement_points = [v if isinstance(v, str) else str(v) for v in self.has_measurement_points]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PHShiftProcess(PlannedProcess):
    """
    A PlannedProcess representing an event-based change in pH during a biocatalytic reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["PHShiftProcess"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:PHShiftProcess"
    class_name: ClassVar[str] = "PHShiftProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PHShiftProcess

    id: Union[str, PHShiftProcessId] = None
    has_ph_before: Optional[Union[Union[dict, "PHValue"], list[Union[dict, "PHValue"]]]] = empty_list()
    has_ph_after: Optional[Union[Union[dict, "PHValue"], list[Union[dict, "PHValue"]]]] = empty_list()
    has_trigger_event: Optional[Union[str, list[str]]] = empty_list()
    has_ph_at_timepoint: Optional[Union[Union[dict, "PHValue"], list[Union[dict, "PHValue"]]]] = empty_list()
    has_ph_measurement: Optional[Union[dict, "PHMeasurementProcess"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PHShiftProcessId):
            self.id = PHShiftProcessId(self.id)

        self._normalize_inlined_as_list(slot_name="has_ph_before", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_after", slot_type=PHValue, key_name="value", keyed=False)

        if not isinstance(self.has_trigger_event, list):
            self.has_trigger_event = [self.has_trigger_event] if self.has_trigger_event is not None else []
        self.has_trigger_event = [v if isinstance(v, str) else str(v) for v in self.has_trigger_event]

        self._normalize_inlined_as_list(slot_name="has_ph_at_timepoint", slot_type=PHValue, key_name="value", keyed=False)

        if self.has_ph_measurement is not None and not isinstance(self.has_ph_measurement, PHMeasurementProcess):
            self.has_ph_measurement = PHMeasurementProcess(**as_dict(self.has_ph_measurement))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PHGradient(PlannedProcess):
    """
    A PlannedProcess representing a dynamic pH gradient applied over distance or time in a tubular flow reactor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["PHGradient"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:PHGradient"
    class_name: ClassVar[str] = "PHGradient"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PHGradient

    id: Union[str, PHGradientId] = None
    has_ph_start: Optional[Union[Union[dict, "PHValue"], list[Union[dict, "PHValue"]]]] = empty_list()
    has_ph_end: Optional[Union[Union[dict, "PHValue"], list[Union[dict, "PHValue"]]]] = empty_list()
    has_gradient_length: Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]] = empty_list()
    has_measurement_points: Optional[Union[str, list[str]]] = empty_list()
    has_ph_measurement: Optional[Union[dict, "PHMeasurementProcess"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PHGradientId):
            self.id = PHGradientId(self.id)

        self._normalize_inlined_as_list(slot_name="has_ph_start", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_end", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_gradient_length", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        if not isinstance(self.has_measurement_points, list):
            self.has_measurement_points = [self.has_measurement_points] if self.has_measurement_points is not None else []
        self.has_measurement_points = [v if isinstance(v, str) else str(v) for v in self.has_measurement_points]

        if self.has_ph_measurement is not None and not isinstance(self.has_ph_measurement, PHMeasurementProcess):
            self.has_ph_measurement = PHMeasurementProcess(**as_dict(self.has_ph_measurement))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplingProcess(PlannedProcess):
    """
    A specimen gathering process with the objective to obtain a specimen that is representative of the input material
    entity
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000744"]
    class_class_curie: ClassVar[str] = "OBI:0000744"
    class_name: ClassVar[str] = "SamplingProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SamplingProcess

    id: Union[str, SamplingProcessId] = None
    has_sample_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_sampling_timepoint: Optional[Union[Union[dict, "SamplingTimepoint"], list[Union[dict, "SamplingTimepoint"]]]] = empty_list()
    mixing_during_sampling: Optional[Union[bool, Bool]] = None
    vessel_opened_for_sampling: Optional[Union[bool, Bool]] = None
    has_gas_phase: Optional[Union[dict[Union[str, GasPhaseId], Union[dict, "GasPhase"]], list[Union[dict, "GasPhase"]]]] = empty_dict()
    sampled_from_phase: Optional[Union[dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], list[Union[dict, "MaterialEntity"]]]] = empty_dict()
    biocatalyst_contamination_possible: Optional[Union[bool, Bool]] = None
    had_output_entity: Optional[Union[dict[Union[str, MaterialSampleId], Union[dict, "MaterialSample"]], list[Union[dict, "MaterialSample"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplingProcessId):
            self.id = SamplingProcessId(self.id)

        self._normalize_inlined_as_list(slot_name="has_sample_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_sampling_timepoint", slot_type=SamplingTimepoint, key_name="value", keyed=False)

        if self.mixing_during_sampling is not None and not isinstance(self.mixing_during_sampling, Bool):
            self.mixing_during_sampling = Bool(self.mixing_during_sampling)

        if self.vessel_opened_for_sampling is not None and not isinstance(self.vessel_opened_for_sampling, Bool):
            self.vessel_opened_for_sampling = Bool(self.vessel_opened_for_sampling)

        self._normalize_inlined_as_list(slot_name="has_gas_phase", slot_type=GasPhase, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sampled_from_phase", slot_type=MaterialEntity, key_name="id", keyed=True)

        if self.biocatalyst_contamination_possible is not None and not isinstance(self.biocatalyst_contamination_possible, Bool):
            self.biocatalyst_contamination_possible = Bool(self.biocatalyst_contamination_possible)

        self._normalize_inlined_as_list(slot_name="had_output_entity", slot_type=MaterialSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialProcessing(PlannedProcess):
    """
    A process that affects the physical qualities of materials or creates, destroys or converts materials. [Allotrope]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFP["0003275"]
    class_class_curie: ClassVar[str] = "AFP:0003275"
    class_name: ClassVar[str] = "MaterialProcessing"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MaterialProcessing

    id: Union[str, MaterialProcessingId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialProcessingId):
            self.id = MaterialProcessingId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DryingProcess(MaterialProcessing):
    """
    The process of removing a solvent from a substance. [CHMO]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFP["0001876"]
    class_class_curie: ClassVar[str] = "AFP:0001876"
    class_name: ClassVar[str] = "DryingProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DryingProcess

    id: Union[str, DryingProcessId] = None
    drying_method_type: Optional[Union[str, "DryingMethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DryingProcessId):
            self.id = DryingProcessId(self.id)

        if self.drying_method_type is not None and not isinstance(self.drying_method_type, DryingMethodEnum):
            self.drying_method_type = DryingMethodEnum(self.drying_method_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiocatalystProductionProcess(MaterialProcessing):
    """
    A MaterialProcessing that describes how a biocatalyst was produced, including the production organism, plasmid,
    and purification steps. Only present when Biocatalyst.is_self_produced is true.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["BiocatalystProductionProcess"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:BiocatalystProductionProcess"
    class_name: ClassVar[str] = "BiocatalystProductionProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.BiocatalystProductionProcess

    id: Union[str, BiocatalystProductionProcessId] = None
    production_organism: Optional[Union[str, list[str]]] = empty_list()
    sequence_plasmid: Optional[Union[str, list[str]]] = empty_list()
    plasmid_specifications: Optional[Union[str, list[str]]] = empty_list()
    purification_method: Optional[Union[str, list[str]]] = empty_list()
    has_purity: Optional[Union[Union[dict, "Purity"], list[Union[dict, "Purity"]]]] = empty_list()
    purity_specification: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiocatalystProductionProcessId):
            self.id = BiocatalystProductionProcessId(self.id)

        if not isinstance(self.production_organism, list):
            self.production_organism = [self.production_organism] if self.production_organism is not None else []
        self.production_organism = [v if isinstance(v, str) else str(v) for v in self.production_organism]

        if not isinstance(self.sequence_plasmid, list):
            self.sequence_plasmid = [self.sequence_plasmid] if self.sequence_plasmid is not None else []
        self.sequence_plasmid = [v if isinstance(v, str) else str(v) for v in self.sequence_plasmid]

        if not isinstance(self.plasmid_specifications, list):
            self.plasmid_specifications = [self.plasmid_specifications] if self.plasmid_specifications is not None else []
        self.plasmid_specifications = [v if isinstance(v, str) else str(v) for v in self.plasmid_specifications]

        if not isinstance(self.purification_method, list):
            self.purification_method = [self.purification_method] if self.purification_method is not None else []
        self.purification_method = [v if isinstance(v, str) else str(v) for v in self.purification_method]

        self._normalize_inlined_as_list(slot_name="has_purity", slot_type=Purity, key_name="value", keyed=False)

        if not isinstance(self.purity_specification, list):
            self.purity_specification = [self.purity_specification] if self.purity_specification is not None else []
        self.purity_specification = [v if isinstance(v, str) else str(v) for v in self.purity_specification]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplePreparationProcess(MaterialProcessing):
    """
    Methods by which physical/chemical processing of samples are performed prior to chemical analysis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAO["000043"]
    class_class_curie: ClassVar[str] = "CAO:000043"
    class_name: ClassVar[str] = "SamplePreparationProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SamplePreparationProcess

    id: Union[str, SamplePreparationProcessId] = None
    has_part: Optional[Union[dict[Union[str, MaterialProcessingId], Union[dict, MaterialProcessing]], list[Union[dict, MaterialProcessing]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplePreparationProcessId):
            self.id = SamplePreparationProcessId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=MaterialProcessing, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuenchingProcess(MaterialProcessing):
    """
    Material processing in which a sample is cooled by immersion in a fluid.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002917"]
    class_class_curie: ClassVar[str] = "CHMO:0002917"
    class_name: ClassVar[str] = "QuenchingProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.QuenchingProcess

    id: Union[str, QuenchingProcessId] = None
    quenching_method_type: Optional[Union[str, list[str]]] = empty_list()
    has_quenching_ratio: Optional[Union[Union[dict, "QuenchingRatio"], list[Union[dict, "QuenchingRatio"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QuenchingProcessId):
            self.id = QuenchingProcessId(self.id)

        if not isinstance(self.quenching_method_type, list):
            self.quenching_method_type = [self.quenching_method_type] if self.quenching_method_type is not None else []
        self.quenching_method_type = [v if isinstance(v, str) else str(v) for v in self.quenching_method_type]

        self._normalize_inlined_as_list(slot_name="has_quenching_ratio", slot_type=QuenchingRatio, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleTreatmentProcess(MaterialProcessing):
    """
    Additional sample processing steps applied after quenching (e.g. filtration, centrifugation, dilution).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["SampleTreatmentProcess"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:SampleTreatmentProcess"
    class_name: ClassVar[str] = "SampleTreatmentProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SampleTreatmentProcess

    id: Union[str, SampleTreatmentProcessId] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleTreatmentProcessId):
            self.id = SampleTreatmentProcessId(self.id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasurementProcess(PlannedProcess):
    """
    A planned process that has the objective to produce information about a material entity by examining it.
    (OBI:0000070 stub)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "MeasurementProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MeasurementProcess

    id: Union[str, MeasurementProcessId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementProcessId):
            self.id = MeasurementProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PHMeasurementProcess(MeasurementProcess):
    """
    A MeasurementProcess capturing the method and context of pH measurement, including when it was measured and by
    which method. Retained for reproducibility provenance; acknowledged as potentially deeper than strictly necessary
    for this schema.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000070"]
    class_class_curie: ClassVar[str] = "OBI:0000070"
    class_name: ClassVar[str] = "PHMeasurementProcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PHMeasurementProcess

    id: Union[str, PHMeasurementProcessId] = None
    has_ph_value: Optional[Union[Union[dict, "PHValue"], list[Union[dict, "PHValue"]]]] = empty_list()
    detected_when: Optional[Union[str, list[str]]] = empty_list()
    detected_how: Optional[Union[str, list[str]]] = empty_list()
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_calibration_info: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PHMeasurementProcessId):
            self.id = PHMeasurementProcessId(self.id)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        if not isinstance(self.detected_when, list):
            self.detected_when = [self.detected_when] if self.detected_when is not None else []
        self.detected_when = [v if isinstance(v, str) else str(v) for v in self.detected_when]

        if not isinstance(self.detected_how, list):
            self.detected_how = [self.detected_how] if self.detected_how is not None else []
        self.detected_how = [v if isinstance(v, str) else str(v) for v in self.detected_how]

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        if not isinstance(self.has_calibration_info, list):
            self.has_calibration_info = [self.has_calibration_info] if self.has_calibration_info is not None else []
        self.has_calibration_info = [v if isinstance(v, str) else str(v) for v in self.has_calibration_info]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnzymeMeasurement(MeasurementProcess):
    """
    A single measurement/experimental run within an EnzymeML document, grouping time-course data for all observed
    species (EnzymeML Measurement).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["EnzymeMeasurement"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:EnzymeMeasurement"
    class_name: ClassVar[str] = "EnzymeMeasurement"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnzymeMeasurement

    id: Union[str, EnzymeMeasurementId] = None
    measurement_group_id: Optional[Union[str, list[str]]] = empty_list()
    has_measurement_species_data: Optional[Union[Union[dict, "EnzymeMeasurementSpeciesData"], list[Union[dict, "EnzymeMeasurementSpeciesData"]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, "PHValue"], list[Union[dict, "PHValue"]]]] = empty_list()
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnzymeMeasurementId):
            self.id = EnzymeMeasurementId(self.id)

        if not isinstance(self.measurement_group_id, list):
            self.measurement_group_id = [self.measurement_group_id] if self.measurement_group_id is not None else []
        self.measurement_group_id = [v if isinstance(v, str) else str(v) for v in self.measurement_group_id]

        if not isinstance(self.has_measurement_species_data, list):
            self.has_measurement_species_data = [self.has_measurement_species_data] if self.has_measurement_species_data is not None else []
        self.has_measurement_species_data = [v if isinstance(v, EnzymeMeasurementSpeciesData) else EnzymeMeasurementSpeciesData(**as_dict(v)) for v in self.has_measurement_species_data]

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvaluatedEntity(Entity):
    """
    An Entity that is being evaluated in a DataGeneratingActivity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "EvaluatedEntity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EvaluatedEntity

    id: Union[str, EvaluatedEntityId] = None
    was_generated_by: Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]] = empty_dict()
    title: Optional[str] = None
    description: Optional[str] = None
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvaluatedEntityId):
            self.id = EvaluatedEntityId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=Activity, key_name="id", keyed=True)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="other_identifier", slot_type=Identifier, key_name="notation", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalysisSourceData(EvaluatedEntity):
    """
    Information that was evaluated within a DataAnalysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "AnalysisSourceData"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.AnalysisSourceData

    id: Union[str, AnalysisSourceDataId] = None
    was_generated_by: Optional[Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalysisSourceDataId):
            self.id = AnalysisSourceDataId(self.id)

        self._normalize_inlined_as_list(slot_name="was_generated_by", slot_type=DataGeneratingActivity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


class Kind(YAMLRoot):
    """
    See [DCAT-AP specs:Kind](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Kind)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VCARD["Kind"]
    class_class_curie: ClassVar[str] = "vcard:Kind"
    class_name: ClassVar[str] = "Kind"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Kind


@dataclass(repr=False)
class Location(YAMLRoot):
    """
    See [DCAT-AP specs:Location](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Location)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Location"]
    class_class_curie: ClassVar[str] = "dcterms:Location"
    class_name: ClassVar[str] = "Location"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Location

    bbox: Optional[str] = None
    centroid: Optional[str] = None
    geometry: Optional[Union[dict, "Geometry"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.bbox is not None and not isinstance(self.bbox, str):
            self.bbox = str(self.bbox)

        if self.centroid is not None and not isinstance(self.centroid, str):
            self.centroid = str(self.centroid)

        if self.geometry is not None and not isinstance(self.geometry, Geometry):
            self.geometry = Geometry(**as_dict(self.geometry))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Plan(YAMLRoot):
    """
    A piece of information that specifies how an activity has to be carried out by its agents including what kind of
    steps have to be taken and what kind of parameters have to be met/set.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Plan"]
    class_class_curie: ClassVar[str] = "prov:Plan"
    class_name: ClassVar[str] = "Plan"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Plan

    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualitativeAttribute(YAMLRoot):
    """
    A piece of information that is attributed to an Entity, Activity or AgenticEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "QualitativeAttribute"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.QualitativeAttribute

    value: str = None
    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KineticEquation(QualitativeAttribute):
    """
    A mathematical equation used to model part of a BiocatalyticReaction's kinetics (EnzymeML Equation). The equation
    expression itself is stored in the inherited "value" slot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["KineticEquation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:KineticEquation"
    class_name: ClassVar[str] = "KineticEquation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.KineticEquation

    value: str = None
    equation_species_reference: Optional[Union[str, list[str]]] = empty_list()
    equation_type: Optional[Union[str, "KineticEquationTypeEnum"]] = None
    has_equation_variable: Optional[Union[Union[dict, "EquationVariable"], list[Union[dict, "EquationVariable"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.equation_species_reference, list):
            self.equation_species_reference = [self.equation_species_reference] if self.equation_species_reference is not None else []
        self.equation_species_reference = [v if isinstance(v, str) else str(v) for v in self.equation_species_reference]

        if self.equation_type is not None and not isinstance(self.equation_type, KineticEquationTypeEnum):
            self.equation_type = KineticEquationTypeEnum(self.equation_type)

        self._normalize_inlined_as_list(slot_name="has_equation_variable", slot_type=EquationVariable, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EquationVariable(QualitativeAttribute):
    """
    A symbolic variable used inside a KineticEquation's expression (EnzymeML Variable). The variable's symbol is
    stored in the inherited "value" slot, its human-readable name in the inherited "title" slot.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["EquationVariable"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:EquationVariable"
    class_name: ClassVar[str] = "EquationVariable"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EquationVariable

    value: str = None

@dataclass(repr=False)
class QuantitativeAttribute(YAMLRoot):
    """
    A quantifiable piece of information that is attributed to an Entity, Activity or AgenticEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "QuantitativeAttribute"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.QuantitativeAttribute

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[Union[str, DefinedTermId]] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.has_quantity_type):
            self.MissingRequiredField("has_quantity_type")
        if not isinstance(self.has_quantity_type, DefinedTermId):
            self.has_quantity_type = DefinedTermId(self.has_quantity_type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.unit is not None and not isinstance(self.unit, DefinedTermId):
            self.unit = DefinedTermId(self.unit)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Purity(QuantitativeAttribute):
    """
    A purity (datum) is a quality quantification facet that quantifies the purity of a portion of material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFR["0002371"]
    class_class_curie: ClassVar[str] = "AFR:0002371"
    class_name: ClassVar[str] = "Purity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Purity

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class SolubilityLimit(QuantitativeAttribute):
    """
    The maximum concentration of a component that can dissolve in a solution or gas phase under given conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["SolubilityLimit"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:SolubilityLimit"
    class_name: ClassVar[str] = "SolubilityLimit"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SolubilityLimit

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class IonicStrength(QuantitativeAttribute):
    """
    Ionic strength calculated from dissolved ions in the solvent, I = 0.5 * sum(ci * zi^2).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["IonicStrength"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:IonicStrength"
    class_name: ClassVar[str] = "IonicStrength"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.IonicStrength

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class FlowRate(QuantitativeAttribute):
    """
    Flow rate is a quality quantification facet that quantifies the motion of material through a surface per time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFR["0001881"]
    class_class_curie: ClassVar[str] = "AFR:0001881"
    class_name: ClassVar[str] = "FlowRate"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.FlowRate

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class ResidenceTime(QuantitativeAttribute):
    """
    Mean residence time (MRT) from the time of dosing to the time of the last measurable concentration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C85700"]
    class_class_curie: ClassVar[str] = "NCIT:C85700"
    class_name: ClassVar[str] = "ResidenceTime"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ResidenceTime

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class AngularVelocity(QuantitativeAttribute):
    """
    The speed or frequency at which a stirrer or shaker operates.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["AngularVelocity"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:AngularVelocity"
    class_name: ClassVar[str] = "AngularVelocity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.AngularVelocity

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class PowerPerVolume(QuantitativeAttribute):
    """
    The amount of mixing power or energy input per unit volume of the reaction mixture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["PowerPerVolume"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:PowerPerVolume"
    class_name: ClassVar[str] = "PowerPerVolume"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PowerPerVolume

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class QuenchingRatio(QuantitativeAttribute):
    """
    The ratio of the volume of quenching solution to the volume of the reaction mixture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["QuenchingRatio"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:QuenchingRatio"
    class_name: ClassVar[str] = "QuenchingRatio"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.QuenchingRatio

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class SamplingTimepoint(QuantitativeAttribute):
    """
    The time at which a sample was taken from the reaction vessel, expressed relative to the start of the reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["SamplingTimepoint"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:SamplingTimepoint"
    class_name: ClassVar[str] = "SamplingTimepoint"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SamplingTimepoint

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_time_value: Optional[Union[float, list[float]]] = empty_list()
    time_unit: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.has_time_value, list):
            self.has_time_value = [self.has_time_value] if self.has_time_value is not None else []
        self.has_time_value = [v if isinstance(v, float) else float(v) for v in self.has_time_value]

        if not isinstance(self.time_unit, list):
            self.time_unit = [self.time_unit] if self.time_unit is not None else []
        self.time_unit = [v if isinstance(v, str) else str(v) for v in self.time_unit]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemperatureTimepoint(QuantitativeAttribute):
    """
    A temperature value recorded at a specific time point during a temperature shift or profile.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["TemperatureTimepoint"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:TemperatureTimepoint"
    class_name: ClassVar[str] = "TemperatureTimepoint"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.TemperatureTimepoint

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_time_value: Optional[Union[float, list[float]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        if not isinstance(self.has_time_value, list):
            self.has_time_value = [self.has_time_value] if self.has_time_value is not None else []
        self.has_time_value = [v if isinstance(v, float) else float(v) for v in self.has_time_value]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MichaelisConstant(QuantitativeAttribute):
    """
    Michaelis-Menten constant - (The substrate concentration at which an enzyme achieves half of its maximum reaction
    rate (Km).)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SBO["0000027"]
    class_class_curie: ClassVar[str] = "SBO:0000027"
    class_name: ClassVar[str] = "MichaelisConstant"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MichaelisConstant

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class MaximumReactionRate(QuantitativeAttribute):
    """
    The maximum initial velocity or rate of a reaction. It is the limiting velocity as substrate concentrations get
    very large.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EDAM["data_0909"]
    class_class_curie: ClassVar[str] = "EDAM:data_0909"
    class_name: ClassVar[str] = "MaximumReactionRate"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MaximumReactionRate

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class TurnoverNumber(QuantitativeAttribute):
    """
    Turnover number representing the maximum number of substrate molecules converted to products per active site per
    unit time.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BAO["0000481"]
    class_class_curie: ClassVar[str] = "BAO:0000481"
    class_name: ClassVar[str] = "TurnoverNumber"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.TurnoverNumber

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class CatalyticEfficiency(QuantitativeAttribute):
    """
    Constant representing the actual efficiency of an enzyme, taking into account its microscopic catalytic activity
    and the rates of substrate binding and dissociation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SBO["0000302"]
    class_class_curie: ClassVar[str] = "SBO:0000302"
    class_name: ClassVar[str] = "CatalyticEfficiency"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.CatalyticEfficiency

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class DissociationConstant(QuantitativeAttribute):
    """
    Synonym: Kd - (The equilibrium dissociation constant (Kd) representing the balance between a complex and its
    dissociated components.)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SBO["0000282"]
    class_class_curie: ClassVar[str] = "SBO:0000282"
    class_name: ClassVar[str] = "DissociationConstant"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DissociationConstant

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class HillCoefficient(QuantitativeAttribute):
    """
    Empirical parameter created by Archibald Vivian Hill to describe the cooperative binding of oxygen on hemoglobine
    (Hill (1910). The possible effects of the aggregation of the molecules of haemoglobin on its dissociation curves.
    J Physiol 40: iv-vii).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SBO["0000190"]
    class_class_curie: ClassVar[str] = "SBO:0000190"
    class_name: ClassVar[str] = "HillCoefficient"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.HillCoefficient

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class InhibitionConstant(QuantitativeAttribute):
    """
    Synonym: Ki - (The inhibition constant (Ki) describing the affinity of an inhibitor for an enzyme. A lower Ki
    indicates stronger binding.)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SBO["0000261"]
    class_class_curie: ClassVar[str] = "SBO:0000261"
    class_name: ClassVar[str] = "InhibitionConstant"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.InhibitionConstant

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class HalfLife(QuantitativeAttribute):
    """
    A time unit which represents the period over which the activity or concentration of a specified chemical or
    element falls to half its original activity or concentration.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = UO["0000152"]
    class_class_curie: ClassVar[str] = "UO:0000152"
    class_name: ClassVar[str] = "HalfLife"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.HalfLife

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class SpaceTimeYield(QuantitativeAttribute):
    """
    A physical quantity that describes the amount of product produced per unit of time and unit of producing entity.
    The producing entity is for example the volume of a chemical reactor or in catalysis the mass or volume or moles
    of catalyst. Example unit: kg{product} / (hour * cubicmeter{catalyst})
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0005006"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0005006"
    class_name: ClassVar[str] = "SpaceTimeYield"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SpaceTimeYield

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class SubstrateConversion(QuantitativeAttribute):
    """
    A dimensionless physical quantity describing the fraction of a reactant that reacts in a chemical conversion. If a
    reactant is consumed completely its conversion is 1 (or 100 %).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0005004"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0005004"
    class_name: ClassVar[str] = "SubstrateConversion"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SubstrateConversion

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class SpecificActivity(QuantitativeAttribute):
    """
    A measure of enzyme activity under standard conditions, at a specific substrate concentration (usually
    saturation), expressed as the amount of product formed per unit time, per amount of enzyme. This is often
    expressed as micromol per min per mg, rather than the less practical official unit, Katal (1 mol per second).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SBO["0000558"]
    class_class_curie: ClassVar[str] = "SBO:0000558"
    class_name: ClassVar[str] = "SpecificActivity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SpecificActivity

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class InitialReactionRate(QuantitativeAttribute):
    """
    The rate at which product is formed in the first 10% of the enzymatic reaction under specific initial substrate
    concentrations and conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["InitialReactionRate"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:InitialReactionRate"
    class_name: ClassVar[str] = "InitialReactionRate"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.InitialReactionRate

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class EnantioselectivityRatio(QuantitativeAttribute):
    """
    The enantiomeric ratio (E) defining the enzyme's preference to catalyze the transformation of one enantiomer over
    its mirror image.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["EnantioselectivityRatio"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:EnantioselectivityRatio"
    class_name: ClassVar[str] = "EnantioselectivityRatio"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnantioselectivityRatio

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class EnantiomericExcess(QuantitativeAttribute):
    """
    The absolute value of the mole fraction for one enantiomer in a mixture minus the mole fraction for the other
    enantiomer. [CHMO]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFQ["0000220"]
    class_class_curie: ClassVar[str] = "AFQ:0000220"
    class_name: ClassVar[str] = "EnantiomericExcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnantiomericExcess

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class DiastereomericExcess(QuantitativeAttribute):
    """
    The absolute value of the mole fraction for one diastereomer in a mixture minus the mole fraction for the other.
    [CHMO]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFQ["0000217"]
    class_class_curie: ClassVar[str] = "AFQ:0000217"
    class_name: ClassVar[str] = "DiastereomericExcess"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DiastereomericExcess

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class IsomericContent(QuantitativeAttribute):
    """
    The isomeric content expressed as a percentage of a specific isomer relative to total product.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["IsomericContent"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:IsomericContent"
    class_name: ClassVar[str] = "IsomericContent"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.IsomericContent

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class GibbsFreeEnergyChange(QuantitativeAttribute):
    """
    A measure of the spontaneity of a chemical reaction. It is the change in the free energy of a system during a
    chemical reaction at a pH of 7.0. It is equal to the change in the enthalpy of the system minus the change in the
    product of the temperature times the entropy of the system. The resulting sign of Delta G determines if a reaction
    is spontaneous or not: DG < 0 indicates that the reaction is spontaneous; DG > 0 indicates that the reaction is
    not spontaneous; and DG = 0 indicates that the reaction is at equilibrium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C52567"]
    class_class_curie: ClassVar[str] = "NCIT:C52567"
    class_name: ClassVar[str] = "GibbsFreeEnergyChange"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.GibbsFreeEnergyChange

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class EnthalpyChange(QuantitativeAttribute):
    """
    Change in enthalpy observed in the constituents of a thermodynamic system when undergoing a transformation or
    chemical reaction. This is the preferred way of expressing the energy changes to a system at constant pressure,
    since enthalpy itself cannot be directly measured. The enthalpy change is positive in endothermic reactions,
    negative in exothermic reactions, and is defined as the difference between the final and initial enthalpy of the
    system under study: delta_H = Hf - Hi. The standard unit of measure is J.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SBO["0000573"]
    class_class_curie: ClassVar[str] = "SBO:0000573"
    class_name: ClassVar[str] = "EnthalpyChange"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnthalpyChange

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class StorageConditions(QuantitativeAttribute):
    """
    The conditions under which a biocatalyst preparation or reaction component is stored, including temperature, start
    date, and additives. Modelled as a QuantitativeAttribute cluster rather than Entity since it describes measurable
    environmental conditions of a material entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["StorageConditions"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:StorageConditions"
    class_name: ClassVar[str] = "StorageConditions"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.StorageConditions

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    storage_start: Optional[Union[str, XSDDate]] = None
    has_storage_additive: Optional[Union[dict[Union[str, StorageAdditiveId], Union[dict, "StorageAdditive"]], list[Union[dict, "StorageAdditive"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        if self.storage_start is not None and not isinstance(self.storage_start, XSDDate):
            self.storage_start = XSDDate(self.storage_start)

        self._normalize_inlined_as_list(slot_name="has_storage_additive", slot_type=StorageAdditive, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KineticParameters(QuantitativeAttribute):
    """
    A wrapper class grouping kinetic parameters determined for a biocatalytic reaction. Km and kcat values must be
    determined by varying all substrate concentrations to obtain true (non-apparent) values.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["000144"]
    class_class_curie: ClassVar[str] = "SIO:000144"
    class_name: ClassVar[str] = "KineticParameters"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.KineticParameters

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_michaelis_constant: Optional[Union[Union[dict, MichaelisConstant], list[Union[dict, MichaelisConstant]]]] = empty_list()
    has_maximum_reaction_rate: Optional[Union[Union[dict, MaximumReactionRate], list[Union[dict, MaximumReactionRate]]]] = empty_list()
    has_turnover_number: Optional[Union[Union[dict, TurnoverNumber], list[Union[dict, TurnoverNumber]]]] = empty_list()
    has_catalytic_efficiency: Optional[Union[Union[dict, CatalyticEfficiency], list[Union[dict, CatalyticEfficiency]]]] = empty_list()
    has_dissociation_constant: Optional[Union[Union[dict, DissociationConstant], list[Union[dict, DissociationConstant]]]] = empty_list()
    has_hill_coefficient: Optional[Union[Union[dict, HillCoefficient], list[Union[dict, HillCoefficient]]]] = empty_list()
    has_inhibition_characterisation: Optional[Union[Union[dict, "EnzymeInhibitionCharacterisation"], list[Union[dict, "EnzymeInhibitionCharacterisation"]]]] = empty_list()
    has_enzyme_stability: Optional[Union[Union[dict, "EnzymeStabilityCharacterisation"], list[Union[dict, "EnzymeStabilityCharacterisation"]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_michaelis_constant", slot_type=MichaelisConstant, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_maximum_reaction_rate", slot_type=MaximumReactionRate, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_turnover_number", slot_type=TurnoverNumber, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_catalytic_efficiency", slot_type=CatalyticEfficiency, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_dissociation_constant", slot_type=DissociationConstant, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_hill_coefficient", slot_type=HillCoefficient, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_inhibition_characterisation", slot_type=EnzymeInhibitionCharacterisation, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_enzyme_stability", slot_type=EnzymeStabilityCharacterisation, key_name="value", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnzymeInhibitionCharacterisation(QuantitativeAttribute):
    """
    A paired description of enzyme inhibition type and inhibition constant (Ki). The two fields are semantically
    coupled and should always appear together.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["EnzymeInhibitionCharacterisation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:EnzymeInhibitionCharacterisation"
    class_name: ClassVar[str] = "EnzymeInhibitionCharacterisation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnzymeInhibitionCharacterisation

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    inhibition_type: Optional[Union[str, "InhibitionTypeEnum"]] = None
    has_inhibition_constant: Optional[Union[Union[dict, InhibitionConstant], list[Union[dict, InhibitionConstant]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.inhibition_type is not None and not isinstance(self.inhibition_type, InhibitionTypeEnum):
            self.inhibition_type = InhibitionTypeEnum(self.inhibition_type)

        self._normalize_inlined_as_list(slot_name="has_inhibition_constant", slot_type=InhibitionConstant, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnzymeStabilityCharacterisation(QuantitativeAttribute):
    """
    A characterisation of biocatalyst stability, including half-life and qualitative description of activity decline
    or preservation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["EnzymeStabilityCharacterisation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:EnzymeStabilityCharacterisation"
    class_name: ClassVar[str] = "EnzymeStabilityCharacterisation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnzymeStabilityCharacterisation

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_half_life: Optional[Union[Union[dict, HalfLife], list[Union[dict, HalfLife]]]] = empty_list()
    stability_description: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_half_life", slot_type=HalfLife, key_name="value", keyed=False)

        if not isinstance(self.stability_description, list):
            self.stability_description = [self.stability_description] if self.stability_description is not None else []
        self.stability_description = [v if isinstance(v, str) else str(v) for v in self.stability_description]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class YieldAndConversion(QuantitativeAttribute):
    """
    A wrapper class grouping yield and conversion metrics for a biocatalytic reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["YieldAndConversion"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:YieldAndConversion"
    class_name: ClassVar[str] = "YieldAndConversion"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.YieldAndConversion

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_yield: Optional[Union[Union[dict, "Yield"], list[Union[dict, "Yield"]]]] = empty_list()
    has_space_time_yield: Optional[Union[Union[dict, SpaceTimeYield], list[Union[dict, SpaceTimeYield]]]] = empty_list()
    has_substrate_conversion: Optional[Union[Union[dict, SubstrateConversion], list[Union[dict, SubstrateConversion]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_yield", slot_type=Yield, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_space_time_yield", slot_type=SpaceTimeYield, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_substrate_conversion", slot_type=SubstrateConversion, key_name="value", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ActivityAndInitialReactionRate(QuantitativeAttribute):
    """
    A wrapper class grouping activity and initial reaction rate measurements for a biocatalytic reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["ActivityAndInitialReactionRate"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:ActivityAndInitialReactionRate"
    class_name: ClassVar[str] = "ActivityAndInitialReactionRate"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ActivityAndInitialReactionRate

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_specific_activity: Optional[Union[Union[dict, SpecificActivity], list[Union[dict, SpecificActivity]]]] = empty_list()
    has_initial_reaction_rate: Optional[Union[Union[dict, InitialReactionRate], list[Union[dict, InitialReactionRate]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_specific_activity", slot_type=SpecificActivity, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_initial_reaction_rate", slot_type=InitialReactionRate, key_name="value", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SelectivityAndSpecificity(QuantitativeAttribute):
    """
    A wrapper class grouping selectivity and specificity parameters for a biocatalytic reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["SelectivityAndSpecificity"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:SelectivityAndSpecificity"
    class_name: ClassVar[str] = "SelectivityAndSpecificity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SelectivityAndSpecificity

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_enantioselectivity_ratio: Optional[Union[Union[dict, EnantioselectivityRatio], list[Union[dict, EnantioselectivityRatio]]]] = empty_list()
    has_enantiomeric_excess: Optional[Union[Union[dict, EnantiomericExcess], list[Union[dict, EnantiomericExcess]]]] = empty_list()
    has_diastereomeric_excess: Optional[Union[Union[dict, DiastereomericExcess], list[Union[dict, DiastereomericExcess]]]] = empty_list()
    has_isomeric_content: Optional[Union[Union[dict, IsomericContent], list[Union[dict, IsomericContent]]]] = empty_list()
    stereoselectivity_description: Optional[Union[str, list[str]]] = empty_list()
    chemoselectivity_description: Optional[Union[str, list[str]]] = empty_list()
    regioselectivity_description: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_enantioselectivity_ratio", slot_type=EnantioselectivityRatio, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_enantiomeric_excess", slot_type=EnantiomericExcess, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_diastereomeric_excess", slot_type=DiastereomericExcess, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_isomeric_content", slot_type=IsomericContent, key_name="value", keyed=False)

        if not isinstance(self.stereoselectivity_description, list):
            self.stereoselectivity_description = [self.stereoselectivity_description] if self.stereoselectivity_description is not None else []
        self.stereoselectivity_description = [v if isinstance(v, str) else str(v) for v in self.stereoselectivity_description]

        if not isinstance(self.chemoselectivity_description, list):
            self.chemoselectivity_description = [self.chemoselectivity_description] if self.chemoselectivity_description is not None else []
        self.chemoselectivity_description = [v if isinstance(v, str) else str(v) for v in self.chemoselectivity_description]

        if not isinstance(self.regioselectivity_description, list):
            self.regioselectivity_description = [self.regioselectivity_description] if self.regioselectivity_description is not None else []
        self.regioselectivity_description = [v if isinstance(v, str) else str(v) for v in self.regioselectivity_description]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThermodynamicParameters(QuantitativeAttribute):
    """
    A wrapper class grouping thermodynamic parameters for a biocatalytic reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["000144"]
    class_class_curie: ClassVar[str] = "SIO:000144"
    class_name: ClassVar[str] = "ThermodynamicParameters"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ThermodynamicParameters

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_gibbs_free_energy_change: Optional[Union[Union[dict, GibbsFreeEnergyChange], list[Union[dict, GibbsFreeEnergyChange]]]] = empty_list()
    has_enthalpy_change: Optional[Union[Union[dict, EnthalpyChange], list[Union[dict, EnthalpyChange]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_gibbs_free_energy_change", slot_type=GibbsFreeEnergyChange, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_enthalpy_change", slot_type=EnthalpyChange, key_name="value", keyed=False)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KineticModelParameter(QuantitativeAttribute):
    """
    An estimated or fixed parameter of a kinetic model, such as a rate or binding constant (EnzymeML Parameter).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["KineticModelParameter"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:KineticModelParameter"
    class_name: ClassVar[str] = "KineticModelParameter"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.KineticModelParameter

    has_quantity_type: Union[str, DefinedTermId] = None
    parameter_symbol: Optional[Union[str, list[str]]] = empty_list()
    initial_value: Optional[float] = None
    upper_bound: Optional[float] = None
    lower_bound: Optional[float] = None
    stderr: Optional[float] = None
    is_fitted: Optional[Union[bool, Bool]] = None
    is_fixed_parameter: Optional[Union[bool, Bool]] = None
    value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.parameter_symbol, list):
            self.parameter_symbol = [self.parameter_symbol] if self.parameter_symbol is not None else []
        self.parameter_symbol = [v if isinstance(v, str) else str(v) for v in self.parameter_symbol]

        if self.initial_value is not None and not isinstance(self.initial_value, float):
            self.initial_value = float(self.initial_value)

        if self.upper_bound is not None and not isinstance(self.upper_bound, float):
            self.upper_bound = float(self.upper_bound)

        if self.lower_bound is not None and not isinstance(self.lower_bound, float):
            self.lower_bound = float(self.lower_bound)

        if self.stderr is not None and not isinstance(self.stderr, float):
            self.stderr = float(self.stderr)

        if self.is_fitted is not None and not isinstance(self.is_fitted, Bool):
            self.is_fitted = Bool(self.is_fitted)

        if self.is_fixed_parameter is not None and not isinstance(self.is_fixed_parameter, Bool):
            self.is_fixed_parameter = Bool(self.is_fixed_parameter)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnzymeMeasurementSpeciesData(QuantitativeAttribute):
    """
    Time-course measurement data for a single species within an EnzymeMeasurement (EnzymeML MeasurementData). "value"
    (inherited) is not used directly here -- see has_timepoint for the actual series.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["EnzymeMeasurementSpeciesData"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:EnzymeMeasurementSpeciesData"
    class_name: ClassVar[str] = "EnzymeMeasurementSpeciesData"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.EnzymeMeasurementSpeciesData

    has_quantity_type: Union[str, DefinedTermId] = None
    measured_species_reference: Optional[Union[str, list[str]]] = empty_list()
    prepared_amount: Optional[float] = None
    initial_amount: Optional[float] = None
    measurement_data_type: Optional[Union[str, "MeasurementDataTypeEnum"]] = None
    is_simulated: Optional[Union[bool, Bool]] = None
    has_timepoint: Optional[Union[Union[dict, "MeasurementTimepoint"], list[Union[dict, "MeasurementTimepoint"]]]] = empty_list()
    value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.measured_species_reference, list):
            self.measured_species_reference = [self.measured_species_reference] if self.measured_species_reference is not None else []
        self.measured_species_reference = [v if isinstance(v, str) else str(v) for v in self.measured_species_reference]

        if self.prepared_amount is not None and not isinstance(self.prepared_amount, float):
            self.prepared_amount = float(self.prepared_amount)

        if self.initial_amount is not None and not isinstance(self.initial_amount, float):
            self.initial_amount = float(self.initial_amount)

        if self.measurement_data_type is not None and not isinstance(self.measurement_data_type, MeasurementDataTypeEnum):
            self.measurement_data_type = MeasurementDataTypeEnum(self.measurement_data_type)

        if self.is_simulated is not None and not isinstance(self.is_simulated, Bool):
            self.is_simulated = Bool(self.is_simulated)

        self._normalize_inlined_as_list(slot_name="has_timepoint", slot_type=MeasurementTimepoint, key_name="value", keyed=False)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasurementTimepoint(QuantitativeAttribute):
    """
    A single (time, value) pair within a time-course measurement, generalising the existing TemperatureTimepoint
    pattern.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["MeasurementTimepoint"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:MeasurementTimepoint"
    class_name: ClassVar[str] = "MeasurementTimepoint"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MeasurementTimepoint

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None
    has_time_value: Optional[Union[float, list[float]]] = empty_list()
    time_unit: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.has_time_value, list):
            self.has_time_value = [self.has_time_value] if self.has_time_value is not None else []
        self.has_time_value = [v if isinstance(v, float) else float(v) for v in self.has_time_value]

        if not isinstance(self.time_unit, list):
            self.time_unit = [self.time_unit] if self.time_unit is not None else []
        self.time_unit = [v if isinstance(v, str) else str(v) for v in self.time_unit]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Relationship(YAMLRoot):
    """
    See [DCAT-AP specs:Relationship](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Relationship)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Relationship"]
    class_class_curie: ClassVar[str] = "dcat:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Relationship

    had_role: Union[Union[dict, "Role"], list[Union[dict, "Role"]]] = None
    relation: Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.had_role):
            self.MissingRequiredField("had_role")
        if not isinstance(self.had_role, list):
            self.had_role = [self.had_role] if self.had_role is not None else []
        self.had_role = [v if isinstance(v, Role) else Role(**as_dict(v)) for v in self.had_role]

        if self._is_empty(self.relation):
            self.MissingRequiredField("relation")
        self._normalize_inlined_as_list(slot_name="relation", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Software(AgenticEntity):
    """
    An instrument composed of a series of instructions that can be interpreted by or directly executed by a computer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["SoftwareAgent"]
    class_class_curie: ClassVar[str] = "prov:SoftwareAgent"
    class_name: ClassVar[str] = "Software"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Software

    id: Union[str, SoftwareId] = None
    has_part: Optional[Union[dict[Union[str, SoftwareId], Union[dict, "Software"]], list[Union[dict, "Software"]]]] = empty_dict()
    other_identifier: Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoftwareId):
            self.id = SoftwareId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Software, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="other_identifier", slot_type=Identifier, key_name="notation", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SupportiveEntity(YAMLRoot):
    """
    The supportive entities are supporting the main entities in the Application Profile. They are included in the
    Application Profile because they form the range of properties.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCATAPPLUS["SupportiveEntity"]
    class_class_curie: ClassVar[str] = "dcatapplus:SupportiveEntity"
    class_name: ClassVar[str] = "SupportiveEntity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SupportiveEntity

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attribution(SupportiveEntity):
    """
    See [DCAT-AP specs:Attribution](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Attribution)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Attribution"]
    class_class_curie: ClassVar[str] = "prov:Attribution"
    class_name: ClassVar[str] = "Attribution"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Attribution

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChecksumAlgorithm(SupportiveEntity):
    """
    See [DCAT-AP specs:ChecksumAlgorithm](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ChecksumAlgorithm)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SPDX["ChecksumAlgorithm"]
    class_class_curie: ClassVar[str] = "spdx:ChecksumAlgorithm"
    class_name: ClassVar[str] = "ChecksumAlgorithm"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ChecksumAlgorithm

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concept(SupportiveEntity):
    """
    See [DCAT-AP specs:Concept](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Concept)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["Concept"]
    class_class_curie: ClassVar[str] = "skos:Concept"
    class_name: ClassVar[str] = "Concept"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Concept

    preferred_label: Union[str, list[str]] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.preferred_label):
            self.MissingRequiredField("preferred_label")
        if not isinstance(self.preferred_label, list):
            self.preferred_label = [self.preferred_label] if self.preferred_label is not None else []
        self.preferred_label = [v if isinstance(v, str) else str(v) for v in self.preferred_label]

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConceptScheme(SupportiveEntity):
    """
    See [DCAT-AP specs:ConceptScheme](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ConceptScheme)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS["ConceptScheme"]
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "ConceptScheme"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ConceptScheme

    title: Union[str, list[str]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, list):
            self.title = [self.title] if self.title is not None else []
        self.title = [v if isinstance(v, str) else str(v) for v in self.title]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Document(SupportiveEntity):
    """
    See [DCAT-AP specs:Document](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Document)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF["Document"]
    class_class_curie: ClassVar[str] = "foaf:Document"
    class_name: ClassVar[str] = "Document"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Document

    id: Union[str, DocumentId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DocumentId):
            self.id = DocumentId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Frequency(SupportiveEntity):
    """
    See [DCAT-AP specs:Frequency](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Frequency)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Frequency"]
    class_class_curie: ClassVar[str] = "dcterms:Frequency"
    class_name: ClassVar[str] = "Frequency"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Frequency

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Geometry(SupportiveEntity):
    """
    See [DCAT-AP specs:Geometry](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Geometry)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LOCN["Geometry"]
    class_class_curie: ClassVar[str] = "locn:Geometry"
    class_name: ClassVar[str] = "Geometry"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Geometry

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Identifier(SupportiveEntity):
    """
    See [DCAT-AP specs:Identifier](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Identifier)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ADMS["Identifier"]
    class_class_curie: ClassVar[str] = "adms:Identifier"
    class_name: ClassVar[str] = "Identifier"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Identifier

    notation: str = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.notation):
            self.MissingRequiredField("notation")
        if not isinstance(self.notation, str):
            self.notation = str(self.notation)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LegalResource(SupportiveEntity):
    """
    See [DCAT-AP specs:LegalResource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LegalResource)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ELI["LegalResource"]
    class_class_curie: ClassVar[str] = "eli:LegalResource"
    class_name: ClassVar[str] = "LegalResource"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.LegalResource

    id: Union[str, LegalResourceId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LegalResourceId):
            self.id = LegalResourceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LicenseDocument(SupportiveEntity):
    """
    See [DCAT-AP specs:LicenseDocument](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LicenseDocument)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["LicenseDocument"]
    class_class_curie: ClassVar[str] = "dcterms:LicenseDocument"
    class_name: ClassVar[str] = "LicenseDocument"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.LicenseDocument

    id: Union[str, LicenseDocumentId] = None
    type: Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]] = empty_list()
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LicenseDocumentId):
            self.id = LicenseDocumentId(self.id)

        self._normalize_inlined_as_list(slot_name="type", slot_type=Concept, key_name="preferred_label", keyed=False)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LinguisticSystem(SupportiveEntity):
    """
    See [DCAT-AP specs:LinguisticSystem](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#LinguisticSystem)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["LinguisticSystem"]
    class_class_curie: ClassVar[str] = "dcterms:LinguisticSystem"
    class_name: ClassVar[str] = "LinguisticSystem"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.LinguisticSystem

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaType(SupportiveEntity):
    """
    See [DCAT-AP specs:MediaType](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaType)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["MediaType"]
    class_class_curie: ClassVar[str] = "dcterms:MediaType"
    class_name: ClassVar[str] = "MediaType"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MediaType

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MediaTypeOrExtent(SupportiveEntity):
    """
    See [DCAT-AP specs:MediaTypeOrExtent](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#MediaTypeOrExtent)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["MediaTypeOrExtent"]
    class_class_curie: ClassVar[str] = "dcterms:MediaTypeOrExtent"
    class_name: ClassVar[str] = "MediaTypeOrExtent"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MediaTypeOrExtent

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PeriodOfTime(SupportiveEntity):
    """
    See [DCAT-AP specs:PeriodOfTime](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#PeriodOfTime)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["PeriodOfTime"]
    class_class_curie: ClassVar[str] = "dcterms:PeriodOfTime"
    class_name: ClassVar[str] = "PeriodOfTime"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PeriodOfTime

    beginning: Optional[Union[dict, "TimeInstant"]] = None
    end: Optional[Union[dict, "TimeInstant"]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    start_date: Optional[Union[str, XSDDate]] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.beginning is not None and not isinstance(self.beginning, TimeInstant):
            self.beginning = TimeInstant(**as_dict(self.beginning))

        if self.end is not None and not isinstance(self.end, TimeInstant):
            self.end = TimeInstant(**as_dict(self.end))

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Policy(SupportiveEntity):
    """
    See [DCAT-AP specs:Policy](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Policy)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ODRL["Policy"]
    class_class_curie: ClassVar[str] = "odrl:Policy"
    class_name: ClassVar[str] = "Policy"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Policy

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProvenanceStatement(SupportiveEntity):
    """
    See [DCAT-AP specs:ProvenanceStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#ProvenanceStatement)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["ProvenanceStatement"]
    class_class_curie: ClassVar[str] = "dcterms:ProvenanceStatement"
    class_name: ClassVar[str] = "ProvenanceStatement"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ProvenanceStatement

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Resource(SupportiveEntity):
    """
    See [DCAT-AP specs:Resource](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Resource)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = RDFS["Resource"]
    class_class_curie: ClassVar[str] = "rdfs:Resource"
    class_name: ClassVar[str] = "Resource"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Resource

    id: Union[str, ResourceId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResourceId):
            self.id = ResourceId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RightsStatement(SupportiveEntity):
    """
    See [DCAT-AP specs:RightsStatement](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#RightsStatement)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["RightsStatement"]
    class_class_curie: ClassVar[str] = "dcterms:RightsStatement"
    class_name: ClassVar[str] = "RightsStatement"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.RightsStatement

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Role(SupportiveEntity):
    """
    See [DCAT-AP specs:Role](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Role)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Role"]
    class_class_curie: ClassVar[str] = "dcat:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Role

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Standard(SupportiveEntity):
    """
    See [DCAT-AP specs:Standard](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#Standard)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = DCTERMS["Standard"]
    class_class_curie: ClassVar[str] = "dcterms:Standard"
    class_name: ClassVar[str] = "Standard"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Standard

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Surrounding(YAMLRoot):
    """
    The surrounding in which the dataset creating activity took place (e.g. a lab).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Location"]
    class_class_curie: ClassVar[str] = "prov:Location"
    class_name: ClassVar[str] = "Surrounding"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Surrounding

    title: Optional[str] = None
    description: Optional[str] = None
    type: Optional[Union[dict, DefinedTerm]] = None
    rdf_type: Optional[Union[dict, DefinedTerm]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.type is not None and not isinstance(self.type, DefinedTerm):
            self.type = DefinedTerm(**as_dict(self.type))

        if self.rdf_type is not None and not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


class Laboratory(Surrounding):
    """
    A facility that provides controlled conditions in which scientific or technological research, experiments, and
    measurement may be performed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = ENVO["01001405"]
    class_class_curie: ClassVar[str] = "ENVO:01001405"
    class_name: ClassVar[str] = "Laboratory"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Laboratory


@dataclass(repr=False)
class TimeInstant(SupportiveEntity):
    """
    See [DCAT-AP specs:TimeInstant](https://semiceu.github.io/DCAT-AP/releases/3.0.0/#TimeInstant)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = TIME["Instant"]
    class_class_curie: ClassVar[str] = "time:Instant"
    class_name: ClassVar[str] = "TimeInstant"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.TimeInstant

    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalEntity(Entity):
    """
    Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex,
    conformer etc., identifiable as a separately distinguishable entity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["23367"]
    class_class_curie: ClassVar[str] = "CHEBI:23367"
    class_name: ClassVar[str] = "ChemicalEntity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ChemicalEntity

    id: Union[str, ChemicalEntityId] = None
    inchi: Optional[Union[Union[dict, "InChi"], list[Union[dict, "InChi"]]]] = empty_list()
    inchikey: Optional[Union[Union[dict, "InChIKey"], list[Union[dict, "InChIKey"]]]] = empty_list()
    smiles: Optional[Union[Union[dict, "SMILES"], list[Union[dict, "SMILES"]]]] = empty_list()
    molecular_formula: Optional[Union[Union[dict, "MolecularFormula"], list[Union[dict, "MolecularFormula"]]]] = empty_list()
    iupac_name: Optional[Union[Union[dict, "IUPACName"], list[Union[dict, "IUPACName"]]]] = empty_list()
    has_molar_mass: Optional[Union[Union[dict, "MolarMass"], list[Union[dict, "MolarMass"]]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], list[Union[dict, "ChemicalEntity"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalEntityId):
            self.id = ChemicalEntityId(self.id)

        self._normalize_inlined_as_list(slot_name="inchi", slot_type=InChi, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="inchikey", slot_type=InChIKey, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="smiles", slot_type=SMILES, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="molecular_formula", slot_type=MolecularFormula, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="iupac_name", slot_type=IUPACName, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_molar_mass", slot_type=MolarMass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=ChemicalEntity, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageAdditive(ChemicalEntity):
    """
    A ChemicalSubstance added to a storage medium to preserve or stabilize a MaterialEntity during storage (e.g.
    antioxidants, stabilizers, drying agents, inert gases such as argon or nitrogen).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["StorageAdditive"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:StorageAdditive"
    class_name: ClassVar[str] = "StorageAdditive"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.StorageAdditive

    id: Union[str, StorageAdditiveId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StorageAdditiveId):
            self.id = StorageAdditiveId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiocatalyticComponent(ChemicalEntity):
    """
    A ChemicalSubstance present in the reaction mixture of a biocatalytic experiment, regardless of its functional
    role (substrate, cofactor, buffer, cosolvent, etc.). Role differentiation is optional per P-002.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["BiocatalyticComponent"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:BiocatalyticComponent"
    class_name: ClassVar[str] = "BiocatalyticComponent"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.BiocatalyticComponent

    id: Union[str, BiocatalyticComponentId] = None
    has_component_role: Optional[Union[str, "ComponentRoleEnum"]] = None
    has_concentration: Optional[Union[Union[dict, "Concentration"], list[Union[dict, "Concentration"]]]] = empty_list()
    has_solubility_limit: Optional[Union[Union[dict, SolubilityLimit], list[Union[dict, SolubilityLimit]]]] = empty_list()
    has_purity: Optional[Union[Union[dict, Purity], list[Union[dict, Purity]]]] = empty_list()
    supplied_by: Optional[Union[dict, Agent]] = None
    has_formulation: Optional[Union[str, list[str]]] = empty_list()
    has_storage_conditions: Optional[Union[dict, StorageConditions]] = None
    has_constant_concentration: Optional[Union[bool, Bool]] = None
    synonymous_names: Optional[Union[str, list[str]]] = empty_list()
    other_identifier: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiocatalyticComponentId):
            self.id = BiocatalyticComponentId(self.id)

        if self.has_component_role is not None and not isinstance(self.has_component_role, ComponentRoleEnum):
            self.has_component_role = ComponentRoleEnum(self.has_component_role)

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_solubility_limit", slot_type=SolubilityLimit, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_purity", slot_type=Purity, key_name="value", keyed=False)

        if self.supplied_by is not None and not isinstance(self.supplied_by, Agent):
            self.supplied_by = Agent(**as_dict(self.supplied_by))

        if not isinstance(self.has_formulation, list):
            self.has_formulation = [self.has_formulation] if self.has_formulation is not None else []
        self.has_formulation = [v if isinstance(v, str) else str(v) for v in self.has_formulation]

        if self.has_storage_conditions is not None and not isinstance(self.has_storage_conditions, StorageConditions):
            self.has_storage_conditions = StorageConditions(**as_dict(self.has_storage_conditions))

        if self.has_constant_concentration is not None and not isinstance(self.has_constant_concentration, Bool):
            self.has_constant_concentration = Bool(self.has_constant_concentration)

        if not isinstance(self.synonymous_names, list):
            self.synonymous_names = [self.synonymous_names] if self.synonymous_names is not None else []
        self.synonymous_names = [v if isinstance(v, str) else str(v) for v in self.synonymous_names]

        if self.other_identifier is not None and not isinstance(self.other_identifier, str):
            self.other_identifier = str(self.other_identifier)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularComplex(ChemicalEntity):
    """
    A grouping of two or more species (SmallMolecule/BiocatalyticComponent and/or Biocatalyst) into a single complex,
    e.g. an enzyme-substrate complex or a buffer/solvent mixture (EnzymeML Complex).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C19398"]
    class_class_curie: ClassVar[str] = "NCIT:C19398"
    class_name: ClassVar[str] = "MolecularComplex"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MolecularComplex

    id: Union[str, MolecularComplexId] = None
    has_constant_concentration: Optional[Union[bool, Bool]] = None
    has_complex_participant: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_part: Optional[Union[str, ChemicalEntityId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MolecularComplexId):
            self.id = MolecularComplexId(self.id)

        if self.has_constant_concentration is not None and not isinstance(self.has_constant_concentration, Bool):
            self.has_constant_concentration = Bool(self.has_constant_concentration)

        self._normalize_inlined_as_list(slot_name="has_complex_participant", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if self.has_part is not None and not isinstance(self.has_part, ChemicalEntityId):
            self.has_part = ChemicalEntityId(self.has_part)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Atom(Entity):
    """
    An Entity constituting the smallest component of a chemical element having the chemical properties of the element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["33250"]
    class_class_curie: ClassVar[str] = "CHEBI:33250"
    class_name: ClassVar[str] = "Atom"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Atom

    id: Union[str, AtomId] = None
    rdf_type: Union[dict, DefinedTerm] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AtomId):
            self.id = AtomId(self.id)

        if self._is_empty(self.rdf_type):
            self.MissingRequiredField("rdf_type")
        if not isinstance(self.rdf_type, DefinedTerm):
            self.rdf_type = DefinedTerm(**as_dict(self.rdf_type))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Concentration(QuantitativeAttribute):
    """
    A QuantitativeAttribute of a ChemicalSubstance that represents the amount of a constituent divided by the volume
    of the mixture.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002820"]
    class_class_curie: ClassVar[str] = "CHMO:0002820"
    class_name: ClassVar[str] = "Concentration"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Concentration

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class AmountOfSubstance(QuantitativeAttribute):
    """
    The total amount of substance used in a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "AmountOfSubstance"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.AmountOfSubstance

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class PHValue(QuantitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001089"]
    class_class_curie: ClassVar[str] = "SIO:001089"
    class_name: ClassVar[str] = "PHValue"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PHValue

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class InChIKey(QualitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000059"]
    class_class_curie: ClassVar[str] = "CHEMINF:000059"
    class_name: ClassVar[str] = "InChIKey"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.InChIKey

    value: str = None

@dataclass(repr=False)
class InChi(QualitativeAttribute):
    """
    A structure descriptor which conforms to the InChI format specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000113"]
    class_class_curie: ClassVar[str] = "CHEMINF:000113"
    class_name: ClassVar[str] = "InChi"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.InChi

    value: str = None

@dataclass(repr=False)
class MolecularFormula(QualitativeAttribute):
    """
    A structure descriptor which identifies each constituent element by its chemical symbol and indicates the number
    of atoms of each element found in each discrete molecule of that compound.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000042"]
    class_class_curie: ClassVar[str] = "CHEMINF:000042"
    class_name: ClassVar[str] = "MolecularFormula"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MolecularFormula

    value: str = None

@dataclass(repr=False)
class IUPACName(QualitativeAttribute):
    """
    A systematic name which is formulated according to the rules and recommendations for chemical nomenclature set out
    by the International Union of Pure and Applied Chemistry (IUPAC).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000107"]
    class_class_curie: ClassVar[str] = "CHEMINF:000107"
    class_name: ClassVar[str] = "IUPACName"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.IUPACName

    value: str = None

@dataclass(repr=False)
class SMILES(QualitativeAttribute):
    """
    A structure descriptor that denotes a molecular structure as a graph and conforms to the SMILES format
    specification.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMINF["000018"]
    class_class_curie: ClassVar[str] = "CHEMINF:000018"
    class_name: ClassVar[str] = "SMILES"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SMILES

    value: str = None

@dataclass(repr=False)
class ChemicalReaction(EvaluatedActivity):
    """
    A process that leads to the transformation of one set of chemical substances to another and that is the subject
    matter of a DataGeneratingActivity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010345"]
    class_class_curie: ClassVar[str] = "SIO:010345"
    class_name: ClassVar[str] = "ChemicalReaction"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ChemicalReaction

    id: Union[str, ChemicalReactionId] = None
    used_starting_material: Optional[Union[dict[Union[str, StartingMaterialId], Union[dict, "StartingMaterial"]], list[Union[dict, "StartingMaterial"]]]] = empty_dict()
    used_reactant: Optional[Union[dict[Union[str, ReagentId], Union[dict, "Reagent"]], list[Union[dict, "Reagent"]]]] = empty_dict()
    generated_product: Optional[Union[dict[Union[str, ChemicalProductId], Union[dict, "ChemicalProduct"]], list[Union[dict, "ChemicalProduct"]]]] = empty_dict()
    used_catalyst: Optional[Union[dict[Union[str, CatalystId], Union[dict, "Catalyst"]], list[Union[dict, "Catalyst"]]]] = empty_dict()
    used_solvent: Optional[Union[dict[Union[str, DissolvingSubstanceId], Union[dict, "DissolvingSubstance"]], list[Union[dict, "DissolvingSubstance"]]]] = empty_dict()
    has_duration: Optional[str] = None
    used_reactor: Optional[Union[dict[Union[str, ReactorId], Union[dict, "Reactor"]], list[Union[dict, "Reactor"]]]] = empty_dict()
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_yield: Optional[Union[Union[dict, "Yield"], list[Union[dict, "Yield"]]]] = empty_list()
    has_reaction_step: Optional[Union[dict[Union[str, ChemicalReactionId], Union[dict, "ChemicalReaction"]], list[Union[dict, "ChemicalReaction"]]]] = empty_dict()
    related_resource: Optional[Union[dict[Union[str, ResourceId], Union[dict, Resource]], list[Union[dict, Resource]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalReactionId):
            self.id = ChemicalReactionId(self.id)

        self._normalize_inlined_as_list(slot_name="used_starting_material", slot_type=StartingMaterial, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_reactant", slot_type=Reagent, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="generated_product", slot_type=ChemicalProduct, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_catalyst", slot_type=Catalyst, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="used_solvent", slot_type=DissolvingSubstance, key_name="id", keyed=True)

        if self.has_duration is not None and not isinstance(self.has_duration, str):
            self.has_duration = str(self.has_duration)

        self._normalize_inlined_as_list(slot_name="used_reactor", slot_type=Reactor, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_yield", slot_type=Yield, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_reaction_step", slot_type=ChemicalReaction, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="related_resource", slot_type=Resource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiocatalyticReaction(ChemicalReaction):
    """
    A ChemicalReaction that is catalyzed by a Biocatalyst (enzyme or whole cell). Evaluated by a
    BiocatalyticExperiment. Carries reaction conditions, phase system, and result attributes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010345"]
    class_class_curie: ClassVar[str] = "SIO:010345"
    class_name: ClassVar[str] = "BiocatalyticReaction"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.BiocatalyticReaction

    id: Union[str, BiocatalyticReactionId] = None
    has_reaction_medium: Optional[Union[dict, "ReactionMedium"]] = None
    has_temperature_shift: Optional[Union[dict[Union[str, TemperatureShiftProcessId], Union[dict, TemperatureShiftProcess]], list[Union[dict, TemperatureShiftProcess]]]] = empty_dict()
    has_temperature_gradient: Optional[Union[dict, TemperatureGradient]] = None
    has_ph_shift: Optional[Union[dict[Union[str, PHShiftProcessId], Union[dict, PHShiftProcess]], list[Union[dict, PHShiftProcess]]]] = empty_dict()
    has_ph_gradient: Optional[Union[dict, PHGradient]] = None
    has_ph_measurement: Optional[Union[dict, PHMeasurementProcess]] = None
    has_kinetic_parameters: Optional[Union[Union[dict, KineticParameters], list[Union[dict, KineticParameters]]]] = empty_list()
    has_yield_and_conversion: Optional[Union[Union[dict, YieldAndConversion], list[Union[dict, YieldAndConversion]]]] = empty_list()
    has_activity_and_reaction_rate: Optional[Union[Union[dict, ActivityAndInitialReactionRate], list[Union[dict, ActivityAndInitialReactionRate]]]] = empty_list()
    has_selectivity_and_specificity: Optional[Union[Union[dict, SelectivityAndSpecificity], list[Union[dict, SelectivityAndSpecificity]]]] = empty_list()
    has_thermodynamic_parameters: Optional[Union[Union[dict, ThermodynamicParameters], list[Union[dict, ThermodynamicParameters]]]] = empty_list()
    has_kinetic_equation: Optional[Union[Union[dict, KineticEquation], list[Union[dict, KineticEquation]]]] = empty_list()
    has_kinetic_model_parameter: Optional[Union[Union[dict, KineticModelParameter], list[Union[dict, KineticModelParameter]]]] = empty_list()
    is_reversible: Optional[Union[bool, Bool]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiocatalyticReactionId):
            self.id = BiocatalyticReactionId(self.id)

        if self.has_reaction_medium is not None and not isinstance(self.has_reaction_medium, ReactionMedium):
            self.has_reaction_medium = ReactionMedium(**as_dict(self.has_reaction_medium))

        self._normalize_inlined_as_list(slot_name="has_temperature_shift", slot_type=TemperatureShiftProcess, key_name="id", keyed=True)

        if self.has_temperature_gradient is not None and not isinstance(self.has_temperature_gradient, TemperatureGradient):
            self.has_temperature_gradient = TemperatureGradient(**as_dict(self.has_temperature_gradient))

        self._normalize_inlined_as_list(slot_name="has_ph_shift", slot_type=PHShiftProcess, key_name="id", keyed=True)

        if self.has_ph_gradient is not None and not isinstance(self.has_ph_gradient, PHGradient):
            self.has_ph_gradient = PHGradient(**as_dict(self.has_ph_gradient))

        if self.has_ph_measurement is not None and not isinstance(self.has_ph_measurement, PHMeasurementProcess):
            self.has_ph_measurement = PHMeasurementProcess(**as_dict(self.has_ph_measurement))

        self._normalize_inlined_as_list(slot_name="has_kinetic_parameters", slot_type=KineticParameters, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_yield_and_conversion", slot_type=YieldAndConversion, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_activity_and_reaction_rate", slot_type=ActivityAndInitialReactionRate, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_selectivity_and_specificity", slot_type=SelectivityAndSpecificity, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_thermodynamic_parameters", slot_type=ThermodynamicParameters, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_kinetic_equation", slot_type=KineticEquation, key_name="value", keyed=False)

        if not isinstance(self.has_kinetic_model_parameter, list):
            self.has_kinetic_model_parameter = [self.has_kinetic_model_parameter] if self.has_kinetic_model_parameter is not None else []
        self.has_kinetic_model_parameter = [v if isinstance(v, KineticModelParameter) else KineticModelParameter(**as_dict(v)) for v in self.has_kinetic_model_parameter]

        if self.is_reversible is not None and not isinstance(self.is_reversible, Bool):
            self.is_reversible = Bool(self.is_reversible)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DissolvingSubstance(AgenticEntity):
    """
    A liquid ChemicalSubstance that dissolves or that is capable of dissolving a ChemicalSubstance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010417"]
    class_class_curie: ClassVar[str] = "SIO:010417"
    class_name: ClassVar[str] = "DissolvingSubstance"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.DissolvingSubstance

    id: Union[str, DissolvingSubstanceId] = None
    has_percentage_of_total: Optional[Union[Union[dict, "PercentageOfTotal"], list[Union[dict, "PercentageOfTotal"]]]] = empty_list()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DissolvingSubstanceId):
            self.id = DissolvingSubstanceId(self.id)

        self._normalize_inlined_as_list(slot_name="has_percentage_of_total", slot_type=PercentageOfTotal, key_name="value", keyed=False)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalyst(AgenticEntity):
    """
    A ChemicalSubstance or MaterialEntity that initiates or accelerates a ChemicalReaction without itself being
    affected.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010344"]
    class_class_curie: ClassVar[str] = "SIO:010344"
    class_name: ClassVar[str] = "Catalyst"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Catalyst

    id: Union[str, CatalystId] = None
    has_molar_equivalent: Optional[Union[Union[dict, "MolarEquivalent"], list[Union[dict, "MolarEquivalent"]]]] = empty_list()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalystId):
            self.id = CatalystId(self.id)

        self._normalize_inlined_as_list(slot_name="has_molar_equivalent", slot_type=MolarEquivalent, key_name="value", keyed=False)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reactor(Device):
    """
    A reactor is a container for controlling a biological or chemical reaction or process.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFE["0000153"]
    class_class_curie: ClassVar[str] = "AFE:0000153"
    class_name: ClassVar[str] = "Reactor"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Reactor

    id: Union[str, ReactorId] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactorId):
            self.id = ReactorId(self.id)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReactionVessel(Reactor):
    """
    A reactor is a container for controlling a biological or chemical reaction or process. [Allotrope]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFE["0000153"]
    class_class_curie: ClassVar[str] = "AFE:0000153"
    class_name: ClassVar[str] = "ReactionVessel"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ReactionVessel

    id: Union[str, ReactionVesselId] = None
    has_constant_volume: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionVesselId):
            self.id = ReactionVesselId(self.id)

        if self.has_constant_volume is not None and not isinstance(self.has_constant_volume, Bool):
            self.has_constant_volume = Bool(self.has_constant_volume)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vial(ReactionVessel):
    """
    A vial is a small vessel or bottle. [Allotrope]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFE["0000329"]
    class_class_curie: ClassVar[str] = "AFE:0000329"
    class_name: ClassVar[str] = "Vial"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Vial

    id: Union[str, VialId] = None
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    vial_size_unit: Optional[Union[str, list[str]]] = empty_list()
    vial_material: Optional[Union[str, list[str]]] = empty_list()
    closure_type: Optional[Union[str, list[str]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, VialId):
            self.id = VialId(self.id)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        if not isinstance(self.vial_size_unit, list):
            self.vial_size_unit = [self.vial_size_unit] if self.vial_size_unit is not None else []
        self.vial_size_unit = [v if isinstance(v, str) else str(v) for v in self.vial_size_unit]

        if not isinstance(self.vial_material, list):
            self.vial_material = [self.vial_material] if self.vial_material is not None else []
        self.vial_material = [v if isinstance(v, str) else str(v) for v in self.vial_material]

        if not isinstance(self.closure_type, list):
            self.closure_type = [self.closure_type] if self.closure_type is not None else []
        self.closure_type = [v if isinstance(v, str) else str(v) for v in self.closure_type]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Plate(ReactionVessel):
    """
    A plate is a tray with multiple "wells" used as small test tubes. [Wikipedia]
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFE["0000029"]
    class_class_curie: ClassVar[str] = "AFE:0000029"
    class_name: ClassVar[str] = "Plate"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Plate

    id: Union[str, PlateId] = None
    plate_type: Optional[Union[str, list[str]]] = empty_list()
    plate_material: Optional[Union[str, list[str]]] = empty_list()
    number_of_wells: Optional[int] = None
    well_shape: Optional[Union[str, list[str]]] = empty_list()
    well_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    well_arrangement: Optional[Union[str, list[str]]] = empty_list()
    sealing_method: Optional[Union[str, list[str]]] = empty_list()
    sealing_material: Optional[Union[str, list[str]]] = empty_list()
    supplied_by: Optional[Union[dict, Agent]] = None
    other_identifier: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlateId):
            self.id = PlateId(self.id)

        if not isinstance(self.plate_type, list):
            self.plate_type = [self.plate_type] if self.plate_type is not None else []
        self.plate_type = [v if isinstance(v, str) else str(v) for v in self.plate_type]

        if not isinstance(self.plate_material, list):
            self.plate_material = [self.plate_material] if self.plate_material is not None else []
        self.plate_material = [v if isinstance(v, str) else str(v) for v in self.plate_material]

        if self.number_of_wells is not None and not isinstance(self.number_of_wells, int):
            self.number_of_wells = int(self.number_of_wells)

        if not isinstance(self.well_shape, list):
            self.well_shape = [self.well_shape] if self.well_shape is not None else []
        self.well_shape = [v if isinstance(v, str) else str(v) for v in self.well_shape]

        self._normalize_inlined_as_list(slot_name="well_volume", slot_type=Volume, key_name="value", keyed=False)

        if not isinstance(self.well_arrangement, list):
            self.well_arrangement = [self.well_arrangement] if self.well_arrangement is not None else []
        self.well_arrangement = [v if isinstance(v, str) else str(v) for v in self.well_arrangement]

        if not isinstance(self.sealing_method, list):
            self.sealing_method = [self.sealing_method] if self.sealing_method is not None else []
        self.sealing_method = [v if isinstance(v, str) else str(v) for v in self.sealing_method]

        if not isinstance(self.sealing_material, list):
            self.sealing_material = [self.sealing_material] if self.sealing_material is not None else []
        self.sealing_material = [v if isinstance(v, str) else str(v) for v in self.sealing_material]

        if self.supplied_by is not None and not isinstance(self.supplied_by, Agent):
            self.supplied_by = Agent(**as_dict(self.supplied_by))

        if self.other_identifier is not None and not isinstance(self.other_identifier, str):
            self.other_identifier = str(self.other_identifier)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StirredTankReactor(ReactionVessel):
    """
    An abstract concept/ideal reactor model type, in which the volume of fluid in the reaction vessel is considered to
    be perfectly mixed which results in the same concentration of all components in the whole reaction volume.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007103"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0007103"
    class_name: ClassVar[str] = "StirredTankReactor"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.StirredTankReactor

    id: Union[str, StirredTankReactorId] = None
    reactor_material: Optional[Union[str, list[str]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    geometry: Optional[str] = None
    bottom_type: Optional[Union[str, list[str]]] = empty_list()
    has_part: Optional[Union[dict[Union[str, DeviceId], Union[dict, Device]], list[Union[dict, Device]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StirredTankReactorId):
            self.id = StirredTankReactorId(self.id)

        if not isinstance(self.reactor_material, list):
            self.reactor_material = [self.reactor_material] if self.reactor_material is not None else []
        self.reactor_material = [v if isinstance(v, str) else str(v) for v in self.reactor_material]

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        if self.geometry is not None and not isinstance(self.geometry, str):
            self.geometry = str(self.geometry)

        if not isinstance(self.bottom_type, list):
            self.bottom_type = [self.bottom_type] if self.bottom_type is not None else []
        self.bottom_type = [v if isinstance(v, str) else str(v) for v in self.bottom_type]

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=Device, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TubularFlowReactor(ReactionVessel):
    """
    A reactor model, in which opposing to the ideal plug flow behavior, friction is acting on the fluid, thus creating
    a residence time distribution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = VOC4CAT["0007104"]
    class_class_curie: ClassVar[str] = "VOC4CAT:0007104"
    class_name: ClassVar[str] = "TubularFlowReactor"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.TubularFlowReactor

    id: Union[str, TubularFlowReactorId] = None
    reactor_type_description: Optional[Union[str, list[str]]] = empty_list()
    reactor_material: Optional[Union[str, list[str]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    geometry: Optional[str] = None
    tubing: Optional[Union[str, list[str]]] = empty_list()
    has_flow_rate: Optional[Union[Union[dict, FlowRate], list[Union[dict, FlowRate]]]] = empty_list()
    has_catalyst_localisation: Optional[Union[str, list[str]]] = empty_list()
    has_residence_time: Optional[Union[Union[dict, ResidenceTime], list[Union[dict, ResidenceTime]]]] = empty_list()
    has_reynolds_number: Optional[Union[str, list[str]]] = empty_list()
    has_passive_mixing: Optional[Union[str, list[str]]] = empty_list()
    has_active_mixer: Optional[Union[str, list[str]]] = empty_list()
    has_pulsing_description: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TubularFlowReactorId):
            self.id = TubularFlowReactorId(self.id)

        if not isinstance(self.reactor_type_description, list):
            self.reactor_type_description = [self.reactor_type_description] if self.reactor_type_description is not None else []
        self.reactor_type_description = [v if isinstance(v, str) else str(v) for v in self.reactor_type_description]

        if not isinstance(self.reactor_material, list):
            self.reactor_material = [self.reactor_material] if self.reactor_material is not None else []
        self.reactor_material = [v if isinstance(v, str) else str(v) for v in self.reactor_material]

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        if self.geometry is not None and not isinstance(self.geometry, str):
            self.geometry = str(self.geometry)

        if not isinstance(self.tubing, list):
            self.tubing = [self.tubing] if self.tubing is not None else []
        self.tubing = [v if isinstance(v, str) else str(v) for v in self.tubing]

        self._normalize_inlined_as_list(slot_name="has_flow_rate", slot_type=FlowRate, key_name="value", keyed=False)

        if not isinstance(self.has_catalyst_localisation, list):
            self.has_catalyst_localisation = [self.has_catalyst_localisation] if self.has_catalyst_localisation is not None else []
        self.has_catalyst_localisation = [v if isinstance(v, str) else str(v) for v in self.has_catalyst_localisation]

        self._normalize_inlined_as_list(slot_name="has_residence_time", slot_type=ResidenceTime, key_name="value", keyed=False)

        if not isinstance(self.has_reynolds_number, list):
            self.has_reynolds_number = [self.has_reynolds_number] if self.has_reynolds_number is not None else []
        self.has_reynolds_number = [v if isinstance(v, str) else str(v) for v in self.has_reynolds_number]

        if not isinstance(self.has_passive_mixing, list):
            self.has_passive_mixing = [self.has_passive_mixing] if self.has_passive_mixing is not None else []
        self.has_passive_mixing = [v if isinstance(v, str) else str(v) for v in self.has_passive_mixing]

        if not isinstance(self.has_active_mixer, list):
            self.has_active_mixer = [self.has_active_mixer] if self.has_active_mixer is not None else []
        self.has_active_mixer = [v if isinstance(v, str) else str(v) for v in self.has_active_mixer]

        if not isinstance(self.has_pulsing_description, list):
            self.has_pulsing_description = [self.has_pulsing_description] if self.has_pulsing_description is not None else []
        self.has_pulsing_description = [v if isinstance(v, str) else str(v) for v in self.has_pulsing_description]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Yield(QuantitativeAttribute):
    """
    A dimensionless physical quantity describing the fraction of a product B that is formed from a reactant A taking
    into account the stoichiometry. If A fully reacts to B without side-reactions, the yield of product B is 1 (or 100
    %).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHMO["0002855"]
    class_class_curie: ClassVar[str] = "CHMO:0002855"
    class_name: ClassVar[str] = "Yield"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Yield

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class MolarEquivalent(QuantitativeAttribute):
    """
    A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a
    reference substance in a chemical reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "MolarEquivalent"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MolarEquivalent

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class PercentageOfTotal(QuantitativeAttribute):
    """
    A dimensionless ratio that quantifies the stoichiometric proportion of a chemical substance relative to a
    reference substance in a chemical reaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "PercentageOfTotal"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PercentageOfTotal

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class MaterialisticMixin(YAMLRoot):
    """
    A LinkML mixin used to pass down properties common to all material entities. It is needed for example to have
    MaterialSample have the same properties as MaterialEntity, although it is defined as a subclass of
    EvaluatedEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MATERIAL_ENTITIES_AP["MaterialisticMixin"]
    class_class_curie: ClassVar[str] = "material_entities_ap:MaterialisticMixin"
    class_name: ClassVar[str] = "MaterialisticMixin"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MaterialisticMixin

    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalSubstanceMixin(MaterialisticMixin):
    """
    A LinkML mixin used to pass down properties common to all material entities that are described in a chemical
    context via being composed of chemical entities (e.g. atom, molecule, ion, ion pair, radical, complex, conformer
    etc., ) of the same type or of different types.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMICAL_ENTITIES_AP["ChemicalSubstanceMixin"]
    class_class_curie: ClassVar[str] = "chemical_entities_ap:ChemicalSubstanceMixin"
    class_name: ClassVar[str] = "ChemicalSubstanceMixin"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ChemicalSubstanceMixin

    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


class PolymerMixin(ChemicalSubstanceMixin):
    """
    A LinkML mixin used to pass down properties common to all chemical substances that are composed of macromolecules
    of different kinds and which may be differentiated by composition, length, degree of branching etc..
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEMICAL_ENTITIES_AP["PolymerMixin"]
    class_class_curie: ClassVar[str] = "chemical_entities_ap:PolymerMixin"
    class_name: ClassVar[str] = "PolymerMixin"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PolymerMixin


@dataclass(repr=False)
class MaterialEntity(Entity):
    """
    A material is an Entity that has some portion of matter as proper part.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BFO["0000040"]
    class_class_curie: ClassVar[str] = "BFO:0000040"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    has_part: Optional[Union[dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], list[Union[dict, "MaterialEntity"]]]] = empty_dict()
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        self._normalize_inlined_as_list(slot_name="has_part", slot_type=MaterialEntity, key_name="id", keyed=True)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Biocatalyst(MaterialEntity):
    """
    An enzyme or cell that catalyzes a biocatalytic reaction. Subclass of MaterialEntity. The physical form in which
    it is applied is described by an associated BiocatalystPreparation; its role as the catalyst of a specific
    BiocatalyticReaction is described by a Catalyst wrapper via used_catalyst.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CHEBI["35233"]
    class_class_curie: ClassVar[str] = "CHEBI:35233"
    class_name: ClassVar[str] = "Biocatalyst"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Biocatalyst

    id: Union[str, BiocatalystId] = None
    is_self_produced: Union[bool, Bool] = None
    title: str = None
    ec_number: Optional[Union[str, list[str]]] = empty_list()
    sequence_amino_acid: Optional[Union[str, list[str]]] = empty_list()
    sequence_DNA: Optional[Union[str, list[str]]] = empty_list()
    origin_organism: Optional[Union[str, list[str]]] = empty_list()
    posttranslational_modification: Optional[Union[str, list[str]]] = empty_list()
    molecular_weight: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()
    has_biocatalyst_production_process: Optional[Union[dict, BiocatalystProductionProcess]] = None
    organism_taxonomy_id: Optional[Union[str, list[str]]] = empty_list()
    other_identifier: Optional[str] = None
    has_quantitative_attribute: Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiocatalystId):
            self.id = BiocatalystId(self.id)

        if self._is_empty(self.is_self_produced):
            self.MissingRequiredField("is_self_produced")
        if not isinstance(self.is_self_produced, Bool):
            self.is_self_produced = Bool(self.is_self_produced)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if not isinstance(self.ec_number, list):
            self.ec_number = [self.ec_number] if self.ec_number is not None else []
        self.ec_number = [v if isinstance(v, str) else str(v) for v in self.ec_number]

        if not isinstance(self.sequence_amino_acid, list):
            self.sequence_amino_acid = [self.sequence_amino_acid] if self.sequence_amino_acid is not None else []
        self.sequence_amino_acid = [v if isinstance(v, str) else str(v) for v in self.sequence_amino_acid]

        if not isinstance(self.sequence_DNA, list):
            self.sequence_DNA = [self.sequence_DNA] if self.sequence_DNA is not None else []
        self.sequence_DNA = [v if isinstance(v, str) else str(v) for v in self.sequence_DNA]

        if not isinstance(self.origin_organism, list):
            self.origin_organism = [self.origin_organism] if self.origin_organism is not None else []
        self.origin_organism = [v if isinstance(v, str) else str(v) for v in self.origin_organism]

        if not isinstance(self.posttranslational_modification, list):
            self.posttranslational_modification = [self.posttranslational_modification] if self.posttranslational_modification is not None else []
        self.posttranslational_modification = [v if isinstance(v, str) else str(v) for v in self.posttranslational_modification]

        self._normalize_inlined_as_list(slot_name="molecular_weight", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        if self.has_biocatalyst_production_process is not None and not isinstance(self.has_biocatalyst_production_process, BiocatalystProductionProcess):
            self.has_biocatalyst_production_process = BiocatalystProductionProcess(**as_dict(self.has_biocatalyst_production_process))

        if not isinstance(self.organism_taxonomy_id, list):
            self.organism_taxonomy_id = [self.organism_taxonomy_id] if self.organism_taxonomy_id is not None else []
        self.organism_taxonomy_id = [v if isinstance(v, str) else str(v) for v in self.organism_taxonomy_id]

        if self.other_identifier is not None and not isinstance(self.other_identifier, str):
            self.other_identifier = str(self.other_identifier)

        self._normalize_inlined_as_list(slot_name="has_quantitative_attribute", slot_type=QuantitativeAttribute, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReactionMedium(MaterialEntity):
    """
    The medium in which a biocatalytic reaction takes place, described by its phase composition, ionic strength, and
    additives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["ReactionMedium"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:ReactionMedium"
    class_name: ClassVar[str] = "ReactionMedium"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ReactionMedium

    id: Union[str, ReactionMediumId] = None
    has_phase_count: Optional[int] = None
    has_liquid_phase: Optional[Union[dict[Union[str, LiquidPhaseId], Union[dict, "LiquidPhase"]], list[Union[dict, "LiquidPhase"]]]] = empty_dict()
    has_solid_phase: Optional[Union[dict[Union[str, SolidPhaseId], Union[dict, "SolidPhase"]], list[Union[dict, "SolidPhase"]]]] = empty_dict()
    has_gas_phase: Optional[Union[dict[Union[str, GasPhaseId], Union[dict, "GasPhase"]], list[Union[dict, "GasPhase"]]]] = empty_dict()
    has_ionic_strength: Optional[Union[Union[dict, IonicStrength], list[Union[dict, IonicStrength]]]] = empty_list()
    has_medium_additive: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionMediumId):
            self.id = ReactionMediumId(self.id)

        if self.has_phase_count is not None and not isinstance(self.has_phase_count, int):
            self.has_phase_count = int(self.has_phase_count)

        self._normalize_inlined_as_list(slot_name="has_liquid_phase", slot_type=LiquidPhase, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_solid_phase", slot_type=SolidPhase, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_gas_phase", slot_type=GasPhase, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_ionic_strength", slot_type=IonicStrength, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_medium_additive", slot_type=ChemicalEntity, key_name="id", keyed=True)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LiquidPhase(MaterialEntity):
    """
    A liquid phase present in the reaction medium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BAO["0002164"]
    class_class_curie: ClassVar[str] = "BAO:0002164"
    class_name: ClassVar[str] = "LiquidPhase"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.LiquidPhase

    id: Union[str, LiquidPhaseId] = None
    has_liquid_type: Optional[Union[str, list[str]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, LiquidPhaseId):
            self.id = LiquidPhaseId(self.id)

        if not isinstance(self.has_liquid_type, list):
            self.has_liquid_type = [self.has_liquid_type] if self.has_liquid_type is not None else []
        self.has_liquid_type = [v if isinstance(v, str) else str(v) for v in self.has_liquid_type]

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SolidPhase(MaterialEntity):
    """
    A solid phase present in the reaction medium.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BAO["0002163"]
    class_class_curie: ClassVar[str] = "BAO:0002163"
    class_name: ClassVar[str] = "SolidPhase"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SolidPhase

    id: Union[str, SolidPhaseId] = None
    has_solid_type: Optional[Union[str, list[str]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SolidPhaseId):
            self.id = SolidPhaseId(self.id)

        if not isinstance(self.has_solid_type, list):
            self.has_solid_type = [self.has_solid_type] if self.has_solid_type is not None else []
        self.has_solid_type = [v if isinstance(v, str) else str(v) for v in self.has_solid_type]

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GasPhase(MaterialEntity):
    """
    A gas phase present in the reaction medium or headspace.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NPO["1613"]
    class_class_curie: ClassVar[str] = "NPO:1613"
    class_name: ClassVar[str] = "GasPhase"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.GasPhase

    id: Union[str, GasPhaseId] = None
    has_gas_type: Optional[Union[str, list[str]]] = empty_list()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GasPhaseId):
            self.id = GasPhaseId(self.id)

        if not isinstance(self.has_gas_type, list):
            self.has_gas_type = [self.has_gas_type] if self.has_gas_type is not None else []
        self.has_gas_type = [v if isinstance(v, str) else str(v) for v in self.has_gas_type]

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StartingMaterial(MaterialEntity):
    """
    A ChemicalSubstance with that has a starting material role in a synthesis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = PROCO["0000029"]
    class_class_curie: ClassVar[str] = "PROCO:0000029"
    class_name: ClassVar[str] = "StartingMaterial"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.StartingMaterial

    id: Union[str, StartingMaterialId] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StartingMaterialId):
            self.id = StartingMaterialId(self.id)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_molar_equivalent", slot_type=MolarEquivalent, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reagent(MaterialEntity):
    """
    A ChemicalSubstance that is consumed or transformed in a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["010411"]
    class_class_curie: ClassVar[str] = "SIO:010411"
    class_name: ClassVar[str] = "Reagent"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Reagent

    id: Union[str, ReagentId] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_molar_equivalent: Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReagentId):
            self.id = ReagentId(self.id)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_molar_equivalent", slot_type=MolarEquivalent, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChemicalProduct(MaterialEntity):
    """
    A chemical substance that is produced by a ChemicalReaction.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NCIT["C48810"]
    class_class_curie: ClassVar[str] = "NCIT:C48810"
    class_name: ClassVar[str] = "ChemicalProduct"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ChemicalProduct

    id: Union[str, ChemicalProductId] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ChemicalProductId):
            self.id = ChemicalProductId(self.id)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MaterialSample(EvaluatedEntity):
    """
    A Sample that was derived from a previous MaterialSample or some other kind of MaterialEntity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OBI["0000747"]
    class_class_curie: ClassVar[str] = "OBI:0000747"
    class_name: ClassVar[str] = "MaterialSample"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MaterialSample

    id: Union[str, MaterialSampleId] = None
    derived_from: Optional[Union[dict, Entity]] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialSampleId):
            self.id = MaterialSampleId(self.id)

        if self.derived_from is not None and not isinstance(self.derived_from, Entity):
            self.derived_from = Entity(**as_dict(self.derived_from))

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SubstanceSample(MaterialSample):
    """
    A MaterialSample derived from a chemical substance that is of interest in an analytical procedure.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001378"]
    class_class_curie: ClassVar[str] = "SIO:001378"
    class_name: ClassVar[str] = "SubstanceSample"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SubstanceSample

    id: Union[str, SubstanceSampleId] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubstanceSampleId):
            self.id = SubstanceSampleId(self.id)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiocatalystPreparation(SubstanceSample):
    """
    The physical form in which a Biocatalyst is applied in a BiocatalyticExperiment. Derived from the Biocatalyst
    entity via prov:wasDerivedFrom. Subclasses encode the specific application form; the application_form slot is
    retained here for P-002 converter compatibility but is redundant with the subclass type.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["BiocatalystPreparation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:BiocatalystPreparation"
    class_name: ClassVar[str] = "BiocatalystPreparation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.BiocatalystPreparation

    id: Union[str, BiocatalystPreparationId] = None
    application_form: Union[str, "BiocatalystApplicationFormEnum"] = None
    derived_from: Union[dict, Biocatalyst] = None
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_activity: Optional[Union[Union[dict, SpecificActivity], list[Union[dict, SpecificActivity]]]] = empty_list()
    has_formulation: Optional[Union[str, list[str]]] = empty_list()
    has_storage_conditions: Optional[Union[dict, StorageConditions]] = None
    had_drying_process: Optional[Union[dict, DryingProcess]] = None
    has_constant_concentration: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiocatalystPreparationId):
            self.id = BiocatalystPreparationId(self.id)

        if self._is_empty(self.application_form):
            self.MissingRequiredField("application_form")
        if not isinstance(self.application_form, BiocatalystApplicationFormEnum):
            self.application_form = BiocatalystApplicationFormEnum(self.application_form)

        if self._is_empty(self.derived_from):
            self.MissingRequiredField("derived_from")
        if not isinstance(self.derived_from, Biocatalyst):
            self.derived_from = Biocatalyst(**as_dict(self.derived_from))

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_activity", slot_type=SpecificActivity, key_name="value", keyed=False)

        if not isinstance(self.has_formulation, list):
            self.has_formulation = [self.has_formulation] if self.has_formulation is not None else []
        self.has_formulation = [v if isinstance(v, str) else str(v) for v in self.has_formulation]

        if self.has_storage_conditions is not None and not isinstance(self.has_storage_conditions, StorageConditions):
            self.has_storage_conditions = StorageConditions(**as_dict(self.has_storage_conditions))

        if self.had_drying_process is not None and not isinstance(self.had_drying_process, DryingProcess):
            self.had_drying_process = DryingProcess(**as_dict(self.had_drying_process))

        if self.has_constant_concentration is not None and not isinstance(self.has_constant_concentration, Bool):
            self.has_constant_concentration = Bool(self.has_constant_concentration)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PurifiedEnzymePreparation(BiocatalystPreparation):
    """
    A BiocatalystPreparation consisting of a purified enzyme solution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["PurifiedEnzymePreparation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:PurifiedEnzymePreparation"
    class_name: ClassVar[str] = "PurifiedEnzymePreparation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PurifiedEnzymePreparation

    id: Union[str, PurifiedEnzymePreparationId] = None
    application_form: Union[str, "BiocatalystApplicationFormEnum"] = None
    derived_from: Union[dict, Biocatalyst] = None
    concentration_determination_method: Optional[Union[str, list[str]]] = empty_list()
    activity_determination_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PurifiedEnzymePreparationId):
            self.id = PurifiedEnzymePreparationId(self.id)

        if not isinstance(self.concentration_determination_method, list):
            self.concentration_determination_method = [self.concentration_determination_method] if self.concentration_determination_method is not None else []
        self.concentration_determination_method = [v if isinstance(v, str) else str(v) for v in self.concentration_determination_method]

        if not isinstance(self.activity_determination_method, list):
            self.activity_determination_method = [self.activity_determination_method] if self.activity_determination_method is not None else []
        self.activity_determination_method = [v if isinstance(v, str) else str(v) for v in self.activity_determination_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CrudeCellExtractPreparation(BiocatalystPreparation):
    """
    A BiocatalystPreparation consisting of a crude cell extract obtained by cell disruption.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["CrudeCellExtractPreparation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:CrudeCellExtractPreparation"
    class_name: ClassVar[str] = "CrudeCellExtractPreparation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.CrudeCellExtractPreparation

    id: Union[str, CrudeCellExtractPreparationId] = None
    application_form: Union[str, "BiocatalystApplicationFormEnum"] = None
    derived_from: Union[dict, Biocatalyst] = None
    cell_disruption_process: Optional[Union[str, list[str]]] = empty_list()
    concentration_determination_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CrudeCellExtractPreparationId):
            self.id = CrudeCellExtractPreparationId(self.id)

        if not isinstance(self.cell_disruption_process, list):
            self.cell_disruption_process = [self.cell_disruption_process] if self.cell_disruption_process is not None else []
        self.cell_disruption_process = [v if isinstance(v, str) else str(v) for v in self.cell_disruption_process]

        if not isinstance(self.concentration_determination_method, list):
            self.concentration_determination_method = [self.concentration_determination_method] if self.concentration_determination_method is not None else []
        self.concentration_determination_method = [v if isinstance(v, str) else str(v) for v in self.concentration_determination_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WholeCellPreparation(BiocatalystPreparation):
    """
    A BiocatalystPreparation in which whole cells serve as the biocatalyst.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["WholeCellPreparation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:WholeCellPreparation"
    class_name: ClassVar[str] = "WholeCellPreparation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.WholeCellPreparation

    id: Union[str, WholeCellPreparationId] = None
    application_form: Union[str, "BiocatalystApplicationFormEnum"] = None
    derived_from: Union[dict, Biocatalyst] = None
    harvesting_method: Optional[Union[str, list[str]]] = empty_list()
    concentration_determination_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WholeCellPreparationId):
            self.id = WholeCellPreparationId(self.id)

        if not isinstance(self.harvesting_method, list):
            self.harvesting_method = [self.harvesting_method] if self.harvesting_method is not None else []
        self.harvesting_method = [v if isinstance(v, str) else str(v) for v in self.harvesting_method]

        if not isinstance(self.concentration_determination_method, list):
            self.concentration_determination_method = [self.concentration_determination_method] if self.concentration_determination_method is not None else []
        self.concentration_determination_method = [v if isinstance(v, str) else str(v) for v in self.concentration_determination_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SecretedEnzymePreparation(BiocatalystPreparation):
    """
    A BiocatalystPreparation consisting of an enzyme secreted into the culture supernatant and separated from cells.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["SecretedEnzymePreparation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:SecretedEnzymePreparation"
    class_name: ClassVar[str] = "SecretedEnzymePreparation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.SecretedEnzymePreparation

    id: Union[str, SecretedEnzymePreparationId] = None
    application_form: Union[str, "BiocatalystApplicationFormEnum"] = None
    derived_from: Union[dict, Biocatalyst] = None
    separation_method: Optional[Union[str, list[str]]] = empty_list()
    concentration_determination_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SecretedEnzymePreparationId):
            self.id = SecretedEnzymePreparationId(self.id)

        if not isinstance(self.separation_method, list):
            self.separation_method = [self.separation_method] if self.separation_method is not None else []
        self.separation_method = [v if isinstance(v, str) else str(v) for v in self.separation_method]

        if not isinstance(self.concentration_determination_method, list):
            self.concentration_determination_method = [self.concentration_determination_method] if self.concentration_determination_method is not None else []
        self.concentration_determination_method = [v if isinstance(v, str) else str(v) for v in self.concentration_determination_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CellFreePreparation(BiocatalystPreparation):
    """
    A BiocatalystPreparation produced by cell-free expression, where synthesis occurs outside living cells using
    extracted cellular machinery.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["CellFreePreparation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:CellFreePreparation"
    class_name: ClassVar[str] = "CellFreePreparation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.CellFreePreparation

    id: Union[str, CellFreePreparationId] = None
    application_form: Union[str, "BiocatalystApplicationFormEnum"] = None
    derived_from: Union[dict, Biocatalyst] = None
    source_of_cellfree_extract: Optional[Union[str, list[str]]] = empty_list()
    concentration_determination_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CellFreePreparationId):
            self.id = CellFreePreparationId(self.id)

        if not isinstance(self.source_of_cellfree_extract, list):
            self.source_of_cellfree_extract = [self.source_of_cellfree_extract] if self.source_of_cellfree_extract is not None else []
        self.source_of_cellfree_extract = [v if isinstance(v, str) else str(v) for v in self.source_of_cellfree_extract]

        if not isinstance(self.concentration_determination_method, list):
            self.concentration_determination_method = [self.concentration_determination_method] if self.concentration_determination_method is not None else []
        self.concentration_determination_method = [v if isinstance(v, str) else str(v) for v in self.concentration_determination_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImmobilisedPreparation(BiocatalystPreparation):
    """
    A BiocatalystPreparation in which the biocatalyst is attached to or entrapped within a carrier material. Always
    derived from another BiocatalystPreparation via prov:wasDerivedFrom.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS["ImmobilisedPreparation"]
    class_class_curie: ClassVar[str] = "strendcat_biocatalysis:ImmobilisedPreparation"
    class_name: ClassVar[str] = "ImmobilisedPreparation"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.ImmobilisedPreparation

    id: Union[str, ImmobilisedPreparationId] = None
    application_form: Union[str, "BiocatalystApplicationFormEnum"] = None
    derived_from: Union[dict, BiocatalystPreparation] = None
    immobilisation_chemistry: Optional[Union[str, list[str]]] = empty_list()
    carrier_material: Optional[Union[str, list[str]]] = empty_list()
    linkers: Optional[Union[str, list[str]]] = empty_list()
    immobilisation_method: Optional[Union[str, list[str]]] = empty_list()
    purification_method: Optional[Union[str, list[str]]] = empty_list()
    concentration_determination_method: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImmobilisedPreparationId):
            self.id = ImmobilisedPreparationId(self.id)

        if self._is_empty(self.derived_from):
            self.MissingRequiredField("derived_from")
        if not isinstance(self.derived_from, BiocatalystPreparation):
            self.derived_from = BiocatalystPreparation(**as_dict(self.derived_from))

        if not isinstance(self.immobilisation_chemistry, list):
            self.immobilisation_chemistry = [self.immobilisation_chemistry] if self.immobilisation_chemistry is not None else []
        self.immobilisation_chemistry = [v if isinstance(v, str) else str(v) for v in self.immobilisation_chemistry]

        if not isinstance(self.carrier_material, list):
            self.carrier_material = [self.carrier_material] if self.carrier_material is not None else []
        self.carrier_material = [v if isinstance(v, str) else str(v) for v in self.carrier_material]

        if not isinstance(self.linkers, list):
            self.linkers = [self.linkers] if self.linkers is not None else []
        self.linkers = [v if isinstance(v, str) else str(v) for v in self.linkers]

        if not isinstance(self.immobilisation_method, list):
            self.immobilisation_method = [self.immobilisation_method] if self.immobilisation_method is not None else []
        self.immobilisation_method = [v if isinstance(v, str) else str(v) for v in self.immobilisation_method]

        if not isinstance(self.purification_method, list):
            self.purification_method = [self.purification_method] if self.purification_method is not None else []
        self.purification_method = [v if isinstance(v, str) else str(v) for v in self.purification_method]

        if not isinstance(self.concentration_determination_method, list):
            self.concentration_determination_method = [self.concentration_determination_method] if self.concentration_determination_method is not None else []
        self.concentration_determination_method = [v if isinstance(v, str) else str(v) for v in self.concentration_determination_method]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PolymerSample(SubstanceSample):
    """
    A SubstanceSample derived from a Polymer.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001378"]
    class_class_curie: ClassVar[str] = "SIO:001378"
    class_name: ClassVar[str] = "PolymerSample"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.PolymerSample

    id: Union[str, PolymerSampleId] = None
    alternative_label: Optional[str] = None
    has_physical_state: Optional[Union[str, "PhysicalStateEnum"]] = None
    has_temperature: Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]] = empty_list()
    has_mass: Optional[Union[Union[dict, "Mass"], list[Union[dict, "Mass"]]]] = empty_list()
    has_volume: Optional[Union[Union[dict, "Volume"], list[Union[dict, "Volume"]]]] = empty_list()
    has_density: Optional[Union[Union[dict, "Density"], list[Union[dict, "Density"]]]] = empty_list()
    has_pressure: Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]] = empty_list()
    has_concentration: Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]] = empty_list()
    has_ph_value: Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]] = empty_list()
    composed_of: Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]] = empty_dict()
    has_amount: Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PolymerSampleId):
            self.id = PolymerSampleId(self.id)

        if self.alternative_label is not None and not isinstance(self.alternative_label, str):
            self.alternative_label = str(self.alternative_label)

        if self.has_physical_state is not None and not isinstance(self.has_physical_state, PhysicalStateEnum):
            self.has_physical_state = PhysicalStateEnum(self.has_physical_state)

        self._normalize_inlined_as_list(slot_name="has_temperature", slot_type=Temperature, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_mass", slot_type=Mass, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_volume", slot_type=Volume, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_density", slot_type=Density, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_pressure", slot_type=Pressure, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_concentration", slot_type=Concentration, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="has_ph_value", slot_type=PHValue, key_name="value", keyed=False)

        self._normalize_inlined_as_list(slot_name="composed_of", slot_type=ChemicalEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_amount", slot_type=AmountOfSubstance, key_name="value", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Temperature(QuantitativeAttribute):
    """
    A physical quantity that quantitatively expresses the attribute of hotness or coldness.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Temperature"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Temperature

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Mass(QuantitativeAttribute):
    """
    The strength of a body's gravitational attraction to other bodies.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Mass"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Mass

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class MolarMass(Mass):
    """
    A Mass (physical quality) that quantifies the mass of a homogeneous ChemicalSubstance containing 6.02 x 10^23
    atoms or molecules.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AFR["0002409"]
    class_class_curie: ClassVar[str] = "AFR:0002409"
    class_name: ClassVar[str] = "MolarMass"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.MolarMass

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Volume(QuantitativeAttribute):
    """
    A measure of regions in three-dimensional space.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Volume

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Density(QuantitativeAttribute):
    """
    A measure of the mass per unit volume of a substance.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001406"]
    class_class_curie: ClassVar[str] = "SIO:001406"
    class_name: ClassVar[str] = "Density"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Density

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

@dataclass(repr=False)
class Pressure(QuantitativeAttribute):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Quantity"]
    class_class_curie: ClassVar[str] = "qudt:Quantity"
    class_name: ClassVar[str] = "Pressure"
    class_model_uri: ClassVar[URIRef] = STRENDCAT_BIOCATALYSIS.Pressure

    value: float = None
    has_quantity_type: Union[str, DefinedTermId] = None

# Enumerations
class OperationModeEnum(EnumDefinitionImpl):
    """
    The mode in which a biocatalytic experiment was operated.
    """
    Batch = PermissibleValue(
        text="Batch",
        description="""All reaction components are mixed simultaneously in a closed system and the reaction proceeds until a predetermined endpoint.""",
        meaning=VOC4CAT["0000110"])
    FedBatch = PermissibleValue(
        text="FedBatch",
        description="""Additional compounds are gradually added during the reaction to control reaction conditions or enhance product formation.""")
    Continuous = PermissibleValue(
        text="Continuous",
        description="""The reaction operates continuously with substrates continuously supplied and products continuously removed.""",
        meaning=VOC4CAT["0000109"])
    Combinatorial = PermissibleValue(
        text="Combinatorial",
        description="""A mixture of operation modes used to systematically explore various reaction conditions or components in a combined manner.""")

    _defn = EnumDefinition(
        name="OperationModeEnum",
        description="The mode in which a biocatalytic experiment was operated.",
    )

class BiocatalystApplicationFormEnum(EnumDefinitionImpl):
    """
    The physical form in which a biocatalyst is applied in an experiment.
    """
    PurifiedEnzyme = PermissibleValue(
        text="PurifiedEnzyme",
        meaning=OBI["0000925"])
    CrudeCellExtract = PermissibleValue(
        text="CrudeCellExtract",
        meaning=OBI["0000261"])
    WholeCell = PermissibleValue(
        text="WholeCell",
        meaning=OBI["0000651"])
    SecretedEnzyme = PermissibleValue(
        text="SecretedEnzyme",
        description="Enzyme secreted into culture supernatant and separated from cells.")
    CellFreeProduction = PermissibleValue(
        text="CellFreeProduction",
        meaning=OBI["0000737"])
    Immobilised = PermissibleValue(
        text="Immobilised",
        description="Biocatalyst attached to or entrapped within a carrier material.")

    _defn = EnumDefinition(
        name="BiocatalystApplicationFormEnum",
        description="The physical form in which a biocatalyst is applied in an experiment.",
    )

class ComponentRoleEnum(EnumDefinitionImpl):
    """
    The functional role of a chemical component in a biocatalytic reaction. Maps to CHEBI role hierarchy. Optional per
    P-002 — a structural converter may leave this unpopulated.
    """
    Substrate = PermissibleValue(
        text="Substrate",
        meaning=CHEBI["78675"])
    Cofactor = PermissibleValue(
        text="Cofactor",
        meaning=CHEBI["23357"])
    Buffer = PermissibleValue(
        text="Buffer",
        meaning=CHEBI["35225"])
    Cosolvent = PermissibleValue(
        text="Cosolvent",
        meaning=CHEBI["46787"])
    SaltIon = PermissibleValue(
        text="SaltIon",
        meaning=CHEBI["24867"])
    InternalStandard = PermissibleValue(
        text="InternalStandard",
        meaning=CHEBI["50504"])
    Activator = PermissibleValue(
        text="Activator",
        description="""A substance that increases the rate or extent of a biocatalytic reaction without being consumed (EnzymeML ModifierRole ACTIVATOR).""")
    Inhibitor = PermissibleValue(
        text="Inhibitor",
        description="""A substance that decreases the rate or extent of a biocatalytic reaction (EnzymeML ModifierRole INHIBITOR). Fuer den eigentlichen Ki-Wert weiterhin EnzymeInhibitionCharacterisation verwenden.""")
    Solvent = PermissibleValue(
        text="Solvent",
        description="""The primary liquid a reaction is carried out in, as distinct from Cosolvent (EnzymeML ModifierRole SOLVENT).""")
    AuxiliaryCatalyst = PermissibleValue(
        text="AuxiliaryCatalyst",
        description="""A non-biological catalyst present alongside or instead of the Biocatalyst (EnzymeML ModifierRole CATALYST, wenn KEIN Biokatalysator gemeint ist -- der Biokatalysator selbst laeuft ueber used_catalyst, nicht ueber diese Rolle).""")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="ComponentRoleEnum",
        description="""The functional role of a chemical component in a biocatalytic reaction. Maps to CHEBI role hierarchy. Optional per P-002 — a structural converter may leave this unpopulated.""",
    )

class InhibitionTypeEnum(EnumDefinitionImpl):
    """
    Type of enzyme inhibition observed.
    """
    Competitive = PermissibleValue(
        text="Competitive",
        meaning=SIO["010997"])
    NonCompetitive = PermissibleValue(
        text="NonCompetitive",
        meaning=SIO["010998"])
    Uncompetitive = PermissibleValue(
        text="Uncompetitive",
        meaning=SIO["010999"])
    Mixed = PermissibleValue(text="Mixed")
    Irreversible = PermissibleValue(text="Irreversible")

    _defn = EnumDefinition(
        name="InhibitionTypeEnum",
        description="Type of enzyme inhibition observed.",
    )

class DryingMethodEnum(EnumDefinitionImpl):
    """
    Method used to remove moisture from a biocatalyst preparation.
    """
    FreezeDrying = PermissibleValue(
        text="FreezeDrying",
        description="Lyophilization — moisture removed under vacuum from frozen material.")
    SprayDrying = PermissibleValue(
        text="SprayDrying",
        description="Solution atomized into small particles before drying.")
    VacuumDrying = PermissibleValue(
        text="VacuumDrying",
        description="Moisture removed through low-pressure conditions.")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="DryingMethodEnum",
        description="Method used to remove moisture from a biocatalyst preparation.",
    )

class PhysicalStateFormEnum(EnumDefinitionImpl):
    """
    Physical state/formulation of a biocatalyst or component as applied.
    """
    Powder = PermissibleValue(
        text="Powder",
        meaning=PATO["0001736"])
    Liquid = PermissibleValue(
        text="Liquid",
        meaning=PATO["0001735"])
    Gaseous = PermissibleValue(
        text="Gaseous",
        meaning=PATO["0001737"])
    Suspension = PermissibleValue(text="Suspension")
    Other = PermissibleValue(text="Other")

    _defn = EnumDefinition(
        name="PhysicalStateFormEnum",
        description="Physical state/formulation of a biocatalyst or component as applied.",
    )

class KineticEquationTypeEnum(EnumDefinitionImpl):
    """
    The role a KineticEquation plays within a kinetic model (EnzymeML EquationType).
    """
    Assignment = PermissibleValue(
        text="Assignment",
        description="A variable is directly assigned the result of the equation.")
    InitialAssignment = PermissibleValue(
        text="InitialAssignment",
        description="The equation sets the initial value of a variable before simulation/integration starts.")
    ODE = PermissibleValue(
        text="ODE",
        description="""The equation is an ordinary differential equation describing the rate of change of a species or variable over time.""")
    RateLaw = PermissibleValue(
        text="RateLaw",
        description="""The equation describes the rate law of a BiocatalyticReaction (e.g. Michaelis-Menten kinetics).""")

    _defn = EnumDefinition(
        name="KineticEquationTypeEnum",
        description="The role a KineticEquation plays within a kinetic model (EnzymeML EquationType).",
    )

class MeasurementDataTypeEnum(EnumDefinitionImpl):
    """
    The physical/analytical nature of a raw measurement data series (EnzymeML DataTypes).
    """
    Absorbance = PermissibleValue(text="Absorbance")
    Amount = PermissibleValue(text="Amount")
    Concentration = PermissibleValue(text="Concentration")
    Conversion = PermissibleValue(text="Conversion")
    Fluorescence = PermissibleValue(text="Fluorescence")
    PeakArea = PermissibleValue(text="PeakArea")
    Transmittance = PermissibleValue(text="Transmittance")
    Turnover = PermissibleValue(text="Turnover")
    Yield = PermissibleValue(text="Yield")

    _defn = EnumDefinition(
        name="MeasurementDataTypeEnum",
        description="The physical/analytical nature of a raw measurement data series (EnzymeML DataTypes).",
    )

class DatasetThemes(EnumDefinitionImpl):

    AGRI = PermissibleValue(
        text="AGRI",
        description="Agriculture, fisheries, forestry and food",
        meaning=None)
    ECON = PermissibleValue(
        text="ECON",
        description="Economy and finance",
        meaning=None)
    EDUC = PermissibleValue(
        text="EDUC",
        description="Education, culture and sport",
        meaning=None)
    ENER = PermissibleValue(
        text="ENER",
        description="Energy",
        meaning=None)
    ENVI = PermissibleValue(
        text="ENVI",
        description="Environment",
        meaning=None)
    GOVE = PermissibleValue(
        text="GOVE",
        description="Government and public sector",
        meaning=None)
    HEAL = PermissibleValue(
        text="HEAL",
        description="Health",
        meaning=None)
    INTR = PermissibleValue(
        text="INTR",
        description="International issues",
        meaning=None)
    JUST = PermissibleValue(
        text="JUST",
        description="Justice, legal system and public safety",
        meaning=None)
    OP_DATPRO = PermissibleValue(
        text="OP_DATPRO",
        description="Provisional data",
        meaning=None)
    REGI = PermissibleValue(
        text="REGI",
        description="Regions and cities",
        meaning=None)
    SOCI = PermissibleValue(
        text="SOCI",
        description="Population and society",
        meaning=None)
    TECH = PermissibleValue(
        text="TECH",
        description="Science and technology",
        meaning=None)
    TRAN = PermissibleValue(
        text="TRAN",
        description="Transport",
        meaning=None)

    _defn = EnumDefinition(
        name="DatasetThemes",
    )

class TopLevelMediaTypes(EnumDefinitionImpl):

    application = PermissibleValue(text="application")
    audio = PermissibleValue(text="audio")
    example = PermissibleValue(text="example")
    font = PermissibleValue(text="font")
    haptics = PermissibleValue(text="haptics")
    image = PermissibleValue(text="image")
    message = PermissibleValue(text="message")
    model = PermissibleValue(text="model")
    multipart = PermissibleValue(text="multipart")
    text = PermissibleValue(text="text")
    video = PermissibleValue(text="video")

    _defn = EnumDefinition(
        name="TopLevelMediaTypes",
    )

class QUDTQuantityKindEnum(EnumDefinitionImpl):
    """
    Possible kinds of quantifiable attribute types provided as QUDT QualityKind instances.
    """
    _defn = EnumDefinition(
        name="QUDTQuantityKindEnum",
        description="Possible kinds of quantifiable attribute types provided as QUDT QualityKind instances.",
    )

class QUDTUnitEnum(EnumDefinitionImpl):
    """
    Possible kinds of QUDT unit instances.
    """
    _defn = EnumDefinition(
        name="QUDTUnitEnum",
        description="Possible kinds of QUDT unit instances.",
    )

class PhysicalStateEnum(EnumDefinitionImpl):

    SOLID = PermissibleValue(
        text="SOLID",
        description="A state of matter in which molecules are closely packed and cannot move past each other.",
        meaning=PATO["0001736"])
    LIQUID = PermissibleValue(
        text="LIQUID",
        description="""A state of matter with a definite volume but no fixed shape. Liquids adapt to the shape of their container and are nearly incompressible, maintaining their volume even under pressure.""",
        meaning=PATO["0001735"])
    GASEOUS = PermissibleValue(
        text="GASEOUS",
        description="A state of matter with neither fixed volume nor fixed shape.",
        meaning=PATO["0001737"])
    PLASMA = PermissibleValue(
        text="PLASMA",
        description="""A state of matter in which a gas becomes ionized and conducts electricity, often found in high-energy environments such as stars or lightning.""",
        meaning=PATO["0015012"])

    _defn = EnumDefinition(
        name="PhysicalStateEnum",
    )

# Slots
class slots:
    pass

slots.ec_number = Slot(uri=CHEMINF['000447'], name="ec_number", curie=CHEMINF.curie('000447'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ec_number, domain=None, range=Optional[Union[str, list[str]]])

slots.sequence_amino_acid = Slot(uri=SIO['010016'], name="sequence_amino_acid", curie=SIO.curie('010016'),
                   model_uri=STRENDCAT_BIOCATALYSIS.sequence_amino_acid, domain=None, range=Optional[Union[str, list[str]]])

slots.sequence_DNA = Slot(uri=SIO['010015'], name="sequence_DNA", curie=SIO.curie('010015'),
                   model_uri=STRENDCAT_BIOCATALYSIS.sequence_DNA, domain=None, range=Optional[Union[str, list[str]]])

slots.origin_organism = Slot(uri=SIO['010079'], name="origin_organism", curie=SIO.curie('010079'),
                   model_uri=STRENDCAT_BIOCATALYSIS.origin_organism, domain=None, range=Optional[Union[str, list[str]]])

slots.posttranslational_modification = Slot(uri=SIO['000008'], name="posttranslational_modification", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.posttranslational_modification, domain=None, range=Optional[Union[str, list[str]]])

slots.is_self_produced = Slot(uri=SIO['000008'], name="is_self_produced", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.is_self_produced, domain=None, range=Union[bool, Bool])

slots.has_biocatalyst_production_process = Slot(uri=PROV.wasGeneratedBy, name="has_biocatalyst_production_process", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_biocatalyst_production_process, domain=None, range=Optional[Union[dict, BiocatalystProductionProcess]])

slots.production_organism = Slot(uri=SIO['000008'], name="production_organism", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.production_organism, domain=None, range=Optional[Union[str, list[str]]])

slots.sequence_plasmid = Slot(uri=SIO['000008'], name="sequence_plasmid", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.sequence_plasmid, domain=None, range=Optional[Union[str, list[str]]])

slots.plasmid_specifications = Slot(uri=SIO['000008'], name="plasmid_specifications", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.plasmid_specifications, domain=None, range=Optional[Union[str, list[str]]])

slots.purification_method = Slot(uri=SIO['000008'], name="purification_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.purification_method, domain=None, range=Optional[Union[str, list[str]]])

slots.purity_specification = Slot(uri=SIO['000008'], name="purity_specification", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.purity_specification, domain=None, range=Optional[Union[str, list[str]]])

slots.has_purity = Slot(uri=SIO['000008'], name="has_purity", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_purity, domain=None, range=Optional[Union[Union[dict, Purity], list[Union[dict, Purity]]]])

slots.application_form = Slot(uri=SIO['000008'], name="application_form", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.application_form, domain=None, range=Union[str, "BiocatalystApplicationFormEnum"])

slots.has_activity = Slot(uri=SIO['000008'], name="has_activity", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_activity, domain=None, range=Optional[Union[Union[dict, SpecificActivity], list[Union[dict, SpecificActivity]]]])

slots.has_formulation = Slot(uri=SIO['000008'], name="has_formulation", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_formulation, domain=None, range=Optional[Union[str, list[str]]])

slots.had_drying_process = Slot(uri=PROV.wasGeneratedBy, name="had_drying_process", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.had_drying_process, domain=None, range=Optional[Union[dict, DryingProcess]])

slots.cell_disruption_process = Slot(uri=SIO['000008'], name="cell_disruption_process", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.cell_disruption_process, domain=None, range=Optional[Union[str, list[str]]])

slots.harvesting_method = Slot(uri=SIO['000008'], name="harvesting_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.harvesting_method, domain=None, range=Optional[Union[str, list[str]]])

slots.separation_method = Slot(uri=SIO['000008'], name="separation_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.separation_method, domain=None, range=Optional[Union[str, list[str]]])

slots.source_of_cellfree_extract = Slot(uri=SIO['000008'], name="source_of_cellfree_extract", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.source_of_cellfree_extract, domain=None, range=Optional[Union[str, list[str]]])

slots.concentration_determination_method = Slot(uri=SIO['000008'], name="concentration_determination_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.concentration_determination_method, domain=None, range=Optional[Union[str, list[str]]])

slots.activity_determination_method = Slot(uri=SIO['000008'], name="activity_determination_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.activity_determination_method, domain=None, range=Optional[Union[str, list[str]]])

slots.immobilisation_chemistry = Slot(uri=SIO['000008'], name="immobilisation_chemistry", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.immobilisation_chemistry, domain=None, range=Optional[Union[str, list[str]]])

slots.carrier_material = Slot(uri=SIO['000008'], name="carrier_material", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.carrier_material, domain=None, range=Optional[Union[str, list[str]]])

slots.linkers = Slot(uri=SIO['000008'], name="linkers", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.linkers, domain=None, range=Optional[Union[str, list[str]]])

slots.immobilisation_method = Slot(uri=SIO['000008'], name="immobilisation_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.immobilisation_method, domain=None, range=Optional[Union[str, list[str]]])

slots.storage_start = Slot(uri=DCTERMS.created, name="storage_start", curie=DCTERMS.curie('created'),
                   model_uri=STRENDCAT_BIOCATALYSIS.storage_start, domain=None, range=Optional[Union[str, XSDDate]])

slots.has_storage_additive = Slot(uri=BFO['0000051'], name="has_storage_additive", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_storage_additive, domain=None, range=Optional[Union[dict[Union[str, StorageAdditiveId], Union[dict, StorageAdditive]], list[Union[dict, StorageAdditive]]]])

slots.has_storage_conditions = Slot(uri=SIO['000008'], name="has_storage_conditions", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_storage_conditions, domain=None, range=Optional[Union[dict, StorageConditions]])

slots.drying_method_type = Slot(uri=OBI['0000011'], name="drying_method_type", curie=OBI.curie('0000011'),
                   model_uri=STRENDCAT_BIOCATALYSIS.drying_method_type, domain=None, range=Optional[Union[str, "DryingMethodEnum"]])

slots.has_component_role = Slot(uri=RO['0000087'], name="has_component_role", curie=RO.curie('0000087'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_component_role, domain=None, range=Optional[Union[str, "ComponentRoleEnum"]])

slots.has_solubility_limit = Slot(uri=SIO['000008'], name="has_solubility_limit", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_solubility_limit, domain=None, range=Optional[Union[Union[dict, SolubilityLimit], list[Union[dict, SolubilityLimit]]]])

slots.supplied_by = Slot(uri=PROV.wasAttributedTo, name="supplied_by", curie=PROV.curie('wasAttributedTo'),
                   model_uri=STRENDCAT_BIOCATALYSIS.supplied_by, domain=None, range=Optional[Union[dict, Agent]])

slots.has_reaction_medium = Slot(uri=SIO['000008'], name="has_reaction_medium", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_reaction_medium, domain=None, range=Optional[Union[dict, ReactionMedium]])

slots.has_phase_count = Slot(uri=SIO['000008'], name="has_phase_count", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_phase_count, domain=None, range=Optional[int])

slots.has_liquid_phase = Slot(uri=BFO['0000051'], name="has_liquid_phase", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_liquid_phase, domain=None, range=Optional[Union[dict[Union[str, LiquidPhaseId], Union[dict, LiquidPhase]], list[Union[dict, LiquidPhase]]]])

slots.has_solid_phase = Slot(uri=BFO['0000051'], name="has_solid_phase", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_solid_phase, domain=None, range=Optional[Union[dict[Union[str, SolidPhaseId], Union[dict, SolidPhase]], list[Union[dict, SolidPhase]]]])

slots.has_gas_phase = Slot(uri=BFO['0000051'], name="has_gas_phase", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_gas_phase, domain=None, range=Optional[Union[dict[Union[str, GasPhaseId], Union[dict, GasPhase]], list[Union[dict, GasPhase]]]])

slots.has_ionic_strength = Slot(uri=SIO['000008'], name="has_ionic_strength", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ionic_strength, domain=None, range=Optional[Union[Union[dict, IonicStrength], list[Union[dict, IonicStrength]]]])

slots.has_medium_additive = Slot(uri=BFO['0000051'], name="has_medium_additive", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_medium_additive, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]])

slots.has_liquid_type = Slot(uri=SIO['000008'], name="has_liquid_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_liquid_type, domain=None, range=Optional[Union[str, list[str]]])

slots.has_solid_type = Slot(uri=SIO['000008'], name="has_solid_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_solid_type, domain=None, range=Optional[Union[str, list[str]]])

slots.has_gas_type = Slot(uri=SIO['000008'], name="has_gas_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_gas_type, domain=None, range=Optional[Union[str, list[str]]])

slots.has_temperature_shift = Slot(uri=SIO['000008'], name="has_temperature_shift", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_temperature_shift, domain=None, range=Optional[Union[dict[Union[str, TemperatureShiftProcessId], Union[dict, TemperatureShiftProcess]], list[Union[dict, TemperatureShiftProcess]]]])

slots.has_temperature_gradient = Slot(uri=SIO['000008'], name="has_temperature_gradient", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_temperature_gradient, domain=None, range=Optional[Union[dict, TemperatureGradient]])

slots.has_ph_shift = Slot(uri=SIO['000008'], name="has_ph_shift", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_shift, domain=None, range=Optional[Union[dict[Union[str, PHShiftProcessId], Union[dict, PHShiftProcess]], list[Union[dict, PHShiftProcess]]]])

slots.has_ph_gradient = Slot(uri=SIO['000008'], name="has_ph_gradient", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_gradient, domain=None, range=Optional[Union[dict, PHGradient]])

slots.has_ph_measurement = Slot(uri=SIO['000008'], name="has_ph_measurement", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_measurement, domain=None, range=Optional[Union[dict, PHMeasurementProcess]])

slots.has_temperature_before = Slot(uri=SIO['000008'], name="has_temperature_before", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_temperature_before, domain=None, range=Optional[Union[Union[dict, Temperature], list[Union[dict, Temperature]]]])

slots.has_temperature_after = Slot(uri=SIO['000008'], name="has_temperature_after", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_temperature_after, domain=None, range=Optional[Union[Union[dict, Temperature], list[Union[dict, Temperature]]]])

slots.has_temperature_start = Slot(uri=SIO['000008'], name="has_temperature_start", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_temperature_start, domain=None, range=Optional[Union[Union[dict, Temperature], list[Union[dict, Temperature]]]])

slots.has_temperature_end = Slot(uri=SIO['000008'], name="has_temperature_end", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_temperature_end, domain=None, range=Optional[Union[Union[dict, Temperature], list[Union[dict, Temperature]]]])

slots.has_temperature_at_timepoint = Slot(uri=SIO['000008'], name="has_temperature_at_timepoint", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_temperature_at_timepoint, domain=None, range=Optional[Union[Union[dict, TemperatureTimepoint], list[Union[dict, TemperatureTimepoint]]]])

slots.has_trigger_event = Slot(uri=SIO['000008'], name="has_trigger_event", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_trigger_event, domain=None, range=Optional[Union[str, list[str]]])

slots.has_ph_before = Slot(uri=SIO['000008'], name="has_ph_before", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_before, domain=None, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.has_ph_after = Slot(uri=SIO['000008'], name="has_ph_after", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_after, domain=None, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.has_ph_start = Slot(uri=SIO['000008'], name="has_ph_start", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_start, domain=None, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.has_ph_end = Slot(uri=SIO['000008'], name="has_ph_end", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_end, domain=None, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.has_ph_at_timepoint = Slot(uri=SIO['000008'], name="has_ph_at_timepoint", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_at_timepoint, domain=None, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.has_gradient_length = Slot(uri=SIO['000008'], name="has_gradient_length", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_gradient_length, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.has_measurement_points = Slot(uri=SIO['000008'], name="has_measurement_points", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_measurement_points, domain=None, range=Optional[Union[str, list[str]]])

slots.detected_when = Slot(uri=SIO['000008'], name="detected_when", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.detected_when, domain=None, range=Optional[Union[str, list[str]]])

slots.detected_how = Slot(uri=SIO['000008'], name="detected_how", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.detected_how, domain=None, range=Optional[Union[str, list[str]]])

slots.has_calibration_info = Slot(uri=SIO['000008'], name="has_calibration_info", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_calibration_info, domain=None, range=Optional[Union[str, list[str]]])

slots.has_time_value = Slot(uri=SIO['000008'], name="has_time_value", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_time_value, domain=None, range=Optional[Union[float, list[float]]])

slots.time_unit = Slot(uri=SIO['000008'], name="time_unit", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.time_unit, domain=None, range=Optional[Union[str, list[str]]])

slots.reactor_material = Slot(uri=SIO['000008'], name="reactor_material", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.reactor_material, domain=None, range=Optional[Union[str, list[str]]])

slots.bottom_type = Slot(uri=SIO['000008'], name="bottom_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.bottom_type, domain=None, range=Optional[Union[str, list[str]]])

slots.reactor_type_description = Slot(uri=SIO['000008'], name="reactor_type_description", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.reactor_type_description, domain=None, range=Optional[Union[str, list[str]]])

slots.tubing = Slot(uri=SIO['000008'], name="tubing", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.tubing, domain=None, range=Optional[Union[str, list[str]]])

slots.has_flow_rate = Slot(uri=SIO['000008'], name="has_flow_rate", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_flow_rate, domain=None, range=Optional[Union[Union[dict, FlowRate], list[Union[dict, FlowRate]]]])

slots.has_catalyst_localisation = Slot(uri=SIO['000008'], name="has_catalyst_localisation", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_catalyst_localisation, domain=None, range=Optional[Union[str, list[str]]])

slots.has_residence_time = Slot(uri=SIO['000008'], name="has_residence_time", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_residence_time, domain=None, range=Optional[Union[Union[dict, ResidenceTime], list[Union[dict, ResidenceTime]]]])

slots.has_reynolds_number = Slot(uri=SIO['000008'], name="has_reynolds_number", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_reynolds_number, domain=None, range=Optional[Union[str, list[str]]])

slots.has_passive_mixing = Slot(uri=SIO['000008'], name="has_passive_mixing", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_passive_mixing, domain=None, range=Optional[Union[str, list[str]]])

slots.has_active_mixer = Slot(uri=SIO['000008'], name="has_active_mixer", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_active_mixer, domain=None, range=Optional[Union[str, list[str]]])

slots.has_pulsing_description = Slot(uri=SIO['000008'], name="has_pulsing_description", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_pulsing_description, domain=None, range=Optional[Union[str, list[str]]])

slots.vial_size_unit = Slot(uri=SIO['000008'], name="vial_size_unit", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.vial_size_unit, domain=None, range=Optional[Union[str, list[str]]])

slots.vial_material = Slot(uri=SIO['000008'], name="vial_material", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.vial_material, domain=None, range=Optional[Union[str, list[str]]])

slots.closure_type = Slot(uri=SIO['000008'], name="closure_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.closure_type, domain=None, range=Optional[Union[str, list[str]]])

slots.plate_type = Slot(uri=SIO['000008'], name="plate_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.plate_type, domain=None, range=Optional[Union[str, list[str]]])

slots.plate_material = Slot(uri=SIO['000008'], name="plate_material", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.plate_material, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_wells = Slot(uri=SIO['000008'], name="number_of_wells", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.number_of_wells, domain=None, range=Optional[int])

slots.well_shape = Slot(uri=SIO['000008'], name="well_shape", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.well_shape, domain=None, range=Optional[Union[str, list[str]]])

slots.well_volume = Slot(uri=SIO['000008'], name="well_volume", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.well_volume, domain=None, range=Optional[Union[Union[dict, Volume], list[Union[dict, Volume]]]])

slots.well_arrangement = Slot(uri=SIO['000008'], name="well_arrangement", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.well_arrangement, domain=None, range=Optional[Union[str, list[str]]])

slots.sealing_method = Slot(uri=SIO['000008'], name="sealing_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.sealing_method, domain=None, range=Optional[Union[str, list[str]]])

slots.sealing_material = Slot(uri=SIO['000008'], name="sealing_material", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.sealing_material, domain=None, range=Optional[Union[str, list[str]]])

slots.stirring_type = Slot(uri=SIO['000008'], name="stirring_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stirring_type, domain=None, range=Optional[Union[str, list[str]]])

slots.stirrer_material = Slot(uri=SIO['000008'], name="stirrer_material", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stirrer_material, domain=None, range=Optional[Union[str, list[str]]])

slots.number_of_stirrers = Slot(uri=SIO['000008'], name="number_of_stirrers", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.number_of_stirrers, domain=None, range=Optional[int])

slots.distance_between_stirrers = Slot(uri=SIO['000008'], name="distance_between_stirrers", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.distance_between_stirrers, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.blade_pitch_angle = Slot(uri=SIO['000008'], name="blade_pitch_angle", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.blade_pitch_angle, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.number_of_blades = Slot(uri=SIO['000008'], name="number_of_blades", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.number_of_blades, domain=None, range=Optional[int])

slots.blade_size = Slot(uri=SIO['000008'], name="blade_size", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.blade_size, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.stirrer_geometry = Slot(uri=SIO['000008'], name="stirrer_geometry", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stirrer_geometry, domain=None, range=Optional[Union[str, list[str]]])

slots.stirrer_speed = Slot(uri=SIO['000008'], name="stirrer_speed", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stirrer_speed, domain=None, range=Optional[Union[Union[dict, AngularVelocity], list[Union[dict, AngularVelocity]]]])

slots.height_above_vessel_base = Slot(uri=SIO['000008'], name="height_above_vessel_base", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.height_above_vessel_base, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.power_per_volume_input = Slot(uri=SIO['000008'], name="power_per_volume_input", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.power_per_volume_input, domain=None, range=Optional[Union[Union[dict, PowerPerVolume], list[Union[dict, PowerPerVolume]]]])

slots.stir_bar_size = Slot(uri=SIO['000008'], name="stir_bar_size", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stir_bar_size, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.stir_bar_shape = Slot(uri=SIO['000008'], name="stir_bar_shape", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stir_bar_shape, domain=None, range=Optional[Union[str, list[str]]])

slots.shaking_type = Slot(uri=SIO['000008'], name="shaking_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.shaking_type, domain=None, range=Optional[Union[str, list[str]]])

slots.deflection = Slot(uri=SIO['000008'], name="deflection", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.deflection, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.shaking_speed = Slot(uri=SIO['000008'], name="shaking_speed", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.shaking_speed, domain=None, range=Optional[Union[Union[dict, AngularVelocity], list[Union[dict, AngularVelocity]]]])

slots.shaking_position = Slot(uri=SIO['000008'], name="shaking_position", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.shaking_position, domain=None, range=Optional[Union[str, list[str]]])

slots.gas_supply_method = Slot(uri=SIO['000008'], name="gas_supply_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.gas_supply_method, domain=None, range=Optional[Union[str, list[str]]])

slots.temperature_control_method = Slot(uri=SIO['000008'], name="temperature_control_method", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.temperature_control_method, domain=None, range=Optional[Union[str, list[str]]])

slots.has_sample_volume = Slot(uri=SIO['000008'], name="has_sample_volume", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_sample_volume, domain=None, range=Optional[Union[Union[dict, Volume], list[Union[dict, Volume]]]])

slots.has_sampling_timepoint = Slot(uri=SIO['000008'], name="has_sampling_timepoint", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_sampling_timepoint, domain=None, range=Optional[Union[Union[dict, SamplingTimepoint], list[Union[dict, SamplingTimepoint]]]])

slots.mixing_during_sampling = Slot(uri=SIO['000008'], name="mixing_during_sampling", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.mixing_during_sampling, domain=None, range=Optional[Union[bool, Bool]])

slots.vessel_opened_for_sampling = Slot(uri=SIO['000008'], name="vessel_opened_for_sampling", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.vessel_opened_for_sampling, domain=None, range=Optional[Union[bool, Bool]])

slots.sampled_from_phase = Slot(uri=SIO['000008'], name="sampled_from_phase", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.sampled_from_phase, domain=None, range=Optional[Union[dict[Union[str, MaterialEntityId], Union[dict, MaterialEntity]], list[Union[dict, MaterialEntity]]]])

slots.biocatalyst_contamination_possible = Slot(uri=SIO['000008'], name="biocatalyst_contamination_possible", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.biocatalyst_contamination_possible, domain=None, range=Optional[Union[bool, Bool]])

slots.quenching_method_type = Slot(uri=SIO['000008'], name="quenching_method_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.quenching_method_type, domain=None, range=Optional[Union[str, list[str]]])

slots.has_quenching_ratio = Slot(uri=SIO['000008'], name="has_quenching_ratio", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_quenching_ratio, domain=None, range=Optional[Union[Union[dict, QuenchingRatio], list[Union[dict, QuenchingRatio]]]])

slots.has_kinetic_parameters = Slot(uri=SIO['000008'], name="has_kinetic_parameters", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_kinetic_parameters, domain=None, range=Optional[Union[Union[dict, KineticParameters], list[Union[dict, KineticParameters]]]])

slots.has_yield_and_conversion = Slot(uri=SIO['000008'], name="has_yield_and_conversion", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_yield_and_conversion, domain=None, range=Optional[Union[Union[dict, YieldAndConversion], list[Union[dict, YieldAndConversion]]]])

slots.has_activity_and_reaction_rate = Slot(uri=SIO['000008'], name="has_activity_and_reaction_rate", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_activity_and_reaction_rate, domain=None, range=Optional[Union[Union[dict, ActivityAndInitialReactionRate], list[Union[dict, ActivityAndInitialReactionRate]]]])

slots.has_selectivity_and_specificity = Slot(uri=SIO['000008'], name="has_selectivity_and_specificity", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_selectivity_and_specificity, domain=None, range=Optional[Union[Union[dict, SelectivityAndSpecificity], list[Union[dict, SelectivityAndSpecificity]]]])

slots.has_thermodynamic_parameters = Slot(uri=SIO['000008'], name="has_thermodynamic_parameters", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_thermodynamic_parameters, domain=None, range=Optional[Union[Union[dict, ThermodynamicParameters], list[Union[dict, ThermodynamicParameters]]]])

slots.has_michaelis_constant = Slot(uri=SIO['000008'], name="has_michaelis_constant", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_michaelis_constant, domain=None, range=Optional[Union[Union[dict, MichaelisConstant], list[Union[dict, MichaelisConstant]]]])

slots.has_maximum_reaction_rate = Slot(uri=SIO['000008'], name="has_maximum_reaction_rate", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_maximum_reaction_rate, domain=None, range=Optional[Union[Union[dict, MaximumReactionRate], list[Union[dict, MaximumReactionRate]]]])

slots.has_turnover_number = Slot(uri=SIO['000008'], name="has_turnover_number", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_turnover_number, domain=None, range=Optional[Union[Union[dict, TurnoverNumber], list[Union[dict, TurnoverNumber]]]])

slots.has_catalytic_efficiency = Slot(uri=SIO['000008'], name="has_catalytic_efficiency", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_catalytic_efficiency, domain=None, range=Optional[Union[Union[dict, CatalyticEfficiency], list[Union[dict, CatalyticEfficiency]]]])

slots.has_dissociation_constant = Slot(uri=SIO['000008'], name="has_dissociation_constant", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_dissociation_constant, domain=None, range=Optional[Union[Union[dict, DissociationConstant], list[Union[dict, DissociationConstant]]]])

slots.has_hill_coefficient = Slot(uri=SIO['000008'], name="has_hill_coefficient", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_hill_coefficient, domain=None, range=Optional[Union[Union[dict, HillCoefficient], list[Union[dict, HillCoefficient]]]])

slots.has_inhibition_characterisation = Slot(uri=SIO['000008'], name="has_inhibition_characterisation", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_inhibition_characterisation, domain=None, range=Optional[Union[Union[dict, EnzymeInhibitionCharacterisation], list[Union[dict, EnzymeInhibitionCharacterisation]]]])

slots.has_enzyme_stability = Slot(uri=SIO['000008'], name="has_enzyme_stability", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_enzyme_stability, domain=None, range=Optional[Union[Union[dict, EnzymeStabilityCharacterisation], list[Union[dict, EnzymeStabilityCharacterisation]]]])

slots.inhibition_type = Slot(uri=SIO['000008'], name="inhibition_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.inhibition_type, domain=None, range=Optional[Union[str, "InhibitionTypeEnum"]])

slots.has_inhibition_constant = Slot(uri=SIO['000008'], name="has_inhibition_constant", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_inhibition_constant, domain=None, range=Optional[Union[Union[dict, InhibitionConstant], list[Union[dict, InhibitionConstant]]]])

slots.has_half_life = Slot(uri=SIO['000008'], name="has_half_life", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_half_life, domain=None, range=Optional[Union[Union[dict, HalfLife], list[Union[dict, HalfLife]]]])

slots.stability_description = Slot(uri=SIO['000008'], name="stability_description", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stability_description, domain=None, range=Optional[Union[str, list[str]]])

slots.has_space_time_yield = Slot(uri=SIO['000008'], name="has_space_time_yield", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_space_time_yield, domain=None, range=Optional[Union[Union[dict, SpaceTimeYield], list[Union[dict, SpaceTimeYield]]]])

slots.has_substrate_conversion = Slot(uri=SIO['000008'], name="has_substrate_conversion", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_substrate_conversion, domain=None, range=Optional[Union[Union[dict, SubstrateConversion], list[Union[dict, SubstrateConversion]]]])

slots.has_specific_activity = Slot(uri=SIO['000008'], name="has_specific_activity", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_specific_activity, domain=None, range=Optional[Union[Union[dict, SpecificActivity], list[Union[dict, SpecificActivity]]]])

slots.has_initial_reaction_rate = Slot(uri=SIO['000008'], name="has_initial_reaction_rate", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_initial_reaction_rate, domain=None, range=Optional[Union[Union[dict, InitialReactionRate], list[Union[dict, InitialReactionRate]]]])

slots.has_enantioselectivity_ratio = Slot(uri=SIO['000008'], name="has_enantioselectivity_ratio", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_enantioselectivity_ratio, domain=None, range=Optional[Union[Union[dict, EnantioselectivityRatio], list[Union[dict, EnantioselectivityRatio]]]])

slots.has_enantiomeric_excess = Slot(uri=SIO['000008'], name="has_enantiomeric_excess", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_enantiomeric_excess, domain=None, range=Optional[Union[Union[dict, EnantiomericExcess], list[Union[dict, EnantiomericExcess]]]])

slots.has_diastereomeric_excess = Slot(uri=SIO['000008'], name="has_diastereomeric_excess", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_diastereomeric_excess, domain=None, range=Optional[Union[Union[dict, DiastereomericExcess], list[Union[dict, DiastereomericExcess]]]])

slots.has_isomeric_content = Slot(uri=SIO['000008'], name="has_isomeric_content", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_isomeric_content, domain=None, range=Optional[Union[Union[dict, IsomericContent], list[Union[dict, IsomericContent]]]])

slots.stereoselectivity_description = Slot(uri=SIO['000008'], name="stereoselectivity_description", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stereoselectivity_description, domain=None, range=Optional[Union[str, list[str]]])

slots.chemoselectivity_description = Slot(uri=SIO['000008'], name="chemoselectivity_description", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.chemoselectivity_description, domain=None, range=Optional[Union[str, list[str]]])

slots.regioselectivity_description = Slot(uri=SIO['000008'], name="regioselectivity_description", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.regioselectivity_description, domain=None, range=Optional[Union[str, list[str]]])

slots.has_gibbs_free_energy_change = Slot(uri=SIO['000008'], name="has_gibbs_free_energy_change", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_gibbs_free_energy_change, domain=None, range=Optional[Union[Union[dict, GibbsFreeEnergyChange], list[Union[dict, GibbsFreeEnergyChange]]]])

slots.has_enthalpy_change = Slot(uri=SIO['000008'], name="has_enthalpy_change", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_enthalpy_change, domain=None, range=Optional[Union[Union[dict, EnthalpyChange], list[Union[dict, EnthalpyChange]]]])

slots.has_operation_mode = Slot(uri=DCTERMS.type, name="has_operation_mode", curie=DCTERMS.curie('type'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_operation_mode, domain=None, range=Union[str, "OperationModeEnum"])

slots.used_biocatalyst_preparation = Slot(uri=PROV.used, name="used_biocatalyst_preparation", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.used_biocatalyst_preparation, domain=None, range=Optional[Union[dict[Union[str, BiocatalystPreparationId], Union[dict, BiocatalystPreparation]], list[Union[dict, BiocatalystPreparation]]]])

slots.has_biocatalytic_component = Slot(uri=PROV.used, name="has_biocatalytic_component", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_biocatalytic_component, domain=None, range=Optional[Union[dict[Union[str, BiocatalyticComponentId], Union[dict, BiocatalyticComponent]], list[Union[dict, BiocatalyticComponent]]]])

slots.used_reaction_vessel = Slot(uri=PROV.wasAssociatedWith, name="used_reaction_vessel", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=STRENDCAT_BIOCATALYSIS.used_reaction_vessel, domain=None, range=Optional[Union[dict[Union[str, ReactionVesselId], Union[dict, ReactionVessel]], list[Union[dict, ReactionVessel]]]])

slots.has_sampling_process = Slot(uri=BFO['0000051'], name="has_sampling_process", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_sampling_process, domain=None, range=Optional[Union[dict[Union[str, SamplingProcessId], Union[dict, SamplingProcess]], list[Union[dict, SamplingProcess]]]])

slots.has_enzyme_measurement = Slot(uri=BFO['0000051'], name="has_enzyme_measurement", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_enzyme_measurement, domain=None, range=Optional[Union[dict[Union[str, EnzymeMeasurementId], Union[dict, EnzymeMeasurement]], list[Union[dict, EnzymeMeasurement]]]])

slots.has_molecular_complex = Slot(uri=PROV.used, name="has_molecular_complex", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_molecular_complex, domain=None, range=Optional[Union[dict[Union[str, MolecularComplexId], Union[dict, MolecularComplex]], list[Union[dict, MolecularComplex]]]])

slots.molecular_weight = Slot(uri=SIO['000119'], name="molecular_weight", curie=SIO.curie('000119'),
                   model_uri=STRENDCAT_BIOCATALYSIS.molecular_weight, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.was_processed_by = Slot(uri=PROV.wasGeneratedBy, name="was_processed_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.was_processed_by, domain=None, range=Optional[Union[dict, SamplePreparationProcess]])

slots.given_name = Slot(uri=SCHEMA.givenName, name="given_name", curie=SCHEMA.curie('givenName'),
                   model_uri=STRENDCAT_BIOCATALYSIS.given_name, domain=None, range=Optional[Union[str, list[str]]])

slots.family_name = Slot(uri=SCHEMA.familyName, name="family_name", curie=SCHEMA.curie('familyName'),
                   model_uri=STRENDCAT_BIOCATALYSIS.family_name, domain=None, range=Optional[Union[str, list[str]]])

slots.mail = Slot(uri=SCHEMA.email, name="mail", curie=SCHEMA.curie('email'),
                   model_uri=STRENDCAT_BIOCATALYSIS.mail, domain=None, range=Optional[Union[str, list[str]]])

slots.has_complex_participant = Slot(uri=BFO['0000051'], name="has_complex_participant", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_complex_participant, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]])

slots.has_constant_concentration = Slot(uri=SIO['000008'], name="has_constant_concentration", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_constant_concentration, domain=None, range=Optional[Union[bool, Bool]])

slots.has_constant_volume = Slot(uri=SIO['000008'], name="has_constant_volume", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_constant_volume, domain=None, range=Optional[Union[bool, Bool]])

slots.equation_species_reference = Slot(uri=SIO['000008'], name="equation_species_reference", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.equation_species_reference, domain=None, range=Optional[Union[str, list[str]]])

slots.equation_type = Slot(uri=SIO['000008'], name="equation_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.equation_type, domain=None, range=Optional[Union[str, "KineticEquationTypeEnum"]])

slots.has_equation_variable = Slot(uri=SIO['000008'], name="has_equation_variable", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_equation_variable, domain=None, range=Optional[Union[Union[dict, EquationVariable], list[Union[dict, EquationVariable]]]])

slots.has_kinetic_equation = Slot(uri=SIO['000008'], name="has_kinetic_equation", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_kinetic_equation, domain=None, range=Optional[Union[Union[dict, KineticEquation], list[Union[dict, KineticEquation]]]])

slots.has_kinetic_model_parameter = Slot(uri=SIO['000008'], name="has_kinetic_model_parameter", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_kinetic_model_parameter, domain=None, range=Optional[Union[Union[dict, KineticModelParameter], list[Union[dict, KineticModelParameter]]]])

slots.parameter_symbol = Slot(uri=SIO['000008'], name="parameter_symbol", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.parameter_symbol, domain=None, range=Optional[Union[str, list[str]]])

slots.initial_value = Slot(uri=SIO['000008'], name="initial_value", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.initial_value, domain=None, range=Optional[float])

slots.upper_bound = Slot(uri=SIO['000008'], name="upper_bound", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.upper_bound, domain=None, range=Optional[float])

slots.lower_bound = Slot(uri=SIO['000008'], name="lower_bound", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.lower_bound, domain=None, range=Optional[float])

slots.stderr = Slot(uri=SIO['000008'], name="stderr", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.stderr, domain=None, range=Optional[float])

slots.is_fitted = Slot(uri=SIO['000008'], name="is_fitted", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.is_fitted, domain=None, range=Optional[Union[bool, Bool]])

slots.is_fixed_parameter = Slot(uri=SIO['000008'], name="is_fixed_parameter", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.is_fixed_parameter, domain=None, range=Optional[Union[bool, Bool]])

slots.is_reversible = Slot(uri=SIO['000008'], name="is_reversible", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.is_reversible, domain=None, range=Optional[Union[bool, Bool]])

slots.organism_taxonomy_id = Slot(uri=SIO['000008'], name="organism_taxonomy_id", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.organism_taxonomy_id, domain=None, range=Optional[Union[str, list[str]]])

slots.measurement_group_id = Slot(uri=SIO['000008'], name="measurement_group_id", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.measurement_group_id, domain=None, range=Optional[Union[str, list[str]]])

slots.has_measurement_species_data = Slot(uri=BFO['0000051'], name="has_measurement_species_data", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_measurement_species_data, domain=None, range=Optional[Union[Union[dict, EnzymeMeasurementSpeciesData], list[Union[dict, EnzymeMeasurementSpeciesData]]]])

slots.measured_species_reference = Slot(uri=SIO['000008'], name="measured_species_reference", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.measured_species_reference, domain=None, range=Optional[Union[str, list[str]]])

slots.prepared_amount = Slot(uri=SIO['000008'], name="prepared_amount", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.prepared_amount, domain=None, range=Optional[float])

slots.initial_amount = Slot(uri=SIO['000008'], name="initial_amount", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.initial_amount, domain=None, range=Optional[float])

slots.measurement_data_type = Slot(uri=SIO['000008'], name="measurement_data_type", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.measurement_data_type, domain=None, range=Optional[Union[str, "MeasurementDataTypeEnum"]])

slots.is_simulated = Slot(uri=SIO['000008'], name="is_simulated", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.is_simulated, domain=None, range=Optional[Union[bool, Bool]])

slots.has_timepoint = Slot(uri=BFO['0000051'], name="has_timepoint", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_timepoint, domain=None, range=Optional[Union[Union[dict, MeasurementTimepoint], list[Union[dict, MeasurementTimepoint]]]])

slots.synonymous_names = Slot(uri=SIO['000008'], name="synonymous_names", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.synonymous_names, domain=None, range=Optional[Union[str, list[str]]])

slots.access_URL = Slot(uri=DCAT.accessURL, name="access_URL", curie=DCAT.curie('accessURL'),
                   model_uri=STRENDCAT_BIOCATALYSIS.access_URL, domain=None, range=Optional[str])

slots.access_rights = Slot(uri=DCTERMS.accessRights, name="access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=STRENDCAT_BIOCATALYSIS.access_rights, domain=None, range=Optional[str])

slots.access_service = Slot(uri=DCAT.accessService, name="access_service", curie=DCAT.curie('accessService'),
                   model_uri=STRENDCAT_BIOCATALYSIS.access_service, domain=None, range=Optional[str])

slots.algorithm = Slot(uri=SPDX.algorithm, name="algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=STRENDCAT_BIOCATALYSIS.algorithm, domain=None, range=Optional[str])

slots.applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.applicable_legislation, domain=None, range=Optional[str])

slots.application_profile = Slot(uri=DCTERMS.conformsTo, name="application_profile", curie=DCTERMS.curie('conformsTo'),
                   model_uri=STRENDCAT_BIOCATALYSIS.application_profile, domain=None, range=Optional[str])

slots.availability = Slot(uri=DCATAP.availability, name="availability", curie=DCATAP.curie('availability'),
                   model_uri=STRENDCAT_BIOCATALYSIS.availability, domain=None, range=Optional[str])

slots.bbox = Slot(uri=DCAT.bbox, name="bbox", curie=DCAT.curie('bbox'),
                   model_uri=STRENDCAT_BIOCATALYSIS.bbox, domain=None, range=Optional[str])

slots.beginning = Slot(uri=TIME.hasBeginning, name="beginning", curie=TIME.curie('hasBeginning'),
                   model_uri=STRENDCAT_BIOCATALYSIS.beginning, domain=None, range=Optional[str])

slots.byte_size = Slot(uri=DCAT.byteSize, name="byte_size", curie=DCAT.curie('byteSize'),
                   model_uri=STRENDCAT_BIOCATALYSIS.byte_size, domain=None, range=Optional[str])

slots.carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=STRENDCAT_BIOCATALYSIS.carried_out_by, domain=None, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, AgenticEntity]], list[Union[dict, AgenticEntity]]]])

slots.catalogue = Slot(uri=DCAT.catalog, name="catalogue", curie=DCAT.curie('catalog'),
                   model_uri=STRENDCAT_BIOCATALYSIS.catalogue, domain=None, range=Optional[str])

slots.centroid = Slot(uri=DCAT.centroid, name="centroid", curie=DCAT.curie('centroid'),
                   model_uri=STRENDCAT_BIOCATALYSIS.centroid, domain=None, range=Optional[str])

slots.change_type = Slot(uri=ADMS.status, name="change_type", curie=ADMS.curie('status'),
                   model_uri=STRENDCAT_BIOCATALYSIS.change_type, domain=None, range=Optional[str])

slots.checksum = Slot(uri=SPDX.checksum, name="checksum", curie=SPDX.curie('checksum'),
                   model_uri=STRENDCAT_BIOCATALYSIS.checksum, domain=None, range=Optional[str])

slots.checksum_value = Slot(uri=SPDX.checksumValue, name="checksum_value", curie=SPDX.curie('checksumValue'),
                   model_uri=STRENDCAT_BIOCATALYSIS.checksum_value, domain=None, range=Optional[str])

slots.compression_format = Slot(uri=DCAT.compressFormat, name="compression_format", curie=DCAT.curie('compressFormat'),
                   model_uri=STRENDCAT_BIOCATALYSIS.compression_format, domain=None, range=Optional[str])

slots.conforms_to = Slot(uri=DCTERMS.conformsTo, name="conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=STRENDCAT_BIOCATALYSIS.conforms_to, domain=None, range=Optional[str])

slots.contact_point = Slot(uri=DCAT.contactPoint, name="contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=STRENDCAT_BIOCATALYSIS.contact_point, domain=None, range=Optional[str])

slots.creator = Slot(uri=DCTERMS.creator, name="creator", curie=DCTERMS.curie('creator'),
                   model_uri=STRENDCAT_BIOCATALYSIS.creator, domain=None, range=Optional[str])

slots.dataset_distribution = Slot(uri=DCAT.distribution, name="dataset_distribution", curie=DCAT.curie('distribution'),
                   model_uri=STRENDCAT_BIOCATALYSIS.dataset_distribution, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.description, domain=None, range=Optional[str])

slots.documentation = Slot(uri=FOAF.page, name="documentation", curie=FOAF.curie('page'),
                   model_uri=STRENDCAT_BIOCATALYSIS.documentation, domain=None, range=Optional[str])

slots.download_URL = Slot(uri=DCAT.downloadURL, name="download_URL", curie=DCAT.curie('downloadURL'),
                   model_uri=STRENDCAT_BIOCATALYSIS.download_URL, domain=None, range=Optional[str])

slots.end = Slot(uri=TIME.hasEnd, name="end", curie=TIME.curie('hasEnd'),
                   model_uri=STRENDCAT_BIOCATALYSIS.end, domain=None, range=Optional[str])

slots.end_date = Slot(uri=DCAT.endDate, name="end_date", curie=DCAT.curie('endDate'),
                   model_uri=STRENDCAT_BIOCATALYSIS.end_date, domain=None, range=Optional[str])

slots.endpoint_URL = Slot(uri=DCAT.endpointURL, name="endpoint_URL", curie=DCAT.curie('endpointURL'),
                   model_uri=STRENDCAT_BIOCATALYSIS.endpoint_URL, domain=None, range=Optional[str])

slots.endpoint_description = Slot(uri=DCAT.endpointDescription, name="endpoint_description", curie=DCAT.curie('endpointDescription'),
                   model_uri=STRENDCAT_BIOCATALYSIS.endpoint_description, domain=None, range=Optional[str])

slots.evaluated_activity = Slot(uri=PROV.wasInformedBy, name="evaluated_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.evaluated_activity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, EvaluatedActivity]], list[Union[dict, EvaluatedActivity]]]])

slots.evaluated_entity = Slot(uri=PROV.used, name="evaluated_entity", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.evaluated_entity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, EvaluatedEntity]], list[Union[dict, EvaluatedEntity]]]])

slots.format = Slot(uri=DCTERMS.format, name="format", curie=DCTERMS.curie('format'),
                   model_uri=STRENDCAT_BIOCATALYSIS.format, domain=None, range=Optional[str])

slots.frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=STRENDCAT_BIOCATALYSIS.frequency, domain=None, range=Optional[str])

slots.geographical_coverage = Slot(uri=DCTERMS.spatial, name="geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=STRENDCAT_BIOCATALYSIS.geographical_coverage, domain=None, range=Optional[str])

slots.geometry = Slot(uri=LOCN.geometry, name="geometry", curie=LOCN.curie('geometry'),
                   model_uri=STRENDCAT_BIOCATALYSIS.geometry, domain=None, range=Optional[str])

slots.had_input_activity = Slot(uri=PROV.wasInformedBy, name="had_input_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.had_input_activity, domain=None, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]])

slots.had_input_entity = Slot(uri=PROV.used, name="had_input_entity", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.had_input_entity, domain=None, range=Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]])

slots.had_output_entity = Slot(uri=PROV.generated, name="had_output_entity", curie=PROV.curie('generated'),
                   model_uri=STRENDCAT_BIOCATALYSIS.had_output_entity, domain=None, range=Optional[Union[dict[Union[str, EntityId], Union[dict, Entity]], list[Union[dict, Entity]]]])

slots.had_role = Slot(uri=DCAT.hadRole, name="had_role", curie=DCAT.curie('hadRole'),
                   model_uri=STRENDCAT_BIOCATALYSIS.had_role, domain=None, range=Optional[str])

slots.has_dataset = Slot(uri=DCAT.dataset, name="has_dataset", curie=DCAT.curie('dataset'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_dataset, domain=None, range=Optional[str])

slots.has_part = Slot(uri=DCTERMS.hasPart, name="has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_part, domain=None, range=Optional[Union[str, ActivityId]])

slots.has_policy = Slot(uri=ODRL.hasPolicy, name="has_policy", curie=ODRL.curie('hasPolicy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_policy, domain=None, range=Optional[str])

slots.has_qualitative_attribute = Slot(uri=DCTERMS.relation, name="has_qualitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_qualitative_attribute, domain=None, range=Optional[Union[Union[dict, QualitativeAttribute], list[Union[dict, QualitativeAttribute]]]])

slots.has_quantitative_attribute = Slot(uri=DCTERMS.relation, name="has_quantitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_quantitative_attribute, domain=None, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.has_version = Slot(uri=DCAT.hasVersion, name="has_version", curie=DCAT.curie('hasVersion'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_version, domain=None, range=Optional[str])

slots.homepage = Slot(uri=FOAF.homepage, name="homepage", curie=FOAF.curie('homepage'),
                   model_uri=STRENDCAT_BIOCATALYSIS.homepage, domain=None, range=Optional[str])

slots.id = Slot(uri=DCATAP_PLUS.id, name="id", curie=DCATAP_PLUS.curie('id'),
                   model_uri=STRENDCAT_BIOCATALYSIS.id, domain=None, range=URIRef)

slots.identifier = Slot(uri=DCTERMS.identifier, name="identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.identifier, domain=None, range=Optional[str])

slots.in_series = Slot(uri=DCAT.inSeries, name="in_series", curie=DCAT.curie('inSeries'),
                   model_uri=STRENDCAT_BIOCATALYSIS.in_series, domain=None, range=Optional[str])

slots.is_about_activity = Slot(uri=DCTERMS.subject, name="is_about_activity", curie=DCTERMS.curie('subject'),
                   model_uri=STRENDCAT_BIOCATALYSIS.is_about_activity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedActivityId], Union[dict, EvaluatedActivity]], list[Union[dict, EvaluatedActivity]]]])

slots.is_about_entity = Slot(uri=DCTERMS.subject, name="is_about_entity", curie=DCTERMS.curie('subject'),
                   model_uri=STRENDCAT_BIOCATALYSIS.is_about_entity, domain=None, range=Optional[Union[dict[Union[str, EvaluatedEntityId], Union[dict, EvaluatedEntity]], list[Union[dict, EvaluatedEntity]]]])

slots.is_referenced_by = Slot(uri=DCTERMS.isReferencedBy, name="is_referenced_by", curie=DCTERMS.curie('isReferencedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.is_referenced_by, domain=None, range=Optional[str])

slots.keyword = Slot(uri=DCAT.keyword, name="keyword", curie=DCAT.curie('keyword'),
                   model_uri=STRENDCAT_BIOCATALYSIS.keyword, domain=None, range=Optional[str])

slots.landing_page = Slot(uri=DCAT.landingPage, name="landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=STRENDCAT_BIOCATALYSIS.landing_page, domain=None, range=Optional[str])

slots.language = Slot(uri=DCTERMS.language, name="language", curie=DCTERMS.curie('language'),
                   model_uri=STRENDCAT_BIOCATALYSIS.language, domain=None, range=Optional[str])

slots.licence = Slot(uri=DCTERMS.license, name="licence", curie=DCTERMS.curie('license'),
                   model_uri=STRENDCAT_BIOCATALYSIS.licence, domain=None, range=Optional[str])

slots.linked_schemas = Slot(uri=DCTERMS.conformsTo, name="linked_schemas", curie=DCTERMS.curie('conformsTo'),
                   model_uri=STRENDCAT_BIOCATALYSIS.linked_schemas, domain=None, range=Optional[str])

slots.listing_date = Slot(uri=DCTERMS.issued, name="listing_date", curie=DCTERMS.curie('issued'),
                   model_uri=STRENDCAT_BIOCATALYSIS.listing_date, domain=None, range=Optional[str])

slots.media_type = Slot(uri=DCAT.mediaType, name="media_type", curie=DCAT.curie('mediaType'),
                   model_uri=STRENDCAT_BIOCATALYSIS.media_type, domain=None, range=Optional[str])

slots.modification_date = Slot(uri=DCTERMS.modified, name="modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=STRENDCAT_BIOCATALYSIS.modification_date, domain=None, range=Optional[str])

slots.name = Slot(uri=FOAF.name, name="name", curie=FOAF.curie('name'),
                   model_uri=STRENDCAT_BIOCATALYSIS.name, domain=None, range=Optional[str])

slots.notation = Slot(uri=SKOS.notation, name="notation", curie=SKOS.curie('notation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.notation, domain=None, range=Optional[str])

slots.occurred_in = Slot(uri=PROV.atLocation, name="occurred_in", curie=PROV.curie('atLocation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.occurred_in, domain=None, range=Optional[Union[dict, Surrounding]])

slots.other_identifier = Slot(uri=ADMS.identifier, name="other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.other_identifier, domain=None, range=Optional[str])

slots.packaging_format = Slot(uri=DCAT.packageFormat, name="packaging_format", curie=DCAT.curie('packageFormat'),
                   model_uri=STRENDCAT_BIOCATALYSIS.packaging_format, domain=None, range=Optional[str])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=STRENDCAT_BIOCATALYSIS.part_of, domain=None, range=Optional[Union[str, ActivityId]])

slots.preferred_label = Slot(uri=SKOS.prefLabel, name="preferred_label", curie=SKOS.curie('prefLabel'),
                   model_uri=STRENDCAT_BIOCATALYSIS.preferred_label, domain=None, range=Optional[str])

slots.primary_topic = Slot(uri=FOAF.primaryTopic, name="primary_topic", curie=FOAF.curie('primaryTopic'),
                   model_uri=STRENDCAT_BIOCATALYSIS.primary_topic, domain=None, range=Optional[str])

slots.provenance = Slot(uri=DCTERMS.provenance, name="provenance", curie=DCTERMS.curie('provenance'),
                   model_uri=STRENDCAT_BIOCATALYSIS.provenance, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=STRENDCAT_BIOCATALYSIS.publisher, domain=None, range=Optional[str])

slots.qualified_attribution = Slot(uri=PROV.qualifiedAttribution, name="qualified_attribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=STRENDCAT_BIOCATALYSIS.qualified_attribution, domain=None, range=Optional[str])

slots.qualified_relation = Slot(uri=DCAT.qualifiedRelation, name="qualified_relation", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.qualified_relation, domain=None, range=Optional[str])

slots.rdf_type = Slot(uri=RDF.type, name="rdf_type", curie=RDF.curie('type'),
                   model_uri=STRENDCAT_BIOCATALYSIS.rdf_type, domain=None, range=Optional[Union[dict, DefinedTerm]])

slots.realized_plan = Slot(uri=PROV.used, name="realized_plan", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.realized_plan, domain=None, range=Optional[Union[dict, Plan]])

slots.record = Slot(uri=DCAT.record, name="record", curie=DCAT.curie('record'),
                   model_uri=STRENDCAT_BIOCATALYSIS.record, domain=None, range=Optional[str])

slots.related_resource = Slot(uri=DCTERMS.relation, name="related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.related_resource, domain=None, range=Optional[str])

slots.relation = Slot(uri=DCTERMS.relation, name="relation", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.relation, domain=None, range=Optional[str])

slots.release_date = Slot(uri=DCTERMS.issued, name="release_date", curie=DCTERMS.curie('issued'),
                   model_uri=STRENDCAT_BIOCATALYSIS.release_date, domain=None, range=Optional[str])

slots.rights = Slot(uri=DCTERMS.rights, name="rights", curie=DCTERMS.curie('rights'),
                   model_uri=STRENDCAT_BIOCATALYSIS.rights, domain=None, range=Optional[str])

slots.sample = Slot(uri=ADMS.sample, name="sample", curie=ADMS.curie('sample'),
                   model_uri=STRENDCAT_BIOCATALYSIS.sample, domain=None, range=Optional[str])

slots.serves_dataset = Slot(uri=DCAT.servesDataset, name="serves_dataset", curie=DCAT.curie('servesDataset'),
                   model_uri=STRENDCAT_BIOCATALYSIS.serves_dataset, domain=None, range=Optional[str])

slots.service = Slot(uri=DCAT.service, name="service", curie=DCAT.curie('service'),
                   model_uri=STRENDCAT_BIOCATALYSIS.service, domain=None, range=Optional[str])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=STRENDCAT_BIOCATALYSIS.source, domain=None, range=Optional[str])

slots.source_metadata = Slot(uri=DCTERMS.source, name="source_metadata", curie=DCTERMS.curie('source'),
                   model_uri=STRENDCAT_BIOCATALYSIS.source_metadata, domain=None, range=Optional[str])

slots.spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=STRENDCAT_BIOCATALYSIS.spatial_resolution, domain=None, range=Optional[str])

slots.start_date = Slot(uri=DCAT.startDate, name="start_date", curie=DCAT.curie('startDate'),
                   model_uri=STRENDCAT_BIOCATALYSIS.start_date, domain=None, range=Optional[str])

slots.status = Slot(uri=ADMS.status, name="status", curie=ADMS.curie('status'),
                   model_uri=STRENDCAT_BIOCATALYSIS.status, domain=None, range=Optional[str])

slots.temporal_coverage = Slot(uri=DCTERMS.temporal, name="temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=STRENDCAT_BIOCATALYSIS.temporal_coverage, domain=None, range=Optional[str])

slots.temporal_resolution = Slot(uri=DCAT.temporalResolution, name="temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=STRENDCAT_BIOCATALYSIS.temporal_resolution, domain=None, range=Optional[str])

slots.theme = Slot(uri=DCAT.theme, name="theme", curie=DCAT.curie('theme'),
                   model_uri=STRENDCAT_BIOCATALYSIS.theme, domain=None, range=Optional[str])

slots.themes = Slot(uri=DCAT.themeTaxonomy, name="themes", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.themes, domain=None, range=Optional[str])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.title, domain=None, range=Optional[str])

slots.type = Slot(uri=DCTERMS.type, name="type", curie=DCTERMS.curie('type'),
                   model_uri=STRENDCAT_BIOCATALYSIS.type, domain=None, range=Optional[str])

slots.value = Slot(uri=PROV.value, name="value", curie=PROV.curie('value'),
                   model_uri=STRENDCAT_BIOCATALYSIS.value, domain=None, range=Optional[str])

slots.version = Slot(uri=DCAT.version, name="version", curie=DCAT.curie('version'),
                   model_uri=STRENDCAT_BIOCATALYSIS.version, domain=None, range=Optional[str])

slots.version_notes = Slot(uri=ADMS.versionNotes, name="version_notes", curie=ADMS.curie('versionNotes'),
                   model_uri=STRENDCAT_BIOCATALYSIS.version_notes, domain=None, range=Optional[str])

slots.was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.was_generated_by, domain=None, range=Optional[str])

slots.composed_of = Slot(uri=BFO['0000051'], name="composed_of", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.composed_of, domain=None, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, ChemicalEntity]], list[Union[dict, ChemicalEntity]]]])

slots.has_concentration = Slot(uri=SIO['000008'], name="has_concentration", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_concentration, domain=None, range=Optional[Union[Union[dict, Concentration], list[Union[dict, Concentration]]]])

slots.has_amount = Slot(uri=SIO['000008'], name="has_amount", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_amount, domain=None, range=Optional[Union[Union[dict, AmountOfSubstance], list[Union[dict, AmountOfSubstance]]]])

slots.has_ph_value = Slot(uri=SIO['000008'], name="has_ph_value", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_ph_value, domain=None, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.inchi = Slot(uri=SIO['000008'], name="inchi", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.inchi, domain=None, range=Optional[Union[Union[dict, InChi], list[Union[dict, InChi]]]])

slots.inchikey = Slot(uri=SIO['000008'], name="inchikey", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.inchikey, domain=None, range=Optional[Union[Union[dict, InChIKey], list[Union[dict, InChIKey]]]])

slots.smiles = Slot(uri=SIO['000008'], name="smiles", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.smiles, domain=None, range=Optional[Union[Union[dict, SMILES], list[Union[dict, SMILES]]]])

slots.molecular_formula = Slot(uri=SIO['000008'], name="molecular_formula", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.molecular_formula, domain=None, range=Optional[Union[Union[dict, MolecularFormula], list[Union[dict, MolecularFormula]]]])

slots.iupac_name = Slot(uri=SIO['000008'], name="iupac_name", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.iupac_name, domain=None, range=Optional[Union[Union[dict, IUPACName], list[Union[dict, IUPACName]]]])

slots.has_molar_mass = Slot(uri=SIO['000008'], name="has_molar_mass", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_molar_mass, domain=None, range=Optional[Union[Union[dict, MolarMass], list[Union[dict, MolarMass]]]])

slots.used_starting_material = Slot(uri=RO['0004009'], name="used_starting_material", curie=RO.curie('0004009'),
                   model_uri=STRENDCAT_BIOCATALYSIS.used_starting_material, domain=None, range=Optional[Union[dict[Union[str, StartingMaterialId], Union[dict, StartingMaterial]], list[Union[dict, StartingMaterial]]]])

slots.used_reactant = Slot(uri=RO['0004009'], name="used_reactant", curie=RO.curie('0004009'),
                   model_uri=STRENDCAT_BIOCATALYSIS.used_reactant, domain=None, range=Optional[Union[dict[Union[str, ReagentId], Union[dict, Reagent]], list[Union[dict, Reagent]]]])

slots.generated_product = Slot(uri=RO['0004008'], name="generated_product", curie=RO.curie('0004008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.generated_product, domain=None, range=Optional[Union[dict[Union[str, ChemicalProductId], Union[dict, ChemicalProduct]], list[Union[dict, ChemicalProduct]]]])

slots.used_catalyst = Slot(uri=RXNO['0000425'], name="used_catalyst", curie=RXNO.curie('0000425'),
                   model_uri=STRENDCAT_BIOCATALYSIS.used_catalyst, domain=None, range=Optional[Union[dict[Union[str, CatalystId], Union[dict, Catalyst]], list[Union[dict, Catalyst]]]])

slots.used_solvent = Slot(uri=PROV.wasAssociatedWith, name="used_solvent", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=STRENDCAT_BIOCATALYSIS.used_solvent, domain=None, range=Optional[Union[dict[Union[str, DissolvingSubstanceId], Union[dict, DissolvingSubstance]], list[Union[dict, DissolvingSubstance]]]])

slots.has_duration = Slot(uri=SCHEMA.duration, name="has_duration", curie=SCHEMA.curie('duration'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_duration, domain=None, range=Optional[str])

slots.used_reactor = Slot(uri=PROV.wasAssociatedWith, name="used_reactor", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=STRENDCAT_BIOCATALYSIS.used_reactor, domain=None, range=Optional[Union[dict[Union[str, ReactorId], Union[dict, Reactor]], list[Union[dict, Reactor]]]])

slots.has_yield = Slot(uri=SIO['000008'], name="has_yield", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_yield, domain=None, range=Optional[Union[Union[dict, Yield], list[Union[dict, Yield]]]])

slots.has_molar_equivalent = Slot(uri=SIO['000008'], name="has_molar_equivalent", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_molar_equivalent, domain=None, range=Optional[Union[Union[dict, MolarEquivalent], list[Union[dict, MolarEquivalent]]]])

slots.has_percentage_of_total = Slot(uri=SIO['000008'], name="has_percentage_of_total", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_percentage_of_total, domain=None, range=Optional[Union[Union[dict, PercentageOfTotal], list[Union[dict, PercentageOfTotal]]]])

slots.has_reaction_step = Slot(uri=BFO['0000051'], name="has_reaction_step", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_reaction_step, domain=None, range=Optional[Union[dict[Union[str, ChemicalReactionId], Union[dict, ChemicalReaction]], list[Union[dict, ChemicalReaction]]]])

slots.alternative_label = Slot(uri=SKOS.altLabel, name="alternative_label", curie=SKOS.curie('altLabel'),
                   model_uri=STRENDCAT_BIOCATALYSIS.alternative_label, domain=None, range=Optional[str])

slots.has_physical_state = Slot(uri=SIO['000008'], name="has_physical_state", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_physical_state, domain=None, range=Optional[Union[str, "PhysicalStateEnum"]])

slots.has_temperature = Slot(uri=SIO['000008'], name="has_temperature", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_temperature, domain=None, range=Optional[Union[Union[dict, Temperature], list[Union[dict, Temperature]]]])

slots.has_mass = Slot(uri=SIO['000008'], name="has_mass", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_mass, domain=None, range=Optional[Union[Union[dict, Mass], list[Union[dict, Mass]]]])

slots.has_volume = Slot(uri=SIO['000008'], name="has_volume", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_volume, domain=None, range=Optional[Union[Union[dict, Volume], list[Union[dict, Volume]]]])

slots.has_density = Slot(uri=SIO['000008'], name="has_density", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_density, domain=None, range=Optional[Union[Union[dict, Density], list[Union[dict, Density]]]])

slots.has_pressure = Slot(uri=SIO['000008'], name="has_pressure", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.has_pressure, domain=None, range=Optional[Union[Union[dict, Pressure], list[Union[dict, Pressure]]]])

slots.derived_from = Slot(uri=PROV.wasDerivedFrom, name="derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=STRENDCAT_BIOCATALYSIS.derived_from, domain=None, range=Optional[Union[dict, Entity]])

slots.definedTerm__from_CV = Slot(uri=SCHEMA.inDefinedTermSet, name="definedTerm__from_CV", curie=SCHEMA.curie('inDefinedTermSet'),
                   model_uri=STRENDCAT_BIOCATALYSIS.definedTerm__from_CV, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.quantitativeAttribute__has_quantity_type = Slot(uri=QUDT.hasQuantityKind, name="quantitativeAttribute__has_quantity_type", curie=QUDT.curie('hasQuantityKind'),
                   model_uri=STRENDCAT_BIOCATALYSIS.quantitativeAttribute__has_quantity_type, domain=None, range=Union[str, DefinedTermId])

slots.quantitativeAttribute__unit = Slot(uri=QUDT.unit, name="quantitativeAttribute__unit", curie=QUDT.curie('unit'),
                   model_uri=STRENDCAT_BIOCATALYSIS.quantitativeAttribute__unit, domain=None, range=Optional[Union[str, DefinedTermId]])

slots.Biocatalyst_title = Slot(uri=DCTERMS.title, name="Biocatalyst_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Biocatalyst_title, domain=Biocatalyst, range=str)

slots.Biocatalyst_other_identifier = Slot(uri=ADMS.identifier, name="Biocatalyst_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Biocatalyst_other_identifier, domain=Biocatalyst, range=Optional[str])

slots.Biocatalyst_has_quantitative_attribute = Slot(uri=DCTERMS.relation, name="Biocatalyst_has_quantitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Biocatalyst_has_quantitative_attribute, domain=Biocatalyst, range=Optional[Union[Union[dict, QuantitativeAttribute], list[Union[dict, QuantitativeAttribute]]]])

slots.BiocatalystPreparation_derived_from = Slot(uri=PROV.wasDerivedFrom, name="BiocatalystPreparation_derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=STRENDCAT_BIOCATALYSIS.BiocatalystPreparation_derived_from, domain=BiocatalystPreparation, range=Union[dict, Biocatalyst])

slots.ImmobilisedPreparation_derived_from = Slot(uri=PROV.wasDerivedFrom, name="ImmobilisedPreparation_derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ImmobilisedPreparation_derived_from, domain=ImmobilisedPreparation, range=Union[dict, BiocatalystPreparation])

slots.BiocatalyticComponent_other_identifier = Slot(uri=ADMS.identifier, name="BiocatalyticComponent_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.BiocatalyticComponent_other_identifier, domain=BiocatalyticComponent, range=Optional[str])

slots.BiocatalyticComponent_description = Slot(uri=DCTERMS.description, name="BiocatalyticComponent_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.BiocatalyticComponent_description, domain=BiocatalyticComponent, range=Optional[str])

slots.ReactionMedium_description = Slot(uri=DCTERMS.description, name="ReactionMedium_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ReactionMedium_description, domain=ReactionMedium, range=Optional[str])

slots.Vial_description = Slot(uri=DCTERMS.description, name="Vial_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Vial_description, domain=Vial, range=Optional[str])

slots.Plate_other_identifier = Slot(uri=ADMS.identifier, name="Plate_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Plate_other_identifier, domain=Plate, range=Optional[str])

slots.StirredTankReactor_has_part = Slot(uri=DCTERMS.hasPart, name="StirredTankReactor_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.StirredTankReactor_has_part, domain=StirredTankReactor, range=Optional[Union[dict[Union[str, DeviceId], Union[dict, Device]], list[Union[dict, Device]]]])

slots.SamplingProcess_had_output_entity = Slot(uri=PROV.generated, name="SamplingProcess_had_output_entity", curie=PROV.curie('generated'),
                   model_uri=STRENDCAT_BIOCATALYSIS.SamplingProcess_had_output_entity, domain=SamplingProcess, range=Optional[Union[dict[Union[str, MaterialSampleId], Union[dict, "MaterialSample"]], list[Union[dict, "MaterialSample"]]]])

slots.SamplePreparationProcess_has_part = Slot(uri=DCTERMS.hasPart, name="SamplePreparationProcess_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.SamplePreparationProcess_has_part, domain=SamplePreparationProcess, range=Optional[Union[dict[Union[str, MaterialProcessingId], Union[dict, MaterialProcessing]], list[Union[dict, MaterialProcessing]]]])

slots.SampleTreatmentProcess_description = Slot(uri=DCTERMS.description, name="SampleTreatmentProcess_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.SampleTreatmentProcess_description, domain=SampleTreatmentProcess, range=Optional[str])

slots.KineticParameters_description = Slot(uri=DCTERMS.description, name="KineticParameters_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.KineticParameters_description, domain=KineticParameters, range=Optional[str])

slots.YieldAndConversion_description = Slot(uri=DCTERMS.description, name="YieldAndConversion_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.YieldAndConversion_description, domain=YieldAndConversion, range=Optional[str])

slots.ActivityAndInitialReactionRate_description = Slot(uri=DCTERMS.description, name="ActivityAndInitialReactionRate_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ActivityAndInitialReactionRate_description, domain=ActivityAndInitialReactionRate, range=Optional[str])

slots.SelectivityAndSpecificity_description = Slot(uri=DCTERMS.description, name="SelectivityAndSpecificity_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.SelectivityAndSpecificity_description, domain=SelectivityAndSpecificity, range=Optional[str])

slots.ThermodynamicParameters_description = Slot(uri=DCTERMS.description, name="ThermodynamicParameters_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ThermodynamicParameters_description, domain=ThermodynamicParameters, range=Optional[str])

slots.BiocatalyticReaction_has_temperature = Slot(uri=SIO['000008'], name="BiocatalyticReaction_has_temperature", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.BiocatalyticReaction_has_temperature, domain=BiocatalyticReaction, range=Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]])

slots.BiocatalyticReaction_has_ph_value = Slot(uri=SIO['000008'], name="BiocatalyticReaction_has_ph_value", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.BiocatalyticReaction_has_ph_value, domain=BiocatalyticReaction, range=Optional[Union[Union[dict, PHValue], list[Union[dict, PHValue]]]])

slots.BiocatalyticExperiment_evaluated_activity = Slot(uri=PROV.wasInformedBy, name="BiocatalyticExperiment_evaluated_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.BiocatalyticExperiment_evaluated_activity, domain=BiocatalyticExperiment, range=Optional[Union[dict[Union[str, BiocatalyticReactionId], Union[dict, "BiocatalyticReaction"]], list[Union[dict, "BiocatalyticReaction"]]]])

slots.BiocatalyticExperiment_occurred_in = Slot(uri=PROV.atLocation, name="BiocatalyticExperiment_occurred_in", curie=PROV.curie('atLocation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.BiocatalyticExperiment_occurred_in, domain=BiocatalyticExperiment, range=Optional[Union[dict, "Laboratory"]])

slots.BiocatalyticExperiment_carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="BiocatalyticExperiment_carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=STRENDCAT_BIOCATALYSIS.BiocatalyticExperiment_carried_out_by, domain=BiocatalyticExperiment, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, AgenticEntity]], list[Union[dict, AgenticEntity]]]])

slots.EnzymeMLDocument_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="EnzymeMLDocument_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EnzymeMLDocument_was_generated_by, domain=EnzymeMLDocument, range=Union[dict[Union[str, BiocatalyticExperimentId], Union[dict, BiocatalyticExperiment]], list[Union[dict, BiocatalyticExperiment]]])

slots.EnzymeMLDocument_is_about_activity = Slot(uri=DCTERMS.subject, name="EnzymeMLDocument_is_about_activity", curie=DCTERMS.curie('subject'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EnzymeMLDocument_is_about_activity, domain=EnzymeMLDocument, range=Optional[Union[dict[Union[str, BiocatalyticReactionId], Union[dict, "BiocatalyticReaction"]], list[Union[dict, "BiocatalyticReaction"]]]])

slots.EnzymeMLDocument_creator = Slot(uri=DCTERMS.creator, name="EnzymeMLDocument_creator", curie=DCTERMS.curie('creator'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EnzymeMLDocument_creator, domain=EnzymeMLDocument, range=Optional[Union[Union[dict, EnzymeMLCreator], list[Union[dict, EnzymeMLCreator]]]])

slots.MolecularComplex_has_part = Slot(uri=DCTERMS.hasPart, name="MolecularComplex_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.MolecularComplex_has_part, domain=MolecularComplex, range=Optional[Union[str, ChemicalEntityId]])

slots.KineticModelParameter_value = Slot(uri=PROV.value, name="KineticModelParameter_value", curie=PROV.curie('value'),
                   model_uri=STRENDCAT_BIOCATALYSIS.KineticModelParameter_value, domain=KineticModelParameter, range=Optional[str])

slots.EnzymeMeasurement_has_ph_value = Slot(uri=SIO['000008'], name="EnzymeMeasurement_has_ph_value", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EnzymeMeasurement_has_ph_value, domain=EnzymeMeasurement, range=Optional[Union[Union[dict, "PHValue"], list[Union[dict, "PHValue"]]]])

slots.EnzymeMeasurement_has_temperature = Slot(uri=SIO['000008'], name="EnzymeMeasurement_has_temperature", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EnzymeMeasurement_has_temperature, domain=EnzymeMeasurement, range=Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]])

slots.EnzymeMeasurementSpeciesData_value = Slot(uri=PROV.value, name="EnzymeMeasurementSpeciesData_value", curie=PROV.curie('value'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EnzymeMeasurementSpeciesData_value, domain=EnzymeMeasurementSpeciesData, range=Optional[str])

slots.SubstanceSampleCharacterizationDataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="SubstanceSampleCharacterizationDataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.SubstanceSampleCharacterizationDataset_was_generated_by, domain=SubstanceSampleCharacterizationDataset, range=Optional[Union[dict[Union[str, SubstanceSampleCharacterizationId], Union[dict, SubstanceSampleCharacterization]], list[Union[dict, SubstanceSampleCharacterization]]]])

slots.SubstanceSampleCharacterizationDataset_is_about_entity = Slot(uri=DCTERMS.subject, name="SubstanceSampleCharacterizationDataset_is_about_entity", curie=DCTERMS.curie('subject'),
                   model_uri=STRENDCAT_BIOCATALYSIS.SubstanceSampleCharacterizationDataset_is_about_entity, domain=SubstanceSampleCharacterizationDataset, range=Optional[Union[dict[Union[str, SubstanceSampleId], Union[dict, "SubstanceSample"]], list[Union[dict, "SubstanceSample"]]]])

slots.ReactionMonitoringDataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="ReactionMonitoringDataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ReactionMonitoringDataset_was_generated_by, domain=ReactionMonitoringDataset, range=Optional[Union[dict[Union[str, ReactionMonitoringId], Union[dict, ReactionMonitoring]], list[Union[dict, ReactionMonitoring]]]])

slots.ReactionMonitoringDataset_is_about_activity = Slot(uri=DCTERMS.subject, name="ReactionMonitoringDataset_is_about_activity", curie=DCTERMS.curie('subject'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ReactionMonitoringDataset_is_about_activity, domain=ReactionMonitoringDataset, range=Optional[Union[dict[Union[str, ChemicalReactionId], Union[dict, "ChemicalReaction"]], list[Union[dict, "ChemicalReaction"]]]])

slots.SubstanceSampleCharacterization_evaluated_entity = Slot(uri=PROV.used, name="SubstanceSampleCharacterization_evaluated_entity", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.SubstanceSampleCharacterization_evaluated_entity, domain=SubstanceSampleCharacterization, range=Optional[Union[dict[Union[str, SubstanceSampleId], Union[dict, "SubstanceSample"]], list[Union[dict, "SubstanceSample"]]]])

slots.ReactionMonitoring_evaluated_activity = Slot(uri=PROV.wasInformedBy, name="ReactionMonitoring_evaluated_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ReactionMonitoring_evaluated_activity, domain=ReactionMonitoring, range=Optional[Union[dict[Union[str, ChemicalReactionId], Union[dict, "ChemicalReaction"]], list[Union[dict, "ChemicalReaction"]]]])

slots.Activity_title = Slot(uri=DCTERMS.title, name="Activity_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_title, domain=Activity, range=Optional[Union[str, list[str]]])

slots.Activity_description = Slot(uri=DCTERMS.description, name="Activity_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_description, domain=Activity, range=Optional[Union[str, list[str]]])

slots.Activity_has_part = Slot(uri=DCTERMS.hasPart, name="Activity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_has_part, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_part_of = Slot(uri=DCTERMS.isPartOf, name="Activity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_part_of, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_other_identifier = Slot(uri=ADMS.identifier, name="Activity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_other_identifier, domain=Activity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Activity_has_qualitative_attribute = Slot(uri=DCTERMS.relation, name="Activity_has_qualitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_has_qualitative_attribute, domain=Activity, range=Optional[Union[Union[dict, "QualitativeAttribute"], list[Union[dict, "QualitativeAttribute"]]]])

slots.Activity_has_quantitative_attribute = Slot(uri=DCTERMS.relation, name="Activity_has_quantitative_attribute", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_has_quantitative_attribute, domain=Activity, range=Optional[Union[Union[dict, "QuantitativeAttribute"], list[Union[dict, "QuantitativeAttribute"]]]])

slots.Activity_had_input_entity = Slot(uri=PROV.used, name="Activity_had_input_entity", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_had_input_entity, domain=Activity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Activity_had_output_entity = Slot(uri=PROV.generated, name="Activity_had_output_entity", curie=PROV.curie('generated'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_had_output_entity, domain=Activity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Activity_had_input_activity = Slot(uri=PROV.wasInformedBy, name="Activity_had_input_activity", curie=PROV.curie('wasInformedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_had_input_activity, domain=Activity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, "Activity"]], list[Union[dict, "Activity"]]]])

slots.Activity_carried_out_by = Slot(uri=PROV.wasAssociatedWith, name="Activity_carried_out_by", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Activity_carried_out_by, domain=Activity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.Agent_name = Slot(uri=FOAF.name, name="Agent_name", curie=FOAF.curie('name'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Agent_name, domain=Agent, range=Union[str, list[str]])

slots.Agent_type = Slot(uri=DCTERMS.type, name="Agent_type", curie=DCTERMS.curie('type'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Agent_type, domain=Agent, range=Optional[Union[dict, "Concept"]])

slots.AgenticEntity_has_part = Slot(uri=DCTERMS.hasPart, name="AgenticEntity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.AgenticEntity_has_part, domain=AgenticEntity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.AgenticEntity_part_of = Slot(uri=DCTERMS.isPartOf, name="AgenticEntity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=STRENDCAT_BIOCATALYSIS.AgenticEntity_part_of, domain=AgenticEntity, range=Optional[Union[dict[Union[str, AgenticEntityId], Union[dict, "AgenticEntity"]], list[Union[dict, "AgenticEntity"]]]])

slots.AgenticEntity_other_identifier = Slot(uri=ADMS.identifier, name="AgenticEntity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.AgenticEntity_other_identifier, domain=AgenticEntity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.AnalysisDataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="AnalysisDataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.AnalysisDataset_was_generated_by, domain=AnalysisDataset, range=Optional[Union[dict[Union[str, DataAnalysisId], Union[dict, DataAnalysis]], list[Union[dict, DataAnalysis]]]])

slots.AnalysisSourceData_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="AnalysisSourceData_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.AnalysisSourceData_was_generated_by, domain=AnalysisSourceData, range=Optional[Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]]])

slots.Catalogue_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Catalogue_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_applicable_legislation, domain=Catalogue, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Catalogue_catalogue = Slot(uri=DCAT.catalog, name="Catalogue_catalogue", curie=DCAT.curie('catalog'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_catalogue, domain=Catalogue, range=Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]])

slots.Catalogue_creator = Slot(uri=DCTERMS.creator, name="Catalogue_creator", curie=DCTERMS.curie('creator'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_creator, domain=Catalogue, range=Optional[Union[dict, Agent]])

slots.Catalogue_description = Slot(uri=DCTERMS.description, name="Catalogue_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_description, domain=Catalogue, range=Union[str, list[str]])

slots.Catalogue_geographical_coverage = Slot(uri=DCTERMS.spatial, name="Catalogue_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_geographical_coverage, domain=Catalogue, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.Catalogue_has_dataset = Slot(uri=DCAT.dataset, name="Catalogue_has_dataset", curie=DCAT.curie('dataset'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_has_dataset, domain=Catalogue, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Catalogue_has_part = Slot(uri=DCTERMS.hasPart, name="Catalogue_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_has_part, domain=Catalogue, range=Optional[Union[Union[dict, "Catalogue"], list[Union[dict, "Catalogue"]]]])

slots.Catalogue_homepage = Slot(uri=FOAF.homepage, name="Catalogue_homepage", curie=FOAF.curie('homepage'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_homepage, domain=Catalogue, range=Optional[Union[dict, "Document"]])

slots.Catalogue_language = Slot(uri=DCTERMS.language, name="Catalogue_language", curie=DCTERMS.curie('language'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_language, domain=Catalogue, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Catalogue_licence = Slot(uri=DCTERMS.license, name="Catalogue_licence", curie=DCTERMS.curie('license'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_licence, domain=Catalogue, range=Optional[Union[dict, "LicenseDocument"]])

slots.Catalogue_modification_date = Slot(uri=DCTERMS.modified, name="Catalogue_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_modification_date, domain=Catalogue, range=Optional[Union[str, XSDDate]])

slots.Catalogue_publisher = Slot(uri=DCTERMS.publisher, name="Catalogue_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_publisher, domain=Catalogue, range=Union[dict, Agent])

slots.Catalogue_record = Slot(uri=DCAT.record, name="Catalogue_record", curie=DCAT.curie('record'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_record, domain=Catalogue, range=Optional[Union[Union[dict, "CatalogueRecord"], list[Union[dict, "CatalogueRecord"]]]])

slots.Catalogue_release_date = Slot(uri=DCTERMS.issued, name="Catalogue_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_release_date, domain=Catalogue, range=Optional[Union[str, XSDDate]])

slots.Catalogue_rights = Slot(uri=DCTERMS.rights, name="Catalogue_rights", curie=DCTERMS.curie('rights'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_rights, domain=Catalogue, range=Optional[Union[dict, "RightsStatement"]])

slots.Catalogue_service = Slot(uri=DCAT.service, name="Catalogue_service", curie=DCAT.curie('service'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_service, domain=Catalogue, range=Optional[Union[Union[dict, "DataService"], list[Union[dict, "DataService"]]]])

slots.Catalogue_temporal_coverage = Slot(uri=DCTERMS.temporal, name="Catalogue_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_temporal_coverage, domain=Catalogue, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.Catalogue_themes = Slot(uri=DCAT.themeTaxonomy, name="Catalogue_themes", curie=DCAT.curie('themeTaxonomy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_themes, domain=Catalogue, range=Optional[Union[Union[dict, "ConceptScheme"], list[Union[dict, "ConceptScheme"]]]])

slots.Catalogue_title = Slot(uri=DCTERMS.title, name="Catalogue_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Catalogue_title, domain=Catalogue, range=Union[str, list[str]])

slots.CatalogueRecord_application_profile = Slot(uri=DCTERMS.conformsTo, name="CatalogueRecord_application_profile", curie=DCTERMS.curie('conformsTo'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_application_profile, domain=CatalogueRecord, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.CatalogueRecord_change_type = Slot(uri=ADMS.status, name="CatalogueRecord_change_type", curie=ADMS.curie('status'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_change_type, domain=CatalogueRecord, range=Optional[Union[dict, "Concept"]])

slots.CatalogueRecord_description = Slot(uri=DCTERMS.description, name="CatalogueRecord_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_description, domain=CatalogueRecord, range=Optional[Union[str, list[str]]])

slots.CatalogueRecord_language = Slot(uri=DCTERMS.language, name="CatalogueRecord_language", curie=DCTERMS.curie('language'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_language, domain=CatalogueRecord, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.CatalogueRecord_listing_date = Slot(uri=DCTERMS.issued, name="CatalogueRecord_listing_date", curie=DCTERMS.curie('issued'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_listing_date, domain=CatalogueRecord, range=Optional[Union[str, XSDDate]])

slots.CatalogueRecord_modification_date = Slot(uri=DCTERMS.modified, name="CatalogueRecord_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_modification_date, domain=CatalogueRecord, range=Union[str, XSDDate])

slots.CatalogueRecord_primary_topic = Slot(uri=FOAF.primaryTopic, name="CatalogueRecord_primary_topic", curie=FOAF.curie('primaryTopic'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_primary_topic, domain=CatalogueRecord, range=Union[dict, Any])

slots.CatalogueRecord_source_metadata = Slot(uri=DCTERMS.source, name="CatalogueRecord_source_metadata", curie=DCTERMS.curie('source'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_source_metadata, domain=CatalogueRecord, range=Optional[Union[dict, "CatalogueRecord"]])

slots.CatalogueRecord_title = Slot(uri=DCTERMS.title, name="CatalogueRecord_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.CatalogueRecord_title, domain=CatalogueRecord, range=Optional[Union[str, list[str]]])

slots.Checksum_algorithm = Slot(uri=SPDX.algorithm, name="Checksum_algorithm", curie=SPDX.curie('algorithm'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Checksum_algorithm, domain=Checksum, range=Union[dict, "ChecksumAlgorithm"])

slots.Checksum_checksum_value = Slot(uri=SPDX.checksumValue, name="Checksum_checksum_value", curie=SPDX.curie('checksumValue'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Checksum_checksum_value, domain=Checksum, range=str)

slots.ClassifierMixin_type = Slot(uri=DCTERMS.type, name="ClassifierMixin_type", curie=DCTERMS.curie('type'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ClassifierMixin_type, domain=None, range=Optional[Union[dict, "DefinedTerm"]])

slots.Concept_preferred_label = Slot(uri=SKOS.prefLabel, name="Concept_preferred_label", curie=SKOS.curie('prefLabel'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Concept_preferred_label, domain=Concept, range=Union[str, list[str]])

slots.ConceptScheme_title = Slot(uri=DCTERMS.title, name="ConceptScheme_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ConceptScheme_title, domain=ConceptScheme, range=Union[str, list[str]])

slots.DataAnalysis_evaluated_entity = Slot(uri=PROV.used, name="DataAnalysis_evaluated_entity", curie=PROV.curie('used'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataAnalysis_evaluated_entity, domain=DataAnalysis, range=Optional[Union[dict[Union[str, AnalysisSourceDataId], Union[dict, "AnalysisSourceData"]], list[Union[dict, "AnalysisSourceData"]]]])

slots.DataService_access_rights = Slot(uri=DCTERMS.accessRights, name="DataService_access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_access_rights, domain=DataService, range=Optional[Union[dict, "RightsStatement"]])

slots.DataService_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="DataService_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_applicable_legislation, domain=DataService, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.DataService_conforms_to = Slot(uri=DCTERMS.conformsTo, name="DataService_conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_conforms_to, domain=DataService, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.DataService_contact_point = Slot(uri=DCAT.contactPoint, name="DataService_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_contact_point, domain=DataService, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.DataService_description = Slot(uri=DCTERMS.description, name="DataService_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_description, domain=DataService, range=Optional[Union[str, list[str]]])

slots.DataService_documentation = Slot(uri=FOAF.page, name="DataService_documentation", curie=FOAF.curie('page'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_documentation, domain=DataService, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.DataService_endpoint_URL = Slot(uri=DCAT.endpointURL, name="DataService_endpoint_URL", curie=DCAT.curie('endpointURL'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_endpoint_URL, domain=DataService, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.DataService_endpoint_description = Slot(uri=DCAT.endpointDescription, name="DataService_endpoint_description", curie=DCAT.curie('endpointDescription'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_endpoint_description, domain=DataService, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.DataService_format = Slot(uri=DCTERMS.format, name="DataService_format", curie=DCTERMS.curie('format'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_format, domain=DataService, range=Optional[Union[Union[dict, "MediaTypeOrExtent"], list[Union[dict, "MediaTypeOrExtent"]]]])

slots.DataService_keyword = Slot(uri=DCAT.keyword, name="DataService_keyword", curie=DCAT.curie('keyword'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_keyword, domain=DataService, range=Optional[Union[str, list[str]]])

slots.DataService_landing_page = Slot(uri=DCAT.landingPage, name="DataService_landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_landing_page, domain=DataService, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.DataService_licence = Slot(uri=DCTERMS.license, name="DataService_licence", curie=DCTERMS.curie('license'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_licence, domain=DataService, range=Optional[Union[dict, "LicenseDocument"]])

slots.DataService_publisher = Slot(uri=DCTERMS.publisher, name="DataService_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_publisher, domain=DataService, range=Optional[Union[dict, Agent]])

slots.DataService_serves_dataset = Slot(uri=DCAT.servesDataset, name="DataService_serves_dataset", curie=DCAT.curie('servesDataset'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_serves_dataset, domain=DataService, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.DataService_theme = Slot(uri=DCAT.theme, name="DataService_theme", curie=DCAT.curie('theme'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_theme, domain=DataService, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.DataService_title = Slot(uri=DCTERMS.title, name="DataService_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DataService_title, domain=DataService, range=Union[str, list[str]])

slots.Dataset_access_rights = Slot(uri=DCTERMS.accessRights, name="Dataset_access_rights", curie=DCTERMS.curie('accessRights'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_access_rights, domain=Dataset, range=Optional[Union[dict, "RightsStatement"]])

slots.Dataset_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Dataset_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_applicable_legislation, domain=Dataset, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Dataset_conforms_to = Slot(uri=DCTERMS.conformsTo, name="Dataset_conforms_to", curie=DCTERMS.curie('conformsTo'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_conforms_to, domain=Dataset, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.Dataset_contact_point = Slot(uri=DCAT.contactPoint, name="Dataset_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_contact_point, domain=Dataset, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.Dataset_creator = Slot(uri=DCTERMS.creator, name="Dataset_creator", curie=DCTERMS.curie('creator'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_creator, domain=Dataset, range=Optional[Union[Union[dict, Agent], list[Union[dict, Agent]]]])

slots.Dataset_dataset_distribution = Slot(uri=DCAT.distribution, name="Dataset_dataset_distribution", curie=DCAT.curie('distribution'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_dataset_distribution, domain=Dataset, range=Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]])

slots.Dataset_description = Slot(uri=DCTERMS.description, name="Dataset_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_description, domain=Dataset, range=Union[str, list[str]])

slots.Dataset_documentation = Slot(uri=FOAF.page, name="Dataset_documentation", curie=FOAF.curie('page'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_documentation, domain=Dataset, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Dataset_frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="Dataset_frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_frequency, domain=Dataset, range=Optional[Union[dict, "Frequency"]])

slots.Dataset_geographical_coverage = Slot(uri=DCTERMS.spatial, name="Dataset_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_geographical_coverage, domain=Dataset, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.Dataset_has_version = Slot(uri=DCAT.hasVersion, name="Dataset_has_version", curie=DCAT.curie('hasVersion'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_has_version, domain=Dataset, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Dataset_identifier = Slot(uri=DCTERMS.identifier, name="Dataset_identifier", curie=DCTERMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_identifier, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_in_series = Slot(uri=DCAT.inSeries, name="Dataset_in_series", curie=DCAT.curie('inSeries'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_in_series, domain=Dataset, range=Optional[Union[Union[dict, "DatasetSeries"], list[Union[dict, "DatasetSeries"]]]])

slots.Dataset_is_referenced_by = Slot(uri=DCTERMS.isReferencedBy, name="Dataset_is_referenced_by", curie=DCTERMS.curie('isReferencedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_is_referenced_by, domain=Dataset, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Dataset_keyword = Slot(uri=DCAT.keyword, name="Dataset_keyword", curie=DCAT.curie('keyword'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_keyword, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_landing_page = Slot(uri=DCAT.landingPage, name="Dataset_landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_landing_page, domain=Dataset, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Dataset_language = Slot(uri=DCTERMS.language, name="Dataset_language", curie=DCTERMS.curie('language'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_language, domain=Dataset, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Dataset_modification_date = Slot(uri=DCTERMS.modified, name="Dataset_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_modification_date, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.Dataset_other_identifier = Slot(uri=ADMS.identifier, name="Dataset_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_other_identifier, domain=Dataset, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Dataset_provenance = Slot(uri=DCTERMS.provenance, name="Dataset_provenance", curie=DCTERMS.curie('provenance'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_provenance, domain=Dataset, range=Optional[Union[Union[dict, "ProvenanceStatement"], list[Union[dict, "ProvenanceStatement"]]]])

slots.Dataset_publisher = Slot(uri=DCTERMS.publisher, name="Dataset_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_publisher, domain=Dataset, range=Optional[Union[dict, Agent]])

slots.Dataset_qualified_attribution = Slot(uri=PROV.qualifiedAttribution, name="Dataset_qualified_attribution", curie=PROV.curie('qualifiedAttribution'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_qualified_attribution, domain=Dataset, range=Optional[Union[Union[dict, "Attribution"], list[Union[dict, "Attribution"]]]])

slots.Dataset_qualified_relation = Slot(uri=DCAT.qualifiedRelation, name="Dataset_qualified_relation", curie=DCAT.curie('qualifiedRelation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_qualified_relation, domain=Dataset, range=Optional[Union[Union[dict, "Relationship"], list[Union[dict, "Relationship"]]]])

slots.Dataset_related_resource = Slot(uri=DCTERMS.relation, name="Dataset_related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_related_resource, domain=Dataset, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Dataset_release_date = Slot(uri=DCTERMS.issued, name="Dataset_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_release_date, domain=Dataset, range=Optional[Union[str, XSDDate]])

slots.Dataset_sample = Slot(uri=ADMS.sample, name="Dataset_sample", curie=ADMS.curie('sample'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_sample, domain=Dataset, range=Optional[Union[Union[dict, "Distribution"], list[Union[dict, "Distribution"]]]])

slots.Dataset_source = Slot(uri=DCTERMS.source, name="Dataset_source", curie=DCTERMS.curie('source'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_source, domain=Dataset, range=Optional[Union[dict[Union[str, DatasetId], Union[dict, "Dataset"]], list[Union[dict, "Dataset"]]]])

slots.Dataset_spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="Dataset_spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_spatial_resolution, domain=Dataset, range=Optional[Decimal])

slots.Dataset_temporal_coverage = Slot(uri=DCTERMS.temporal, name="Dataset_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_temporal_coverage, domain=Dataset, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.Dataset_temporal_resolution = Slot(uri=DCAT.temporalResolution, name="Dataset_temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_temporal_resolution, domain=Dataset, range=Optional[str])

slots.Dataset_theme = Slot(uri=DCAT.theme, name="Dataset_theme", curie=DCAT.curie('theme'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_theme, domain=Dataset, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.Dataset_title = Slot(uri=DCTERMS.title, name="Dataset_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_title, domain=Dataset, range=Union[str, list[str]])

slots.Dataset_type = Slot(uri=DCTERMS.type, name="Dataset_type", curie=DCTERMS.curie('type'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_type, domain=Dataset, range=Optional[Union[Union[dict, "Concept"], list[Union[dict, "Concept"]]]])

slots.Dataset_version = Slot(uri=DCAT.version, name="Dataset_version", curie=DCAT.curie('version'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_version, domain=Dataset, range=Optional[str])

slots.Dataset_version_notes = Slot(uri=ADMS.versionNotes, name="Dataset_version_notes", curie=ADMS.curie('versionNotes'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_version_notes, domain=Dataset, range=Optional[Union[str, list[str]]])

slots.Dataset_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="Dataset_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Dataset_was_generated_by, domain=Dataset, range=Union[dict[Union[str, DataGeneratingActivityId], Union[dict, DataGeneratingActivity]], list[Union[dict, DataGeneratingActivity]]])

slots.DatasetSeries_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="DatasetSeries_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_applicable_legislation, domain=DatasetSeries, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.DatasetSeries_contact_point = Slot(uri=DCAT.contactPoint, name="DatasetSeries_contact_point", curie=DCAT.curie('contactPoint'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_contact_point, domain=DatasetSeries, range=Optional[Union[Union[dict, "Kind"], list[Union[dict, "Kind"]]]])

slots.DatasetSeries_description = Slot(uri=DCTERMS.description, name="DatasetSeries_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_description, domain=DatasetSeries, range=Union[str, list[str]])

slots.DatasetSeries_frequency = Slot(uri=DCTERMS.accrualPeriodicity, name="DatasetSeries_frequency", curie=DCTERMS.curie('accrualPeriodicity'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_frequency, domain=DatasetSeries, range=Optional[Union[dict, "Frequency"]])

slots.DatasetSeries_geographical_coverage = Slot(uri=DCTERMS.spatial, name="DatasetSeries_geographical_coverage", curie=DCTERMS.curie('spatial'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_geographical_coverage, domain=DatasetSeries, range=Optional[Union[Union[dict, "Location"], list[Union[dict, "Location"]]]])

slots.DatasetSeries_modification_date = Slot(uri=DCTERMS.modified, name="DatasetSeries_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_modification_date, domain=DatasetSeries, range=Optional[Union[str, XSDDate]])

slots.DatasetSeries_publisher = Slot(uri=DCTERMS.publisher, name="DatasetSeries_publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_publisher, domain=DatasetSeries, range=Optional[Union[dict, Agent]])

slots.DatasetSeries_release_date = Slot(uri=DCTERMS.issued, name="DatasetSeries_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_release_date, domain=DatasetSeries, range=Optional[Union[str, XSDDate]])

slots.DatasetSeries_temporal_coverage = Slot(uri=DCTERMS.temporal, name="DatasetSeries_temporal_coverage", curie=DCTERMS.curie('temporal'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_temporal_coverage, domain=DatasetSeries, range=Optional[Union[Union[dict, "PeriodOfTime"], list[Union[dict, "PeriodOfTime"]]]])

slots.DatasetSeries_title = Slot(uri=DCTERMS.title, name="DatasetSeries_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DatasetSeries_title, domain=DatasetSeries, range=Union[str, list[str]])

slots.DefinedTerm_title = Slot(uri=SCHEMA.name, name="DefinedTerm_title", curie=SCHEMA.curie('name'),
                   model_uri=STRENDCAT_BIOCATALYSIS.DefinedTerm_title, domain=DefinedTerm, range=Optional[str])

slots.Device_has_part = Slot(uri=DCTERMS.hasPart, name="Device_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Device_has_part, domain=Device, range=Optional[Union[dict[Union[str, DeviceId], Union[dict, "Device"]], list[Union[dict, "Device"]]]])

slots.Device_other_identifier = Slot(uri=ADMS.identifier, name="Device_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Device_other_identifier, domain=Device, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Distribution_access_URL = Slot(uri=DCAT.accessURL, name="Distribution_access_URL", curie=DCAT.curie('accessURL'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_access_URL, domain=Distribution, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.Distribution_access_service = Slot(uri=DCAT.accessService, name="Distribution_access_service", curie=DCAT.curie('accessService'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_access_service, domain=Distribution, range=Optional[Union[Union[dict, DataService], list[Union[dict, DataService]]]])

slots.Distribution_applicable_legislation = Slot(uri=DCATAP.applicableLegislation, name="Distribution_applicable_legislation", curie=DCATAP.curie('applicableLegislation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_applicable_legislation, domain=Distribution, range=Optional[Union[dict[Union[str, LegalResourceId], Union[dict, "LegalResource"]], list[Union[dict, "LegalResource"]]]])

slots.Distribution_availability = Slot(uri=DCATAP.availability, name="Distribution_availability", curie=DCATAP.curie('availability'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_availability, domain=Distribution, range=Optional[Union[dict, "Concept"]])

slots.Distribution_byte_size = Slot(uri=DCAT.byteSize, name="Distribution_byte_size", curie=DCAT.curie('byteSize'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_byte_size, domain=Distribution, range=Optional[int])

slots.Distribution_checksum = Slot(uri=SPDX.checksum, name="Distribution_checksum", curie=SPDX.curie('checksum'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_checksum, domain=Distribution, range=Optional[Union[dict, Checksum]])

slots.Distribution_compression_format = Slot(uri=DCAT.compressFormat, name="Distribution_compression_format", curie=DCAT.curie('compressFormat'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_compression_format, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_description = Slot(uri=DCTERMS.description, name="Distribution_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_description, domain=Distribution, range=Optional[Union[str, list[str]]])

slots.Distribution_documentation = Slot(uri=FOAF.page, name="Distribution_documentation", curie=FOAF.curie('page'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_documentation, domain=Distribution, range=Optional[Union[dict[Union[str, DocumentId], Union[dict, "Document"]], list[Union[dict, "Document"]]]])

slots.Distribution_download_URL = Slot(uri=DCAT.downloadURL, name="Distribution_download_URL", curie=DCAT.curie('downloadURL'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_download_URL, domain=Distribution, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]]])

slots.Distribution_format = Slot(uri=DCTERMS.format, name="Distribution_format", curie=DCTERMS.curie('format'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_format, domain=Distribution, range=Optional[Union[dict, "MediaTypeOrExtent"]])

slots.Distribution_has_policy = Slot(uri=ODRL.hasPolicy, name="Distribution_has_policy", curie=ODRL.curie('hasPolicy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_has_policy, domain=Distribution, range=Optional[Union[dict, "Policy"]])

slots.Distribution_language = Slot(uri=DCTERMS.language, name="Distribution_language", curie=DCTERMS.curie('language'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_language, domain=Distribution, range=Optional[Union[Union[dict, "LinguisticSystem"], list[Union[dict, "LinguisticSystem"]]]])

slots.Distribution_licence = Slot(uri=DCTERMS.license, name="Distribution_licence", curie=DCTERMS.curie('license'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_licence, domain=Distribution, range=Optional[Union[dict, "LicenseDocument"]])

slots.Distribution_linked_schemas = Slot(uri=DCTERMS.conformsTo, name="Distribution_linked_schemas", curie=DCTERMS.curie('conformsTo'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_linked_schemas, domain=Distribution, range=Optional[Union[Union[dict, "Standard"], list[Union[dict, "Standard"]]]])

slots.Distribution_media_type = Slot(uri=DCAT.mediaType, name="Distribution_media_type", curie=DCAT.curie('mediaType'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_media_type, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_modification_date = Slot(uri=DCTERMS.modified, name="Distribution_modification_date", curie=DCTERMS.curie('modified'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_modification_date, domain=Distribution, range=Optional[Union[str, XSDDate]])

slots.Distribution_packaging_format = Slot(uri=DCAT.packageFormat, name="Distribution_packaging_format", curie=DCAT.curie('packageFormat'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_packaging_format, domain=Distribution, range=Optional[Union[dict, "MediaType"]])

slots.Distribution_release_date = Slot(uri=DCTERMS.issued, name="Distribution_release_date", curie=DCTERMS.curie('issued'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_release_date, domain=Distribution, range=Optional[Union[str, XSDDate]])

slots.Distribution_rights = Slot(uri=DCTERMS.rights, name="Distribution_rights", curie=DCTERMS.curie('rights'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_rights, domain=Distribution, range=Optional[Union[dict, "RightsStatement"]])

slots.Distribution_spatial_resolution = Slot(uri=DCAT.spatialResolutionInMeters, name="Distribution_spatial_resolution", curie=DCAT.curie('spatialResolutionInMeters'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_spatial_resolution, domain=Distribution, range=Optional[Decimal])

slots.Distribution_status = Slot(uri=ADMS.status, name="Distribution_status", curie=ADMS.curie('status'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_status, domain=Distribution, range=Optional[Union[dict, "Concept"]])

slots.Distribution_temporal_resolution = Slot(uri=DCAT.temporalResolution, name="Distribution_temporal_resolution", curie=DCAT.curie('temporalResolution'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_temporal_resolution, domain=Distribution, range=Optional[str])

slots.Distribution_title = Slot(uri=DCTERMS.title, name="Distribution_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Distribution_title, domain=Distribution, range=Optional[Union[str, list[str]]])

slots.Entity_title = Slot(uri=DCTERMS.title, name="Entity_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Entity_title, domain=Entity, range=Optional[str])

slots.Entity_description = Slot(uri=DCTERMS.description, name="Entity_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Entity_description, domain=Entity, range=Optional[str])

slots.Entity_other_identifier = Slot(uri=ADMS.identifier, name="Entity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Entity_other_identifier, domain=Entity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Entity_has_part = Slot(uri=DCTERMS.hasPart, name="Entity_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Entity_has_part, domain=Entity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.Entity_part_of = Slot(uri=DCTERMS.isPartOf, name="Entity_part_of", curie=DCTERMS.curie('isPartOf'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Entity_part_of, domain=Entity, range=Optional[Union[dict[Union[str, EntityId], Union[dict, "Entity"]], list[Union[dict, "Entity"]]]])

slots.EvaluatedActivity_other_identifier = Slot(uri=ADMS.identifier, name="EvaluatedActivity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EvaluatedActivity_other_identifier, domain=EvaluatedActivity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.EvaluatedEntity_title = Slot(uri=DCTERMS.title, name="EvaluatedEntity_title", curie=DCTERMS.curie('title'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EvaluatedEntity_title, domain=EvaluatedEntity, range=Optional[str])

slots.EvaluatedEntity_description = Slot(uri=DCTERMS.description, name="EvaluatedEntity_description", curie=DCTERMS.curie('description'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EvaluatedEntity_description, domain=EvaluatedEntity, range=Optional[str])

slots.EvaluatedEntity_was_generated_by = Slot(uri=PROV.wasGeneratedBy, name="EvaluatedEntity_was_generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EvaluatedEntity_was_generated_by, domain=EvaluatedEntity, range=Optional[Union[dict[Union[str, ActivityId], Union[dict, Activity]], list[Union[dict, Activity]]]])

slots.EvaluatedEntity_other_identifier = Slot(uri=ADMS.identifier, name="EvaluatedEntity_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.EvaluatedEntity_other_identifier, domain=EvaluatedEntity, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.Identifier_notation = Slot(uri=SKOS.notation, name="Identifier_notation", curie=SKOS.curie('notation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Identifier_notation, domain=Identifier, range=str)

slots.LicenseDocument_type = Slot(uri=DCTERMS.type, name="LicenseDocument_type", curie=DCTERMS.curie('type'),
                   model_uri=STRENDCAT_BIOCATALYSIS.LicenseDocument_type, domain=LicenseDocument, range=Optional[Union[Union[dict, Concept], list[Union[dict, Concept]]]])

slots.Location_bbox = Slot(uri=DCAT.bbox, name="Location_bbox", curie=DCAT.curie('bbox'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Location_bbox, domain=Location, range=Optional[str])

slots.Location_centroid = Slot(uri=DCAT.centroid, name="Location_centroid", curie=DCAT.curie('centroid'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Location_centroid, domain=Location, range=Optional[str])

slots.Location_geometry = Slot(uri=LOCN.geometry, name="Location_geometry", curie=LOCN.curie('geometry'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Location_geometry, domain=Location, range=Optional[Union[dict, "Geometry"]])

slots.PeriodOfTime_beginning = Slot(uri=TIME.hasBeginning, name="PeriodOfTime_beginning", curie=TIME.curie('hasBeginning'),
                   model_uri=STRENDCAT_BIOCATALYSIS.PeriodOfTime_beginning, domain=PeriodOfTime, range=Optional[Union[dict, "TimeInstant"]])

slots.PeriodOfTime_end = Slot(uri=TIME.hasEnd, name="PeriodOfTime_end", curie=TIME.curie('hasEnd'),
                   model_uri=STRENDCAT_BIOCATALYSIS.PeriodOfTime_end, domain=PeriodOfTime, range=Optional[Union[dict, "TimeInstant"]])

slots.PeriodOfTime_end_date = Slot(uri=DCAT.endDate, name="PeriodOfTime_end_date", curie=DCAT.curie('endDate'),
                   model_uri=STRENDCAT_BIOCATALYSIS.PeriodOfTime_end_date, domain=PeriodOfTime, range=Optional[Union[str, XSDDate]])

slots.PeriodOfTime_start_date = Slot(uri=DCAT.startDate, name="PeriodOfTime_start_date", curie=DCAT.curie('startDate'),
                   model_uri=STRENDCAT_BIOCATALYSIS.PeriodOfTime_start_date, domain=PeriodOfTime, range=Optional[Union[str, XSDDate]])

slots.QualitativeAttribute_value = Slot(uri=PROV.value, name="QualitativeAttribute_value", curie=PROV.curie('value'),
                   model_uri=STRENDCAT_BIOCATALYSIS.QualitativeAttribute_value, domain=QualitativeAttribute, range=str)

slots.QuantitativeAttribute_value = Slot(uri=PROV.value, name="QuantitativeAttribute_value", curie=PROV.curie('value'),
                   model_uri=STRENDCAT_BIOCATALYSIS.QuantitativeAttribute_value, domain=QuantitativeAttribute, range=float)

slots.Relationship_had_role = Slot(uri=DCAT.hadRole, name="Relationship_had_role", curie=DCAT.curie('hadRole'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Relationship_had_role, domain=Relationship, range=Union[Union[dict, "Role"], list[Union[dict, "Role"]]])

slots.Relationship_relation = Slot(uri=DCTERMS.relation, name="Relationship_relation", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Relationship_relation, domain=Relationship, range=Union[dict[Union[str, ResourceId], Union[dict, "Resource"]], list[Union[dict, "Resource"]]])

slots.Software_has_part = Slot(uri=DCTERMS.hasPart, name="Software_has_part", curie=DCTERMS.curie('hasPart'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Software_has_part, domain=Software, range=Optional[Union[dict[Union[str, SoftwareId], Union[dict, "Software"]], list[Union[dict, "Software"]]]])

slots.Software_other_identifier = Slot(uri=ADMS.identifier, name="Software_other_identifier", curie=ADMS.curie('identifier'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Software_other_identifier, domain=Software, range=Optional[Union[Union[dict, "Identifier"], list[Union[dict, "Identifier"]]]])

slots.ChemicalEntity_has_part = Slot(uri=BFO['0000051'], name="ChemicalEntity_has_part", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ChemicalEntity_has_part, domain=ChemicalEntity, range=Optional[Union[dict[Union[str, ChemicalEntityId], Union[dict, "ChemicalEntity"]], list[Union[dict, "ChemicalEntity"]]]])

slots.Atom_rdf_type = Slot(uri=RDF.type, name="Atom_rdf_type", curie=RDF.curie('type'),
                   model_uri=STRENDCAT_BIOCATALYSIS.Atom_rdf_type, domain=Atom, range=Union[dict, DefinedTerm])

slots.ChemicalReaction_has_temperature = Slot(uri=SIO['000008'], name="ChemicalReaction_has_temperature", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ChemicalReaction_has_temperature, domain=ChemicalReaction, range=Optional[Union[Union[dict, "Temperature"], list[Union[dict, "Temperature"]]]])

slots.ChemicalReaction_has_pressure = Slot(uri=SIO['000008'], name="ChemicalReaction_has_pressure", curie=SIO.curie('000008'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ChemicalReaction_has_pressure, domain=ChemicalReaction, range=Optional[Union[Union[dict, "Pressure"], list[Union[dict, "Pressure"]]]])

slots.ChemicalReaction_related_resource = Slot(uri=DCTERMS.relation, name="ChemicalReaction_related_resource", curie=DCTERMS.curie('relation'),
                   model_uri=STRENDCAT_BIOCATALYSIS.ChemicalReaction_related_resource, domain=ChemicalReaction, range=Optional[Union[dict[Union[str, ResourceId], Union[dict, Resource]], list[Union[dict, Resource]]]])

slots.MaterialEntity_has_part = Slot(uri=BFO['0000051'], name="MaterialEntity_has_part", curie=BFO.curie('0000051'),
                   model_uri=STRENDCAT_BIOCATALYSIS.MaterialEntity_has_part, domain=MaterialEntity, range=Optional[Union[dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], list[Union[dict, "MaterialEntity"]]]])

slots.MaterialSample_derived_from = Slot(uri=PROV.wasDerivedFrom, name="MaterialSample_derived_from", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=STRENDCAT_BIOCATALYSIS.MaterialSample_derived_from, domain=MaterialSample, range=Optional[Union[dict, Entity]])
