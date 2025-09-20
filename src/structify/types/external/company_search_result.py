# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["CompanySearchResult"]


class CompanySearchResult(BaseModel):
    id: str
    """Organization ID"""

    name: str
    """Organization name"""

    annual_revenue: Optional[str] = None
    """Annual revenue"""

    blog_url: Optional[str] = None
    """Blog URL"""

    description: Optional[str] = None
    """Description"""

    facebook_url: Optional[str] = None
    """Facebook URL"""

    founded_year: Optional[int] = None
    """Founded year"""

    headquarters: Optional[object] = None
    """Headquarters location"""

    industry: Optional[str] = None
    """Industry"""

    linkedin_url: Optional[str] = None
    """LinkedIn URL"""

    logo_url: Optional[str] = None
    """Logo URL"""

    naics_codes: Optional[List[str]] = None
    """NAICS codes"""

    num_employees: Optional[int] = None
    """Number of employees"""

    num_employees_range: Optional[str] = None
    """Number of employees range"""

    phone: Optional[str] = None
    """Phone number"""

    publicly_traded_symbol: Optional[str] = None
    """Publicly traded symbol"""

    sic_codes: Optional[List[str]] = None
    """SIC codes"""

    technologies: Optional[List[Dict[str, object]]] = None
    """Technologies used"""

    twitter_url: Optional[str] = None
    """Twitter URL"""

    website_url: Optional[str] = None
    """Website URL"""
