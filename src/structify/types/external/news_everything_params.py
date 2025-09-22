# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NewsEverythingParams"]


class NewsEverythingParams(TypedDict, total=False):
    domains: Optional[str]
    """Comma-separated domains"""

    exclude_domains: Optional[str]
    """Domains to exclude"""

    from_: Annotated[Optional[str], PropertyInfo(alias="from")]
    """Oldest article date (ISO 8601)"""

    language: Optional[str]
    """Language code (ISO 639-1)"""

    page: Optional[int]
    """Page number"""

    page_size: Optional[int]
    """Results per page (max 100)"""

    q: Optional[str]
    """Keywords"""

    q_in_title: Optional[str]
    """Keywords in title only"""

    sort_by: Optional[str]
    """Sort order"""

    sources: Optional[str]
    """Comma-separated sources"""

    to: Optional[str]
    """Newest article date (ISO 8601)"""
