# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["PersonMatch"]


class PersonMatch(BaseModel):
    id: str
    """Unique person ID in Apollo"""

    city: Optional[str] = None
    """Location"""

    country: Optional[str] = None
    """Country"""

    email: Optional[str] = None
    """Email addresses"""

    employment_history: Optional[List[Dict[str, object]]] = None
    """Employment history"""

    first_name: Optional[str] = None
    """First name"""

    headline: Optional[str] = None
    """Confidence score"""

    last_name: Optional[str] = None
    """Last name"""

    linkedin_url: Optional[str] = None
    """LinkedIn URL"""

    match_score: Optional[float] = None
    """Apollo match confidence"""

    name: Optional[str] = None
    """Full name"""

    organization: Optional[object] = None
    """Company information"""

    personal_emails: Optional[List[str]] = None
    """Personal emails"""

    phone_numbers: Optional[List[Dict[str, object]]] = None
    """Phone numbers"""

    state: Optional[str] = None
    """State"""

    title: Optional[str] = None
    """Job title"""

    work_email: Optional[str] = None
    """Work email"""
