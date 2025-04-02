# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "EntityMatch",
    "EntityA",
    "EntityAProperties",
    "EntityB",
    "EntityBProperties",
    "MatchedProperty",
    "CardinalityOverride",
]

EntityAProperties: TypeAlias = Union[str, bool, float, Image]


class EntityA(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntityAProperties]

    updated_at: datetime


EntityBProperties: TypeAlias = Union[str, bool, float, Image]


class EntityB(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntityBProperties]

    updated_at: datetime


class MatchedProperty(BaseModel):
    match_prob: float

    match_transfer_prob: float

    name: str

    property_cardinality: int

    unique: bool


class CardinalityOverride(BaseModel):
    cardinality: int

    entity_id: str

    relationship_name: str


class EntityMatch(BaseModel):
    baseline_cardinality: int

    entity_a: EntityA

    entity_b: EntityB

    matched_properties: List[MatchedProperty]

    p_match: float

    p_match_threshold: float

    cardinality_override: Optional[CardinalityOverride] = None
