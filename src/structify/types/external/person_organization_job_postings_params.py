# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PersonOrganizationJobPostingsParams"]


class PersonOrganizationJobPostingsParams(TypedDict, total=False):
    page: Optional[int]
    """Page number"""

    per_page: Optional[int]
    """Results per page"""
