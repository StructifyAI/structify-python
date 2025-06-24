# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["GetSessionEventsResponse", "Event"]


class Event(BaseModel):
    id: str

    body: Dict[str, object]

    job_id: str

    created_at: Optional[datetime] = None

    node_id: Optional[str] = None


class GetSessionEventsResponse(BaseModel):
    count: int

    events: List[Event]
