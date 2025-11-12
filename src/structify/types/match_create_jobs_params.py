# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["MatchCreateJobsParams"]


class MatchCreateJobsParams(TypedDict, total=False):
    conditioning: Required[str]
    """Optional conditioning prompt for the LLM matcher"""

    dataset: Required[str]
    """Dataset name"""

    source_table: Required[str]
    """Source table name (entities to match from)"""

    target_table: Required[str]
    """Target table name (entities to match to)"""

    node_id: Optional[str]
