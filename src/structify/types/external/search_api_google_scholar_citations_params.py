# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleScholarCitationsParams"]


class SearchAPIGoogleScholarCitationsParams(TypedDict, total=False):
    q: Required[str]
    """The publication ID to get citations for"""

    hl: Optional[str]
    """Language (optional, e.g. "en")"""

    num: Optional[int]
    """Number of citations to return (optional)"""

    start: Optional[int]
    """Starting result index (optional)"""
