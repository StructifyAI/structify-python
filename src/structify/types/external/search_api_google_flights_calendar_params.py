# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleFlightsCalendarParams"]


class SearchAPIGoogleFlightsCalendarParams(TypedDict, total=False):
    arrival_id: Required[str]
    """Arrival airport code"""

    departure_id: Required[str]
    """Departure airport code"""

    outbound_date: Required[str]
    """Outbound date (YYYY-MM-DD format)"""

    currency: Optional[str]
    """Currency (optional, e.g. "USD")"""

    hl: Optional[str]
    """Language (optional, e.g. "en")"""

    return_date: Optional[str]
    """Return date (YYYY-MM-DD format, optional)"""
