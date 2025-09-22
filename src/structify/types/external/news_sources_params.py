# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NewsSourcesParams"]


class NewsSourcesParams(TypedDict, total=False):
    category: Optional[str]
    """News category"""

    country: Optional[str]
    """Country code"""

    language: Optional[str]
    """Language code"""
