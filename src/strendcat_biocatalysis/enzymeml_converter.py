"""Translate EnzymeML v2 data documents into strendcat_biocatalysis (BioDCAT) records.

This module reads an EnzymeML v2 data document (JSON or YAML, structured
according to https://github.com/EnzymeML/enzymeml-specifications) and
produces an ``EnzymeMLDocument`` instance of the strendcat_biocatalysis
LinkML model (src/strendcat_biocatalysis/schema/strendcat_biocatalysis.yaml).

EnzymeML models an experiment as a flat pool of species (Protein/Complex/
SmallMolecule) referenced by short local id strings from reactions,
modifiers and measurements. strendcat_biocatalysis models it as a PROV-style
graph of role-specific, inlined objects. Several of the mappings below are
therefore necessarily approximate or require a guess where EnzymeML simply
does not carry the information strendcat_biocatalysis needs (e.g. whether a
protein was purified or used as a crude extract, or which QUDT quantity
kind a given numeric value represents). Every such guess is logged as a
``WARNING`` with the affected id, so a run against real data yields a
searchable list of things worth checking by hand.

Usage as a script::

    python -m strendcat_biocatalysis.enzymeml_converter input.json -o output.yaml

Usage as a library::

    from strendcat_biocatalysis.enzymeml_converter import translate_document
    doc = translate_document(json.load(open("input.json")))
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from pathlib import Path
from typing import Any, Optional

import yaml

from strendcat_biocatalysis.datamodel.strendcat_biocatalysis_pydantic import (
    Biocatalyst,
    BiocatalyticComponent,
    BiocatalyticExperiment,
    BiocatalyticReaction,
    BiocatalystPreparation,
    Catalyst,
    ChemicalProduct,
    EnzymeMeasurement,
    EnzymeMeasurementSpeciesData,
    EnzymeMLCreator,
    EnzymeMLDocument,
    EquationVariable,
    InChi,
    InChIKey,
    KineticEquation,
    KineticModelParameter,
    MeasurementTimepoint,
    MolarEquivalent,
    MolecularComplex,
    PHValue,
    PurifiedEnzymePreparation,
    Reagent,
    ReactionVessel,
    SMILES,
    StartingMaterial,
    Temperature,
    Volume,
)

logger = logging.getLogger(__name__)

BASE_URI = "https://w3id.org/mvoelken-hub/StrenDCAT-Biocatalysis/enzymeml"

# =============================================================================
# Lookup tables -- adjust/extend these to taste, they are the main knobs for
# tuning conversion quality against a specific real-world dataset.
# =============================================================================

# EnzymeML UnitType (single base unit, exponent 1) -> QUDT unit URI.
# Only covers the common single-base-unit case; composite units (more than
# one base_units entry, or exponent/multiplier/scale != 1) fall back to a
# best-effort free-text notation, see _unit_to_qudt().
UNIT_TYPE_TO_QUDT: dict[str, str] = {
    "LITRE": "http://qudt.org/vocab/unit/L",
    "GRAM": "http://qudt.org/vocab/unit/GM",
    "KILOGRAM": "http://qudt.org/vocab/unit/KiloGM",
    "SECOND": "http://qudt.org/vocab/unit/SEC",
    "KELVIN": "http://qudt.org/vocab/unit/K",
    "CELSIUS": "http://qudt.org/vocab/unit/DEG_C",
    "MOLE": "http://qudt.org/vocab/unit/MOL",
    "METRE": "http://qudt.org/vocab/unit/M",
    "AMPERE": "http://qudt.org/vocab/unit/A",
    "CANDELA": "http://qudt.org/vocab/unit/CD",
    "PASCAL": "http://qudt.org/vocab/unit/PA",
    "JOULE": "http://qudt.org/vocab/unit/J",
    "WATT": "http://qudt.org/vocab/unit/W",
    "NEWTON": "http://qudt.org/vocab/unit/N",
    "HERTZ": "http://qudt.org/vocab/unit/HZ",
    "VOLT": "http://qudt.org/vocab/unit/V",
    "OHM": "http://qudt.org/vocab/unit/OHM",
    "FARAD": "http://qudt.org/vocab/unit/F",
    "HENRY": "http://qudt.org/vocab/unit/H",
    "SIEMENS": "http://qudt.org/vocab/unit/SIEMENS",
    "TESLA": "http://qudt.org/vocab/unit/T",
    "WEBER": "http://qudt.org/vocab/unit/WB",
    "LUMEN": "http://qudt.org/vocab/unit/LM",
    "LUX": "http://qudt.org/vocab/unit/LX",
    "BECQUEREL": "http://qudt.org/vocab/unit/BQ",
    "GRAY": "http://qudt.org/vocab/unit/GY",
    "SIEVERT": "http://qudt.org/vocab/unit/SV",
    "KATAL": "http://qudt.org/vocab/unit/KAT",
    "RADIAN": "http://qudt.org/vocab/unit/RAD",
    "STERADIAN": "http://qudt.org/vocab/unit/SR",
    "COULOMB": "http://qudt.org/vocab/unit/C",
    "DIMENSIONLESS": "http://qudt.org/vocab/unit/UNITLESS",
    "ITEM": "http://qudt.org/vocab/unit/NUM",
}

# EnzymeML DataTypes -> QUDT quantity kind URI, used for MeasurementData
# values (and, transitively, for the individual MeasurementTimepoints
# derived from them) where the *only* signal available is this enum.
DATA_TYPE_TO_QUANTITY_KIND: dict[str, str] = {
    "CONCENTRATION": "http://qudt.org/vocab/quantitykind/AmountOfSubstanceConcentration",
    "AMOUNT": "http://qudt.org/vocab/quantitykind/AmountOfSubstance",
    "CONVERSION": "http://qudt.org/vocab/quantitykind/DimensionlessRatio",
    "YIELD": "http://qudt.org/vocab/quantitykind/DimensionlessRatio",
    "TRANSMITTANCE": "http://qudt.org/vocab/quantitykind/DimensionlessRatio",
    # Absorbance/Fluorescence/PeakArea/Turnover have no single obvious QUDT
    # quantity kind -- deliberately left unmapped, see _quantity_kind_for().
}

# Fixed QUDT quantity kinds for slots where *we* (not the source data) know
# exactly what physical quantity is represented.
QK_VOLUME = "http://qudt.org/vocab/quantitykind/Volume"
QK_TEMPERATURE = "http://qudt.org/vocab/quantitykind/Temperature"
QK_MOLAR_EQUIVALENT = "http://qudt.org/vocab/quantitykind/DimensionlessRatio"

# Honest placeholder used whenever no quantity kind can be determined.
# Deliberately NOT a real QUDT term -- a wrong-but-plausible-looking QUDT URI
# would silently claim false precision. Always paired with a logged warning.
UNMAPPED_QUANTITY_KIND = "strendcat_biocatalysis:UnmappedQuantityKind"

# EnzymeML ModifierRole -> strendcat_biocatalysis ComponentRoleEnum. Roles
# with no listed target are handled specially (BIOCATALYST -> used_catalyst,
# not a component role at all).
MODIFIER_ROLE_TO_COMPONENT_ROLE: dict[str, str] = {
    "ACTIVATOR": "Activator",
    "ADDITIVE": "Other",
    "BUFFER": "Buffer",
    "CATALYST": "AuxiliaryCatalyst",
    "INHIBITOR": "Inhibitor",
    "SOLVENT": "Solvent",
}

EQUATION_TYPE_MAP: dict[str, str] = {
    "ASSIGNMENT": "Assignment",
    "INITIAL_ASSIGNMENT": "InitialAssignment",
    "ODE": "ODE",
    "RATE_LAW": "RateLaw",
}

APPLICATION_FORM_DEFAULT = "PurifiedEnzyme"
OPERATION_MODE_DEFAULT = "Batch"


# =============================================================================
# Small helpers
# =============================================================================


_URI_UNSAFE_RUN = re.compile(r"\s+")


def _mint_uri(local_id: str, kind: str) -> str:
    """Turn a short EnzymeML local id (e.g. "s0") into a schema-conformant URI.

    EnzymeML ids are usually already URL-safe short tokens, but some
    real-world documents reuse a free-text name as an id (observed for
    measurement ids) -- collapse whitespace to hyphens so the result is
    always a valid URI, since some generated identifier types (e.g.
    EnzymeMeasurementId) validate this strictly on load.
    """
    slug = _URI_UNSAFE_RUN.sub("-", local_id.strip())
    return f"{BASE_URI}/{kind}/{slug}"


def _unit_type_to_string(unit_definition: Optional[dict]) -> Optional[str]:
    """Best-effort human-readable unit string, for the plain-string time_unit slot."""
    if not unit_definition:
        return None
    if unit_definition.get("name"):
        return unit_definition["name"]
    base_units = unit_definition.get("base_units") or []
    parts = []
    for bu in base_units:
        kind = bu.get("kind", "?")
        exponent = bu.get("exponent", 1)
        parts.append(kind if exponent == 1 else f"{kind}^{exponent}")
    return "*".join(parts) if parts else None


def _unit_to_qudt(unit_definition: Optional[dict], *, context: str = "") -> Optional[str]:
    """Resolve an EnzymeML UnitDefinition to a QUDT unit URI where possible.

    Only handles the common case of a single base unit with exponent 1,
    multiplier 1 and scale 1. Anything more complex (composite units, scaled
    units) falls back to a readable free-text notation and a warning, since
    a full unit-algebra resolver is out of scope here.
    """
    if not unit_definition:
        return None
    base_units = unit_definition.get("base_units") or []
    if len(base_units) == 1:
        bu = base_units[0]
        simple = (
            bu.get("exponent", 1) == 1
            and bu.get("multiplier", 1) in (1, 1.0)
            and bu.get("scale", 1) in (1, 1.0)
        )
        qudt = UNIT_TYPE_TO_QUDT.get(bu.get("kind"))
        if simple and qudt:
            return qudt
    fallback = _unit_type_to_string(unit_definition)
    logger.warning(
        "Could not resolve unit %r to a QUDT unit URI (%s); using free-text fallback %r. "
        "Composite/scaled units are not fully resolved by this converter.",
        unit_definition,
        context or "unspecified context",
        fallback,
    )
    return fallback


def _quantity_kind_for(data_type: Optional[str], *, context: str = "") -> str:
    if data_type and data_type in DATA_TYPE_TO_QUANTITY_KIND:
        return DATA_TYPE_TO_QUANTITY_KIND[data_type]
    logger.warning(
        "No QUDT quantity kind known for data_type=%r (%s); using placeholder %r. "
        "Review and set has_quantity_type manually if this value matters.",
        data_type,
        context or "unspecified context",
        UNMAPPED_QUANTITY_KIND,
    )
    return UNMAPPED_QUANTITY_KIND


def _make_quantity(
    cls,
    value: Optional[float],
    quantity_kind: str,
    *,
    unit_definition: Optional[dict] = None,
    title: Optional[str] = None,
    context: str = "",
    **extra: Any,
):
    """Construct a QuantitativeAttribute-derived instance with a resolved unit."""
    kwargs: dict[str, Any] = {"value": value, "has_quantity_type": quantity_kind}
    qudt_unit = _unit_to_qudt(unit_definition, context=context)
    if qudt_unit:
        kwargs["unit"] = qudt_unit
    if title:
        kwargs["title"] = title
    kwargs.update(extra)
    return cls(**kwargs)


def _full_name(given_name: Optional[str], family_name: Optional[str]) -> str:
    parts = [p for p in (given_name, family_name) if p]
    return " ".join(parts) if parts else "Unknown"


# =============================================================================
# Species index -- resolves EnzymeML's flat, id-referenced species pools so
# every reference site (reactions, modifiers, complex participants,
# measurement species) can look up what kind of species it is pointing at.
# =============================================================================


class SpeciesIndex:
    """Indexes an EnzymeML document's proteins/complexes/small_molecules by id
    and memoizes their converted strendcat_biocatalysis objects, so the same
    species converts to the same (reused) object everywhere it is referenced.
    """

    def __init__(self, data: dict):
        self.raw: dict[str, tuple[str, dict]] = {}
        for p in data.get("proteins") or []:
            self.raw[p["id"]] = ("protein", p)
        for c in data.get("complexes") or []:
            self.raw[c["id"]] = ("complex", c)
        for sm in data.get("small_molecules") or []:
            self.raw[sm["id"]] = ("small_molecule", sm)
        self._biocatalysts: dict[str, Biocatalyst] = {}
        self._preparations: dict[str, BiocatalystPreparation] = {}
        self._components: dict[str, BiocatalyticComponent] = {}
        self._complexes: dict[str, MolecularComplex] = {}

    def kind_of(self, species_id: str) -> Optional[str]:
        entry = self.raw.get(species_id)
        return entry[0] if entry else None

    def biocatalyst(self, species_id: str) -> Optional[Biocatalyst]:
        if species_id not in self.raw or self.raw[species_id][0] != "protein":
            return None
        if species_id not in self._biocatalysts:
            bio, prep = convert_protein(self.raw[species_id][1])
            self._biocatalysts[species_id] = bio
            self._preparations[species_id] = prep
        return self._biocatalysts[species_id]

    def preparation(self, species_id: str) -> Optional[BiocatalystPreparation]:
        self.biocatalyst(species_id)  # ensure both are built together
        return self._preparations.get(species_id)

    def component(self, species_id: str) -> Optional[BiocatalyticComponent]:
        """A ChemicalEntity-branch representation, for SmallMolecule and
        Complex species (Complex is resolved to a MolecularComplex, not a
        BiocatalyticComponent -- see complex() below)."""
        kind = self.kind_of(species_id)
        if kind != "small_molecule":
            return None
        if species_id not in self._components:
            self._components[species_id] = convert_small_molecule(self.raw[species_id][1])
        return self._components[species_id]

    def complex(self, species_id: str) -> Optional[MolecularComplex]:
        if self.kind_of(species_id) != "complex":
            return None
        if species_id not in self._complexes:
            # Placeholder avoids infinite recursion for (unlikely) self-referencing complexes.
            self._complexes[species_id] = None
            self._complexes[species_id] = convert_complex(self.raw[species_id][1], self)
        return self._complexes[species_id]

    def all_biocatalysts(self) -> list[Biocatalyst]:
        return list(self._biocatalysts.values())

    def all_preparations(self) -> list[BiocatalystPreparation]:
        return list(self._preparations.values())

    def all_components(self) -> list[BiocatalyticComponent]:
        return list(self._components.values())

    def all_complexes(self) -> list[MolecularComplex]:
        return [c for c in self._complexes.values() if c is not None]


# =============================================================================
# Per-EnzymeML-class converters
# =============================================================================


def convert_vessel(vessel: dict) -> ReactionVessel:
    kwargs: dict[str, Any] = {
        "id": _mint_uri(vessel["id"], "vessel"),
        "title": vessel.get("name"),
    }
    if vessel.get("volume") is not None:
        kwargs["has_volume"] = [
            _make_quantity(
                Volume,
                vessel["volume"],
                QK_VOLUME,
                unit_definition=vessel.get("unit"),
                context=f"Vessel {vessel['id']} volume",
            )
        ]
    if vessel.get("constant") is not None:
        kwargs["has_constant_volume"] = vessel["constant"]
    return ReactionVessel(**kwargs)


def convert_protein(protein: dict) -> tuple[Biocatalyst, BiocatalystPreparation]:
    pid = protein["id"]
    biocatalyst = Biocatalyst(
        id=_mint_uri(pid, "biocatalyst"),
        title=protein.get("name", pid),
        is_self_produced=False,
        sequence_amino_acid=[protein["sequence"]] if protein.get("sequence") else None,
        origin_organism=[protein["organism"]] if protein.get("organism") else None,
        organism_taxonomy_id=[protein["organism_tax_id"]] if protein.get("organism_tax_id") else None,
        ec_number=[protein["ecnumber"]] if protein.get("ecnumber") else None,
    )
    logger.warning(
        "Biocatalyst %r: 'is_self_produced' has no EnzymeML equivalent, defaulted to False.",
        pid,
    )
    logger.warning(
        "Biocatalyst %r: EnzymeML does not distinguish application form; "
        "wrapping in PurifiedEnzymePreparation (application_form=%r) as a default guess.",
        pid,
        APPLICATION_FORM_DEFAULT,
    )
    preparation = PurifiedEnzymePreparation(
        id=_mint_uri(pid, "preparation"),
        application_form=APPLICATION_FORM_DEFAULT,
        derived_from=biocatalyst,
        has_constant_concentration=protein.get("constant"),
    )
    return biocatalyst, preparation


def convert_small_molecule(sm: dict) -> BiocatalyticComponent:
    sid = sm["id"]
    return BiocatalyticComponent(
        id=_mint_uri(sid, "component"),
        title=sm.get("name", sid),
        smiles=[SMILES(value=sm["canonical_smiles"])] if sm.get("canonical_smiles") else None,
        inchi=[InChi(value=sm["inchi"])] if sm.get("inchi") else None,
        inchikey=[InChIKey(value=sm["inchikey"])] if sm.get("inchikey") else None,
        synonymous_names=sm.get("synonymous_names"),
        has_constant_concentration=sm.get("constant"),
    )


def convert_complex(complex_: dict, species_index: "SpeciesIndex") -> MolecularComplex:
    cid = complex_["id"]
    participants: list = []
    for participant_id in complex_.get("participants") or []:
        kind = species_index.kind_of(participant_id)
        if kind == "protein":
            obj = species_index.biocatalyst(participant_id)
        elif kind == "small_molecule":
            obj = species_index.component(participant_id)
        elif kind == "complex":
            obj = species_index.complex(participant_id)
        else:
            obj = None
        if obj is None:
            logger.warning(
                "MolecularComplex %r: participant %r could not be resolved and was skipped.",
                cid,
                participant_id,
            )
            continue
        participants.append(obj)
    return MolecularComplex(
        id=_mint_uri(cid, "complex"),
        title=complex_.get("name", cid),
        has_complex_participant=participants or None,
        has_constant_concentration=complex_.get("constant"),
    )


def _resolve_species_as_chemical(species_id: str, species_index: SpeciesIndex, *, context: str):
    """Resolve a species id to whichever ChemicalEntity-branch object represents
    it (BiocatalyticComponent for small molecules, MolecularComplex for
    complexes). Proteins are handled separately by callers (used_catalyst),
    since they are not ChemicalEntity-branch objects."""
    kind = species_index.kind_of(species_id)
    if kind == "small_molecule":
        return species_index.component(species_id)
    if kind == "complex":
        return species_index.complex(species_id)
    logger.warning(
        "%s: species %r is not a small molecule or complex (kind=%r); skipped.",
        context,
        species_id,
        kind,
    )
    return None


def _wrap_reaction_element(cls, element: dict, species_index: SpeciesIndex, *, role: str, rid: str, context: str):
    """Wrap a resolved species into a Reagent/ChemicalProduct/StartingMaterial
    identity+stoichiometry record. NOTE: these wrapper classes have no
    chemical-descriptor slots (inchi/smiles/...) -- the full descriptors live
    on the BiocatalyticComponent objects reachable via
    BiocatalyticExperiment.has_biocatalytic_component. This wrapper only
    carries identity and stoichiometry.
    """
    species_id = element["species_id"]
    resolved = _resolve_species_as_chemical(species_id, species_index, context=context)
    title = resolved.title if resolved is not None else species_id
    kwargs: dict[str, Any] = {"id": _mint_uri(f"{species_id}-{rid}-{role}", "reaction-element"), "title": title}
    # ChemicalProduct has no has_molar_equivalent slot (only Reagent/StartingMaterial/
    # Catalyst/DissolvingSubstance do) -- stoichiometry of products is not carried.
    if cls is ChemicalProduct:
        if element.get("stoichiometry") is not None:
            logger.info(
                "%s: stoichiometry (%s) not carried -- ChemicalProduct has no "
                "has_molar_equivalent slot.",
                context,
                element["stoichiometry"],
            )
        return cls(**kwargs)
    if element.get("stoichiometry") is not None:
        logger.info(
            "%s: mapping EnzymeML stoichiometry (%s) to has_molar_equivalent as an "
            "approximation -- the two concepts are related but not identical.",
            context,
            element["stoichiometry"],
        )
        kwargs["has_molar_equivalent"] = [
            _make_quantity(
                MolarEquivalent,
                abs(element["stoichiometry"]),
                QK_MOLAR_EQUIVALENT,
                context=context,
            )
        ]
    return cls(**kwargs)


def convert_equation(equation: dict) -> KineticEquation:
    variables = [
        EquationVariable(value=v["symbol"], title=v.get("name"))
        for v in equation.get("variables") or []
    ]
    equation_type = equation.get("equation_type")
    return KineticEquation(
        value=equation["equation"],
        equation_species_reference=[equation["species_id"]] if equation.get("species_id") else None,
        equation_type=EQUATION_TYPE_MAP.get(equation_type) if equation_type else None,
        has_equation_variable=variables or None,
    )


def convert_parameter(parameter: dict) -> KineticModelParameter:
    quantity_kind = UNMAPPED_QUANTITY_KIND
    logger.warning(
        "KineticModelParameter %r (symbol=%r): fitted/kinetic parameters have no reliable "
        "QUDT quantity kind derivable from EnzymeML alone; using placeholder. Set "
        "has_quantity_type manually for parameters that matter (e.g. Km -> "
        "AmountOfSubstanceConcentration, kcat -> Frequency).",
        parameter.get("id"),
        parameter.get("symbol"),
    )
    return _make_quantity(
        KineticModelParameter,
        parameter.get("value"),
        quantity_kind,
        unit_definition=parameter.get("unit"),
        title=parameter.get("name"),
        context=f"Parameter {parameter.get('id')}",
        parameter_symbol=[parameter["symbol"]] if parameter.get("symbol") else None,
        initial_value=parameter.get("initial_value"),
        upper_bound=parameter.get("upper_bound"),
        lower_bound=parameter.get("lower_bound"),
        stderr=parameter.get("stderr"),
        is_fitted=parameter.get("fit"),
        is_fixed_parameter=parameter.get("constant"),
    )


def convert_measurement_data(species_data: dict, species_index: SpeciesIndex) -> EnzymeMeasurementSpeciesData:
    species_id = species_data["species_id"]
    resolved = _resolve_species_as_chemical(
        species_id, species_index, context=f"MeasurementData {species_id}"
    )
    data_type = species_data.get("data_type")
    quantity_kind = _quantity_kind_for(data_type, context=f"MeasurementData {species_id}")

    time_unit_str = _unit_type_to_string(species_data.get("time_unit"))
    timepoints = []
    values = species_data.get("data") or []
    times = species_data.get("time") or []
    for value, time in zip(values, times):
        timepoints.append(
            MeasurementTimepoint(
                value=value,
                has_quantity_type=quantity_kind,
                has_time_value=[time],
                time_unit=[time_unit_str] if time_unit_str else None,
            )
        )
    if len(values) != len(times):
        logger.warning(
            "MeasurementData %r: data (%d points) and time (%d points) have different "
            "lengths; only the first %d pairs were used.",
            species_id,
            len(values),
            len(times),
            len(timepoints),
        )

    # EnzymeMeasurementSpeciesData.value (inherited from QuantitativeAttribute) is not
    # semantically used here -- has_timepoint carries the actual series -- and the schema
    # marks it slot_usage required:false accordingly. The generated dataclass still enforces
    # QuantitativeAttribute's own required check on super().__post_init__() regardless, so
    # mirror initial_amount (or the first timepoint) into it to satisfy that redundant check.
    value = species_data.get("initial")
    if value is None and values:
        value = values[0]

    return EnzymeMeasurementSpeciesData(
        value=value,
        measured_species_reference=[resolved.title if resolved is not None else species_id],
        prepared_amount=species_data.get("prepared"),
        initial_amount=species_data.get("initial"),
        measurement_data_type=data_type.title().replace("_", "") if data_type else None,
        is_simulated=species_data.get("is_simulated"),
        has_timepoint=timepoints or None,
        has_quantity_type=quantity_kind,
    )


def convert_measurement(measurement: dict, species_index: SpeciesIndex) -> EnzymeMeasurement:
    kwargs: dict[str, Any] = {
        "id": _mint_uri(measurement["id"], "measurement"),
        "title": [measurement.get("name", measurement["id"])],
        "measurement_group_id": [measurement["group_id"]] if measurement.get("group_id") else None,
    }
    if measurement.get("ph") is not None:
        kwargs["has_ph_value"] = [
            PHValue(
                value=measurement["ph"],
                has_quantity_type="http://qudt.org/vocab/quantitykind/DimensionlessRatio",
            )
        ]
    if measurement.get("temperature") is not None:
        kwargs["has_temperature"] = [
            _make_quantity(
                Temperature,
                measurement["temperature"],
                QK_TEMPERATURE,
                unit_definition=measurement.get("temperature_unit"),
                context=f"Measurement {measurement['id']} temperature",
            )
        ]
    species_data = [
        convert_measurement_data(sd, species_index) for sd in measurement.get("species_data") or []
    ]
    if species_data:
        kwargs["has_measurement_species_data"] = species_data
    return EnzymeMeasurement(**kwargs)


def convert_creator(creator: dict) -> EnzymeMLCreator:
    return EnzymeMLCreator(
        name=[_full_name(creator.get("given_name"), creator.get("family_name"))],
        given_name=[creator["given_name"]] if creator.get("given_name") else None,
        family_name=[creator["family_name"]] if creator.get("family_name") else None,
        mail=[creator["mail"]] if creator.get("mail") else None,
    )


def convert_reaction(
    reaction: dict,
    species_index: SpeciesIndex,
    *,
    equations: list[dict],
    parameters: list[dict],
) -> BiocatalyticReaction:
    rid = reaction["id"]
    kwargs: dict[str, Any] = {
        "id": _mint_uri(rid, "reaction"),
        "title": [reaction.get("name", rid)],
        "is_reversible": reaction.get("reversible"),
    }

    used_reactant = [
        _wrap_reaction_element(Reagent, el, species_index, role="reactant", rid=rid, context=f"Reaction {rid} reactant")
        for el in reaction.get("reactants") or []
    ]
    if used_reactant:
        kwargs["used_reactant"] = used_reactant
    generated_product = [
        _wrap_reaction_element(ChemicalProduct, el, species_index, role="product", rid=rid, context=f"Reaction {rid} product")
        for el in reaction.get("products") or []
    ]
    if generated_product:
        kwargs["generated_product"] = generated_product

    catalysts = []
    for modifier in reaction.get("modifiers") or []:
        result = convert_modifier(modifier, species_index, rid=rid)
        if result is not None and result[0] == "catalyst":
            catalysts.append(result[1])
    if catalysts:
        kwargs["used_catalyst"] = catalysts

    reaction_equations = []
    if reaction.get("kinetic_law"):
        reaction_equations.append(convert_equation(reaction["kinetic_law"]))
    reaction_equations.extend(convert_equation(eq) for eq in equations)
    if reaction_equations:
        kwargs["has_kinetic_equation"] = reaction_equations

    reaction_parameters = [convert_parameter(p) for p in parameters]
    if reaction_parameters:
        kwargs["has_kinetic_model_parameter"] = reaction_parameters

    return BiocatalyticReaction(**kwargs)


def convert_modifier(modifier: dict, species_index: SpeciesIndex, *, rid: str):
    """Returns ("catalyst", Catalyst) for a BIOCATALYST modifier, or
    ("component", BiocatalyticComponent) for any other role, or None if the
    species could not be resolved."""
    species_id = modifier["species_id"]
    role = modifier.get("role")
    if role == "BIOCATALYST":
        bio = species_index.biocatalyst(species_id)
        if bio is None:
            logger.warning(
                "Modifier %r has role BIOCATALYST but is not a Protein (kind=%r); skipped.",
                species_id,
                species_index.kind_of(species_id),
            )
            return None
        catalyst = Catalyst(
            id=_mint_uri(f"{species_id}-{rid}-catalyst", "reaction-element"),
            title=bio.title,
        )
        return ("catalyst", catalyst)

    resolved = _resolve_species_as_chemical(species_id, species_index, context=f"Modifier {species_id}")
    if resolved is None:
        return None
    if isinstance(resolved, MolecularComplex):
        # MolecularComplex has no has_component_role slot -- the modifier role
        # cannot be recorded for a complex, only for its individual participants.
        return ("complex", resolved)
    component_role = MODIFIER_ROLE_TO_COMPONENT_ROLE.get(role)
    if component_role is None:
        logger.warning("Modifier %r: unrecognised role %r, defaulting to 'Other'.", species_id, role)
        component_role = "Other"
    resolved.has_component_role = component_role
    return ("component", resolved)


# =============================================================================
# Top-level orchestration
# =============================================================================


def translate_document(data: dict) -> EnzymeMLDocument:
    """Translate a parsed EnzymeML v2 document (as a plain dict) into an
    EnzymeMLDocument instance of the strendcat_biocatalysis model."""
    doc_name = data.get("name", "unnamed-enzymeml-document")
    species_index = SpeciesIndex(data)

    vessels = [convert_vessel(v) for v in data.get("vessels") or []]

    # Build all species up front so every reference site reuses the same object.
    for p in data.get("proteins") or []:
        species_index.biocatalyst(p["id"])
    for sm in data.get("small_molecules") or []:
        species_index.component(sm["id"])
    for c in data.get("complexes") or []:
        species_index.complex(c["id"])

    all_components: list = list(species_index.all_components())
    all_complexes: list = list(species_index.all_complexes())
    for modifier_owner_reaction in data.get("reactions") or []:
        for modifier in modifier_owner_reaction.get("modifiers") or []:
            result = convert_modifier(modifier, species_index, rid=modifier_owner_reaction["id"])
            if result is None:
                continue
            kind, obj = result
            if kind == "component" and obj not in all_components:
                all_components.append(obj)
            elif kind == "complex" and obj not in all_complexes:
                all_complexes.append(obj)

    reactions_raw = data.get("reactions") or []
    all_equations = data.get("equations") or []
    all_parameters = data.get("parameters") or []
    if len(reactions_raw) != 1 and (all_equations or all_parameters):
        logger.warning(
            "Document has %d reactions but document-level equations/parameters are not "
            "reaction-scoped in EnzymeML; they were not auto-attached to any reaction. "
            "Attach them manually via has_kinetic_equation/has_kinetic_model_parameter.",
            len(reactions_raw),
        )
        all_equations, all_parameters = [], []

    reactions = [
        convert_reaction(
            r,
            species_index,
            equations=all_equations if len(reactions_raw) == 1 else [],
            parameters=all_parameters if len(reactions_raw) == 1 else [],
        )
        for r in reactions_raw
    ]

    measurements = [convert_measurement(m, species_index) for m in data.get("measurements") or []]

    if not reactions:
        logger.warning("Document %r has no reactions; BiocatalyticReaction list will be empty.", doc_name)

    if len(vessels) > 1:
        logger.warning(
            "Document has %d vessels but used_reaction_vessel is single-valued; only the "
            "first (%s) was kept.",
            len(vessels),
            vessels[0].id,
        )
    logger.warning(
        "BiocatalyticExperiment %r: 'has_operation_mode' has no EnzymeML equivalent, "
        "defaulted to %r.",
        doc_name,
        OPERATION_MODE_DEFAULT,
    )
    if len(reactions) > 1:
        logger.warning(
            "Document has %d reactions but BiocatalyticExperiment.evaluated_activity is "
            "single-valued; only the first (%s) was kept.",
            len(reactions),
            reactions[0].id,
        )
    experiment = BiocatalyticExperiment(
        id=_mint_uri(doc_name, "experiment"),
        title=[doc_name],
        has_operation_mode=OPERATION_MODE_DEFAULT,
        used_biocatalyst_preparation=species_index.all_preparations() or None,
        has_biocatalytic_component=all_components or None,
        has_molecular_complex=all_complexes or None,
        used_reaction_vessel=[vessels[0]] if vessels else None,
        evaluated_activity=reactions[0] if reactions else None,
        has_enzyme_measurement=measurements or None,
    )

    creators = [convert_creator(c) for c in data.get("creators") or []]
    if not creators:
        logger.warning("Document %r has no creators; EnzymeMLDocument.creator is recommended and left empty.", doc_name)

    return EnzymeMLDocument(
        id=_mint_uri(doc_name, "document"),
        title=[doc_name],
        description=[data.get("description") or f"Converted from EnzymeML document {doc_name!r}."],
        version=data.get("version"),
        release_date=data.get("created"),
        modification_date=data.get("modified"),
        creator=creators,
        was_generated_by=[experiment],
        is_about_activity=reactions or None,
    )


# =============================================================================
# I/O and CLI
# =============================================================================


def load_enzymeml_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    if path.suffix.lower() in (".yaml", ".yml"):
        return yaml.safe_load(text)
    raise ValueError(f"Unsupported input file extension: {path.suffix!r} (expected .json/.yaml/.yml)")


def _flatten_value_only_dicts(obj: Any) -> Any:
    """Work around a linkml_runtime yaml_loader bug (confirmed against
    linkml-runtime==1.10.0): a multivalued, inlined slot whose range is a
    bare {value: ...} wrapper class (InChi, InChIKey, SMILES, ...) fails to
    round-trip when serialized -- as pydantic naturally does -- as a list of
    single-key {"value": x} dicts; yaml_loader's _normalize_inlined
    misconstructs the wrapper from the whole dict instead of just x. A list
    of bare scalars is the form yaml_loader parses correctly, and the same
    wrapper class reconstructs identically from either shape on load.

    Trade-off (deliberate, confirmed with the project maintainer): the bare
    scalar form is not what the schema formally declares (range: InChi, a
    class/object type), so `just test`'s separate `_test-examples` step
    (JSON Schema validation via linkml-run-examples) rejects it with "is not
    of type 'object'" for these three slots. There is currently no single
    on-disk shape that satisfies both linkml_runtime's dataclass loader and
    its JSON Schema generator for this pattern -- pytest (`_test-python`) was
    prioritized since that's the check this converter's output is meant to
    satisfy. Revisit if a future linkml_runtime release fixes the
    _normalize_inlined bug (see git history around this function for the
    reproduction), which would let this workaround be removed entirely.
    """
    if isinstance(obj, dict):
        return {k: _flatten_value_only_dicts(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [
            item["value"] if isinstance(item, dict) and list(item) == ["value"] else _flatten_value_only_dicts(item)
            for item in obj
        ]
    return obj


def dump_biodcat(doc: EnzymeMLDocument, path: Path) -> None:
    data = doc.model_dump(exclude_none=True, mode="json")
    data = _flatten_value_only_dicts(data)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="EnzymeML v2 document (.json, .yaml or .yml)")
    parser.add_argument("-o", "--output", type=Path, default=None, help="Output YAML path (default: stdout)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable INFO-level logging")
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s: %(message)s")

    data = load_enzymeml_file(args.input)
    doc = translate_document(data)

    if args.output:
        dump_biodcat(doc, args.output)
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        print(yaml.safe_dump(doc.model_dump(exclude_none=True, mode="json"), sort_keys=False, allow_unicode=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
