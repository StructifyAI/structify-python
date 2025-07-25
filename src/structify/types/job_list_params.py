# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    dataset: Optional[str]
    """Dataset name to optionally filter jobs by"""

    job_type: Optional[Literal["Web", "Pdf", "Derive", "Scrape"]]
    """Type of job to optionally filter jobs by"""

    limit: int

    offset: int

    seeded_kg_search_term: Optional[str]
    """seeded kg search term"""

    since: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """List since a specific timestamp"""

    status: Optional[Literal["Queued", "Running", "Completed", "Failed"]]
    """Status to optionally filter jobs by"""
