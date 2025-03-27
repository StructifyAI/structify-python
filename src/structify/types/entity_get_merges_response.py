# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "EntityGetMergesResponse",
    "EntityGetMergesResponseItem",
    "EntityGetMergesResponseItemEntityA",
    "EntityGetMergesResponseItemEntityAProperties",
    "EntityGetMergesResponseItemEntityB",
    "EntityGetMergesResponseItemEntityBProperties",
    "EntityGetMergesResponseItemMatchedProperty",
]

EntityGetMergesResponseItemEntityAProperties: TypeAlias = Union[str, bool, float, Image]


class EntityGetMergesResponseItemEntityA(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntityGetMergesResponseItemEntityAProperties]

    updated_at: datetime


EntityGetMergesResponseItemEntityBProperties: TypeAlias = Union[str, bool, float, Image]


class EntityGetMergesResponseItemEntityB(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntityGetMergesResponseItemEntityBProperties]

    updated_at: datetime


class EntityGetMergesResponseItemMatchedProperty(BaseModel):
    match_prob: float

    match_transfer_prob: float

    name: str

    property_cardinality: int

    unique: bool


class EntityGetMergesResponseItem(BaseModel):
    alternate_matches: List[object]
    """Alternate matches for entity a - just used for dataset eval"""

    baseline_cardinality: int

    entity_a: EntityGetMergesResponseItemEntityA

    entity_b: EntityGetMergesResponseItemEntityB

    matched_properties: List[EntityGetMergesResponseItemMatchedProperty]

    p_match: float

    p_match_threshold: float


EntityGetMergesResponse: TypeAlias = List[EntityGetMergesResponseItem]
