# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "StructureCreatePlanParams",
    "Plan",
    "PlanStep",
    "PlanStepEnhancePropertyArgs",
    "PlanStepEnhanceRelationshipArgs",
    "PlanStepFindRelationshipArgs",
]


class StructureCreatePlanParams(TypedDict, total=False):
    dataset: Required[str]

    plan: Required[Plan]


class PlanStepEnhancePropertyArgs(TypedDict, total=False):
    entity_id: Required[str]

    property_name: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]


class PlanStepEnhanceRelationshipArgs(TypedDict, total=False):
    entity_id: Required[str]

    relationship_name: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]


class PlanStepFindRelationshipArgs(TypedDict, total=False):
    relationship_name: Required[str]

    source_entity_id: Required[str]

    target_entity_id: Required[str]

    allow_extra_entities: bool

    starting_searches: List[str]

    starting_urls: List[str]


PlanStep: TypeAlias = Union[
    Iterable[object], PlanStepEnhancePropertyArgs, PlanStepEnhanceRelationshipArgs, PlanStepFindRelationshipArgs
]


class Plan(TypedDict, total=False):
    steps: Required[Iterable[PlanStep]]
