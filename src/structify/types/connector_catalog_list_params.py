# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ConnectorCatalogListParams"]


class ConnectorCatalogListParams(TypedDict, total=False):
    include_inactive: bool
    """Include inactive auth methods (admin only)"""

    limit: int

    offset: int

    search: Optional[str]
    """
    Optional search query to filter by name, slug, or category (case-insensitive
    substring match)
    """
