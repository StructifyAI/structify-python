# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleMapsPlacePhotosParams"]


class SearchAPIGoogleMapsPlacePhotosParams(TypedDict, total=False):
    place_id: Required[str]
    """Place ID from Google Maps"""

    num: Optional[int]
    """Number of photos to return (optional)"""
