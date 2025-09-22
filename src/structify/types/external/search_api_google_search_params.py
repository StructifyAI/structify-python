# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleSearchParams"]


class SearchAPIGoogleSearchParams(TypedDict, total=False):
    q: Required[str]
    """The search query"""

    gl: Optional[str]
    """Geographic location (optional, e.g. "us", "uk")"""

    hl: Optional[str]
    """Language (optional, e.g. "en", "es")"""

    num: Optional[int]
    """Number of results to return (optional, max 100)"""

    start: Optional[int]
    """Starting result index (optional)"""
