# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleMapsPlaceReviewsParams"]


class SearchAPIGoogleMapsPlaceReviewsParams(TypedDict, total=False):
    place_id: Required[str]
    """Place ID from Google Maps"""

    hl: Optional[str]
    """Language (optional, e.g. "en", "es")"""

    num: Optional[int]
    """Number of reviews to return (optional)"""
