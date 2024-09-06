# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    dataset_name: Optional[str]
    """Dataset name to optionally filter jobs by"""

    limit: int

    offset: int

    status: Optional[Literal["Queued", "Running", "Completed", "Failed"]]
    """Status to optionally filter jobs by"""
