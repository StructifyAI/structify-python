# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["EntityMatch", "EntityA", "EntityAProperties", "EntityB", "EntityBProperties", "MatchedProperty"]

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


class EntityMatch(BaseModel):
    alternate_matches: List["EntityMatch"]
    """Alternate matches for entity a - just used for dataset eval"""

    baseline_cardinality: int

    entity_a: EntityA

    entity_b: EntityB

    matched_properties: List[MatchedProperty]

    p_match: float

    p_match_threshold: float


if PYDANTIC_V2:
    EntityMatch.model_rebuild()
    EntityA.model_rebuild()
    EntityB.model_rebuild()
    MatchedProperty.model_rebuild()
else:
    EntityMatch.update_forward_refs()  # type: ignore
    EntityA.update_forward_refs()  # type: ignore
    EntityB.update_forward_refs()  # type: ignore
    MatchedProperty.update_forward_refs()  # type: ignore
