# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPILocationSearchParams"]


class SearchAPILocationSearchParams(TypedDict, total=False):
    q: Required[str]
    """The location query to search for"""

    gl: Optional[str]
    """Geographic location bias (optional, e.g. "us", "uk")"""

    hl: Optional[str]
    """Language (optional, e.g. "en")"""

    num: Optional[int]
    """Number of results to return (optional)"""
