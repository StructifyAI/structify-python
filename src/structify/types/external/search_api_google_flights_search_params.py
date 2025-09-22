# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleFlightsSearchParams"]


class SearchAPIGoogleFlightsSearchParams(TypedDict, total=False):
    arrival_id: Required[str]
    """Arrival airport code (e.g., "JFK", "LAX")"""

    departure_id: Required[str]
    """Departure airport code (e.g., "JFK", "LAX")"""

    outbound_date: Required[str]
    """Outbound date (YYYY-MM-DD format)"""

    adults: Optional[int]
    """Number of adults (optional, default 1)"""

    children: Optional[int]
    """Number of children (optional, default 0)"""

    currency: Optional[str]
    """Currency (optional, e.g. "USD")"""

    hl: Optional[str]
    """Language (optional, e.g. "en")"""

    infants_in_seat: Optional[int]
    """Number of infants on lap (optional, default 0)"""

    infants_on_lap: Optional[int]
    """Number of infants in seat (optional, default 0)"""

    return_date: Optional[str]
    """Return date (YYYY-MM-DD format, optional for one-way)"""

    travel_class: Optional[str]
    """Travel class (optional: "economy", "premium_economy", "business", "first")"""
