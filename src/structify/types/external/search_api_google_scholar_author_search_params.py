# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SearchAPIGoogleScholarAuthorSearchParams"]


class SearchAPIGoogleScholarAuthorSearchParams(TypedDict, total=False):
    author: Required[str]
    """Author name to search for"""

    hl: Optional[str]
    """Language (optional, e.g. "en")"""

    num: Optional[int]
    """Number of results to return (optional)"""

    start: Optional[int]
    """Starting result index (optional)"""
