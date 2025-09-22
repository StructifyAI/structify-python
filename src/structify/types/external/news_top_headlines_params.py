# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NewsTopHeadlinesParams"]


class NewsTopHeadlinesParams(TypedDict, total=False):
    category: Optional[str]
    """Category"""

    country: Optional[str]
    """Country code (ISO 3166-1)"""

    page: Optional[int]
    """Page number"""

    page_size: Optional[int]
    """Results per page (max 100)"""

    q: Optional[str]
    """Keywords"""

    sources: Optional[str]
    """Comma-separated sources"""
