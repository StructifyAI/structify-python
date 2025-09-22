# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PersonPeopleMatchParams"]


class PersonPeopleMatchParams(TypedDict, total=False):
    company_domain: Optional[str]
    """Company domain"""

    company_name: Optional[str]
    """Company name"""

    email: Optional[str]
    """Email address"""

    first_name: Optional[str]
    """First name"""

    last_name: Optional[str]
    """Last name"""

    linkedin_url: Optional[str]
    """LinkedIn URL"""

    location: Optional[str]
    """Location (city, state, country)"""

    name: Optional[str]
    """Full name (alternative to first/last)"""

    phone: Optional[str]
    """Phone number"""

    reveal_personal_emails: Optional[bool]
    """Whether to reveal personal email"""

    reveal_phone_number: Optional[bool]
    """Whether to reveal phone numbers"""

    reveal_professional_emails: Optional[bool]
    """Whether to reveal work email"""

    title: Optional[str]
    """Job title"""
