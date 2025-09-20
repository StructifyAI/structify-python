# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["JobPosting"]


class JobPosting(BaseModel):
    id: str
    """Job posting ID"""

    title: str
    """Job title"""

    application_url: Optional[str] = None
    """Application URL"""

    department: Optional[str] = None
    """Department"""

    description: Optional[str] = None
    """Job description"""

    education_required: Optional[str] = None
    """Education required"""

    employment_type: Optional[str] = None
    """Employment type (full-time, part-time, contract, etc.)"""

    experience_required: Optional[str] = None
    """Experience required"""

    job_function: Optional[str] = None
    """Job function"""

    location: Optional[str] = None
    """Location"""

    posted_date: Optional[str] = None
    """Posted date"""

    remote_allowed: Optional[bool] = None
    """Remote work allowed"""

    salary_range: Optional[str] = None
    """Salary range"""

    seniority_level: Optional[str] = None
    """Seniority level"""

    url: Optional[str] = None
    """Job posting URL"""
