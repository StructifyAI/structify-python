# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["EntityMergeResponse"]


class EntityMergeResponse(BaseModel):
    match_object: Optional["MatchedEntity"] = None

    merged_entity_id: Optional[str] = None


from .matched_entity import MatchedEntity

if PYDANTIC_V2:
    EntityMergeResponse.model_rebuild()
else:
    EntityMergeResponse.update_forward_refs()  # type: ignore
