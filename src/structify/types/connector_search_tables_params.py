# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ConnectorSearchTablesParams"]


class ConnectorSearchTablesParams(TypedDict, total=False):
    query: Required[str]
    """Search query string"""

    team_id: Required[str]
    """Team ID to search tables for"""
