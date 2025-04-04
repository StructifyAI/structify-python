# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .entity_match import EntityMatch

__all__ = ["EntityMergeResponse"]


class EntityMergeResponse(BaseModel):
    match_object: Optional[EntityMatch] = None

    merged_entity_id: Optional[str] = None
