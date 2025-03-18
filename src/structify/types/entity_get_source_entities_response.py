# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EntityGetSourceEntitiesResponse", "SourceEntity"]


class SourceEntity(BaseModel):
    id: int

    created_at: datetime

    is_summary: bool

    label: str

    link: object

    llm_id: int

    location: object

    properties: object

    source_id: int

    user_specified: bool

    entity_id: Optional[int] = None

    job_id: Optional[int] = None

    step_id: Optional[int] = None


class EntityGetSourceEntitiesResponse(BaseModel):
    source_entities: List[List[SourceEntity]]
