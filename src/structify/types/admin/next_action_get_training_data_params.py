# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["NextActionGetTrainingDataParams"]


class NextActionGetTrainingDataParams(TypedDict, total=False):
    job_id: Optional[str]
    """Optional job ID to filter training data"""

    limit: Optional[int]
    """Optional limit to filter training data"""

    offset: Optional[int]
    """Optional offset to filter training data"""

    status: Optional[str]
    """Optional status to filter training data"""
