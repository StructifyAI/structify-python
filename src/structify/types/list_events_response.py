# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .event import Event
from .._models import BaseModel

__all__ = ["ListEventsResponse"]


class ListEventsResponse(BaseModel):
    data: List[Event]

    next_cursor: Optional[str] = None
    """Cursor to fetch the next page; `None` when the current page is the last one."""
