# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EntityGetSourceEntitiesResponse", "SourceEntity"]


class SourceEntity(BaseModel):
    id: str

    created_at: datetime

    is_summary: bool

    label: str

    llm_id: int

    properties: object

    source_id: str

    user_specified: bool

    job_id: Optional[str] = None

    kg_entity_id: Optional[str] = None

    link: Optional[object] = None

    location: Optional[object] = None

    step_id: Optional[str] = None


class EntityGetSourceEntitiesResponse(BaseModel):
    source_entities: List[List[SourceEntity]]
