# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .job_event_body import JobEventBody
from .knowledge_graph import KnowledgeGraph

__all__ = ["SessionGetEventsResponse", "Event", "EventEvent"]


class EventEvent(BaseModel):
    body: JobEventBody
    """The body content of a job event"""

    created_at: datetime


class Event(BaseModel):
    id: str

    events: List[EventEvent]

    run_started_time: datetime

    status: Literal["Queued", "Running", "Completed", "Failed"]

    seeded_kg: Optional[KnowledgeGraph] = None
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class SessionGetEventsResponse(BaseModel):
    count: int

    events: List[Event]
