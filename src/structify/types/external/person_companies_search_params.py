# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["PersonCompaniesSearchParams"]


class PersonCompaniesSearchParams(TypedDict, total=False):
    organization_department_headcount_ranges: Optional[SequenceNotStr[str]]
    """Organization department headcount ranges"""

    organization_founded_year_max: Optional[int]
    """Organization founded year maximum"""

    organization_founded_year_min: Optional[int]
    """Organization founded year minimum"""

    organization_locations: Optional[SequenceNotStr[str]]
    """Organization locations"""

    organization_naics_codes: Optional[SequenceNotStr[str]]
    """Organization NAICS codes"""

    organization_not_ids: Optional[SequenceNotStr[str]]
    """Organization ids to exclude"""

    organization_num_employees_ranges: Optional[SequenceNotStr[str]]
    """Organization num employees ranges"""

    organization_revenue_ranges: Optional[SequenceNotStr[str]]
    """Organization revenue ranges"""

    organization_sic_codes: Optional[SequenceNotStr[str]]
    """Organization SIC codes"""

    organization_technologies: Optional[SequenceNotStr[str]]
    """Organization technologies"""

    page: Optional[int]
    """Page number (default: 1)"""

    per_page: Optional[int]
    """Number of results per page (max 200)"""

    q_keywords: Optional[str]
    """Keywords to search for"""

    q_organization_industry_tag_ids: Optional[SequenceNotStr[str]]
    """Organization industries"""

    q_organization_keyword_tags: Optional[SequenceNotStr[str]]
    """Organization keyword tags"""

    sort_ascending: Optional[bool]
    """Sort ascending"""

    sort_by_field: Optional[str]
    """Sort by field"""
