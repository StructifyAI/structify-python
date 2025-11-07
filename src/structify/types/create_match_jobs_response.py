# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CreateMatchJobsResponse"]


class CreateMatchJobsResponse(BaseModel):
    count: int
    """Number of jobs created"""

    job_ids: List[str]
    """IDs of the created match jobs"""
