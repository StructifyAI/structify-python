# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleScholarSearchParams"]


class SearchAPIGoogleScholarSearchParams(TypedDict, total=False):
    q: Required[str]
    """The search query"""

    as_yhi: Optional[int]
    """Year range end (optional, e.g. 2023)"""

    as_ylo: Optional[int]
    """Year range start (optional, e.g. 2020)"""

    hl: Optional[str]
    """Language (optional, e.g. "en")"""

    num: Optional[int]
    """Number of results to return (optional)"""

    start: Optional[int]
    """Starting result index (optional)"""
