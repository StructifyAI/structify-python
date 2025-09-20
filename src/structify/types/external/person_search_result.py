# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["PersonSearchResult"]


class PersonSearchResult(BaseModel):
    id: str
    """Person ID"""

    city: Optional[str] = None
    """City"""

    country: Optional[str] = None
    """Country"""

    email: Optional[str] = None
    """Email address"""

    employment_history: Optional[List[Dict[str, object]]] = None
    """Employment history"""

    first_name: Optional[str] = None
    """First name"""

    last_name: Optional[str] = None
    """Last name"""

    linkedin_url: Optional[str] = None
    """LinkedIn URL"""

    name: Optional[str] = None
    """Full name"""

    organization: Optional[object] = None
    """Organization"""

    phone_numbers: Optional[List[Dict[str, object]]] = None
    """Phone numbers"""

    state: Optional[str] = None
    """State"""

    title: Optional[str] = None
    """Job title"""
