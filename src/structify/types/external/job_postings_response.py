# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .job_posting import JobPosting

__all__ = ["JobPostingsResponse"]


class JobPostingsResponse(BaseModel):
    job_postings: List[JobPosting]
    """Array of job postings"""

    pagination: object
    """Pagination information"""

    organization: Optional[object] = None
    """Organization information"""
