# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SessionGetEventsParams"]


class SessionGetEventsParams(TypedDict, total=False):
    limit: int

    offset: int

    search_term: Optional[str]

    status: Optional[Literal["Queued", "Running", "Completed", "Failed"]]
