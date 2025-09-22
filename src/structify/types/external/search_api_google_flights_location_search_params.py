# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleFlightsLocationSearchParams"]


class SearchAPIGoogleFlightsLocationSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query for airport/location"""

    hl: Optional[str]
    """Language (optional, e.g. "en")"""
