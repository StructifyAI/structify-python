# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MatchListResultsParams"]


class MatchListResultsParams(TypedDict, total=False):
    dataset: Required[str]
    """Dataset name"""

    source_table: Required[str]
    """Source table name to get matches for"""

    limit: int
    """Number of results to return (default: 1000, max: 1000)"""

    offset: int
    """Offset for pagination (default: 0)"""
