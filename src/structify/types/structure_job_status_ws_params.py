# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["StructureJobStatusWsParams"]


class StructureJobStatusWsParams(TypedDict, total=False):
    job_ids: Required[List[str]]
    """List of job IDs to monitor"""
