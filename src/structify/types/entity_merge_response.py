# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = [
    "EntityMergeResponse",
    "MatchObject",
    "MatchObjectEntityA",
    "MatchObjectEntityAProperties",
    "MatchObjectEntityB",
    "MatchObjectEntityBProperties",
    "MatchObjectMatchedProperty",
]

MatchObjectEntityAProperties: TypeAlias = Union[str, bool, float, Image]


class MatchObjectEntityA(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, MatchObjectEntityAProperties]

    updated_at: datetime


MatchObjectEntityBProperties: TypeAlias = Union[str, bool, float, Image]


class MatchObjectEntityB(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, MatchObjectEntityBProperties]

    updated_at: datetime


class MatchObjectMatchedProperty(BaseModel):
    match_prob: float

    match_transfer_prob: float

    name: str

    property_cardinality: int

    unique: bool


class MatchObject(BaseModel):
    alternate_matches: List[object]
    """Alternate matches for entity a - just used for dataset eval"""

    baseline_cardinality: int

    entity_a: MatchObjectEntityA

    entity_b: MatchObjectEntityB

    matched_properties: List[MatchObjectMatchedProperty]

    p_match: float

    p_match_threshold: float


class EntityMergeResponse(BaseModel):
    match_object: Optional[MatchObject] = None

    merged_entity_id: Optional[str] = None
