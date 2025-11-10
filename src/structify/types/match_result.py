# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["MatchResult"]


class MatchResult(BaseModel):
    id: str

    created_at: datetime

    job_id: str

    match_reason: str

    source_entity_id: str

    target_entity_id: str

    confidence_score: Optional[float] = None

    source_entity_index: Optional[int] = None

    target_entity_index: Optional[int] = None
