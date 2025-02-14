# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "StructureListPlansResponse",
    "StructureListPlansResponseItem",
    "StructureListPlansResponseItemPlan",
    "StructureListPlansResponseItemPlanStep",
    "StructureListPlansResponseItemPlanStepEnhancePropertyArgs",
    "StructureListPlansResponseItemPlanStepEnhanceRelationshipArgs",
    "StructureListPlansResponseItemPlanStepFindRelationshipArgs",
]


class StructureListPlansResponseItemPlanStepEnhancePropertyArgs(BaseModel):
    entity_id: str

    property_name: str

    allow_extra_entities: Optional[bool] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None


class StructureListPlansResponseItemPlanStepEnhanceRelationshipArgs(BaseModel):
    entity_id: str

    relationship_name: str

    allow_extra_entities: Optional[bool] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None


class StructureListPlansResponseItemPlanStepFindRelationshipArgs(BaseModel):
    relationship_name: str

    source_entity_id: str

    target_entity_id: str

    allow_extra_entities: Optional[bool] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None


StructureListPlansResponseItemPlanStep: TypeAlias = Union[
    List[object],
    StructureListPlansResponseItemPlanStepEnhancePropertyArgs,
    StructureListPlansResponseItemPlanStepEnhanceRelationshipArgs,
    StructureListPlansResponseItemPlanStepFindRelationshipArgs,
]


class StructureListPlansResponseItemPlan(BaseModel):
    steps: List[StructureListPlansResponseItemPlanStep]


class StructureListPlansResponseItem(BaseModel):
    plan: StructureListPlansResponseItemPlan

    plan_id: str

    status: Literal["Running", "StartingNextStep", "Completed", "Canceled"]

    step: int


StructureListPlansResponse: TypeAlias = List[StructureListPlansResponseItem]
