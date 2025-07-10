# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    filter_test_users: Required[bool]
    """
    Filter out jobs from test users (users with functional_test feature flag or
    debug permission)
    """

    limit: Required[int]
    """Number of results to return"""

    offset: Required[int]
    """Pagination offset"""

    dataset_id: Optional[str]
    """Dataset ID to optionally filter jobs by"""

    seeded_kg_search_term: Optional[str]
    """Seeded kg search term"""

    since: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """List since a specific timestamp"""

    status: Optional[Literal["Queued", "Running", "Completed", "Failed"]]
    """Status to optionally filter jobs by"""
