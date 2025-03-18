# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EntityMergeResponse", "MatchObject"]


class MatchObject(BaseModel):
    a_id: int

    b_id: int

    info: str

    p_match: float

    p_match_threshold: float


class EntityMergeResponse(BaseModel):
    match_object: Optional[MatchObject] = None

    merged_entity_id: Optional[int] = None
