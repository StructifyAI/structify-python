# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .job_event_body import JobEventBody

__all__ = ["GetJobEventsResponse", "Event"]


class Event(BaseModel):
    body: JobEventBody
    """The body content of a job event"""

    created_at: datetime


class GetJobEventsResponse(BaseModel):
    events: List[Event]
