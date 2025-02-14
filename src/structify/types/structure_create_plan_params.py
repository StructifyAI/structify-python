# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "StructureCreatePlanParams",
    "Plan",
    "PlanStep",
    "PlanStepParallel",
    "PlanStepEnhanceProperty",
    "PlanStepEnhancePropertyEnhanceProperty",
    "PlanStepEnhanceRelationship",
    "PlanStepEnhanceRelationshipEnhanceRelationship",
    "PlanStepFindRelationship",
    "PlanStepFindRelationshipFindRelationship",
]


class StructureCreatePlanParams(TypedDict, total=False):
    dataset: Required[str]

    plan: Required[Plan]


class PlanStepParallel(TypedDict, total=False):
    parallel: Required[Annotated[Iterable[object], PropertyInfo(alias="Parallel")]]


class PlanStepEnhancePropertyEnhanceProperty(TypedDict, total=False):
    entity_id: Required[str]

    property_name: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]


class PlanStepEnhanceProperty(TypedDict, total=False):
    enhance_property: Required[Annotated[PlanStepEnhancePropertyEnhanceProperty, PropertyInfo(alias="EnhanceProperty")]]


class PlanStepEnhanceRelationshipEnhanceRelationship(TypedDict, total=False):
    entity_id: Required[str]

    relationship_name: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]


class PlanStepEnhanceRelationship(TypedDict, total=False):
    enhance_relationship: Required[
        Annotated[PlanStepEnhanceRelationshipEnhanceRelationship, PropertyInfo(alias="EnhanceRelationship")]
    ]


class PlanStepFindRelationshipFindRelationship(TypedDict, total=False):
    relationship_name: Required[str]

    source_entity_id: Required[str]

    target_entity_id: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]


class PlanStepFindRelationship(TypedDict, total=False):
    find_relationship: Required[
        Annotated[PlanStepFindRelationshipFindRelationship, PropertyInfo(alias="FindRelationship")]
    ]


PlanStep: TypeAlias = Union[
    PlanStepParallel, PlanStepEnhanceProperty, PlanStepEnhanceRelationship, PlanStepFindRelationship
]


class Plan(TypedDict, total=False):
    steps: Required[Iterable[PlanStep]]
