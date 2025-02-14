# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "StructureListPlansResponse",
    "StructureListPlansResponseItem",
    "StructureListPlansResponseItemPlan",
    "StructureListPlansResponseItemPlanStep",
    "StructureListPlansResponseItemPlanStepParallel",
    "StructureListPlansResponseItemPlanStepEnhanceProperty",
    "StructureListPlansResponseItemPlanStepEnhancePropertyEnhanceProperty",
    "StructureListPlansResponseItemPlanStepEnhanceRelationship",
    "StructureListPlansResponseItemPlanStepEnhanceRelationshipEnhanceRelationship",
    "StructureListPlansResponseItemPlanStepFindRelationship",
    "StructureListPlansResponseItemPlanStepFindRelationshipFindRelationship",
]


class StructureListPlansResponseItemPlanStepParallel(BaseModel):
    parallel: List[object] = FieldInfo(alias="Parallel")


class StructureListPlansResponseItemPlanStepEnhancePropertyEnhanceProperty(BaseModel):
    entity_id: str

    property_name: str

    allow_extra_entities: Optional[bool] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None


class StructureListPlansResponseItemPlanStepEnhanceProperty(BaseModel):
    enhance_property: StructureListPlansResponseItemPlanStepEnhancePropertyEnhanceProperty = FieldInfo(
        alias="EnhanceProperty"
    )


class StructureListPlansResponseItemPlanStepEnhanceRelationshipEnhanceRelationship(BaseModel):
    entity_id: str

    relationship_name: str

    allow_extra_entities: Optional[bool] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None


class StructureListPlansResponseItemPlanStepEnhanceRelationship(BaseModel):
    enhance_relationship: StructureListPlansResponseItemPlanStepEnhanceRelationshipEnhanceRelationship = FieldInfo(
        alias="EnhanceRelationship"
    )


class StructureListPlansResponseItemPlanStepFindRelationshipFindRelationship(BaseModel):
    relationship_name: str

    source_entity_id: str

    target_entity_id: str

    allow_extra_entities: Optional[bool] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None


class StructureListPlansResponseItemPlanStepFindRelationship(BaseModel):
    find_relationship: StructureListPlansResponseItemPlanStepFindRelationshipFindRelationship = FieldInfo(
        alias="FindRelationship"
    )


StructureListPlansResponseItemPlanStep: TypeAlias = Union[
    StructureListPlansResponseItemPlanStepParallel,
    StructureListPlansResponseItemPlanStepEnhanceProperty,
    StructureListPlansResponseItemPlanStepEnhanceRelationship,
    StructureListPlansResponseItemPlanStepFindRelationship,
]


class StructureListPlansResponseItemPlan(BaseModel):
    steps: List[StructureListPlansResponseItemPlanStep]


class StructureListPlansResponseItem(BaseModel):
    plan: StructureListPlansResponseItemPlan

    plan_id: str

    status: Literal["Running", "StartingNextStep", "Completed", "Canceled"]

    step: int


StructureListPlansResponse: TypeAlias = List[StructureListPlansResponseItem]
