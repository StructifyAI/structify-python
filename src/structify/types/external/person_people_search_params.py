# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["PersonPeopleSearchParams"]


class PersonPeopleSearchParams(TypedDict, total=False):
    contact_email_status: Optional[SequenceNotStr[str]]
    """Contact email status"""

    organization_ids: Optional[SequenceNotStr[str]]
    """Organization ids"""

    organization_locations: Optional[SequenceNotStr[str]]
    """Organization locations"""

    organization_num_employees_ranges: Optional[SequenceNotStr[str]]
    """Organization num employees ranges"""

    page: Optional[int]
    """Page number (default: 1)"""

    per_page: Optional[int]
    """Number of results per page (max 200)"""

    person_departments: Optional[SequenceNotStr[str]]
    """Person departments"""

    person_locations: Optional[SequenceNotStr[str]]
    """Person locations"""

    person_seniorities: Optional[SequenceNotStr[str]]
    """Person seniorities"""

    person_titles: Optional[SequenceNotStr[str]]
    """Person titles to include"""

    q_keywords: Optional[str]
    """Keywords"""

    q_organization_industry_tag_ids: Optional[SequenceNotStr[str]]
    """Organization industries"""

    reveal_personal_emails: Optional[bool]
    """Reveal personal emails"""

    reveal_phone_number: Optional[bool]
    """Reveal phone numbers"""

    reveal_professional_emails: Optional[bool]
    """Reveal work emails"""
