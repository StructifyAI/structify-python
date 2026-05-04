# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AnalyticsListEventsParams"]


class AnalyticsListEventsParams(TypedDict, total=False):
    cursor: Optional[str]
    """
    Opaque cursor returned as `next_cursor` on the previous page. Omit on the first
    request.
    """

    limit: Optional[int]
    """Maximum number of events to return. Defaults to 100, capped at 1000."""
