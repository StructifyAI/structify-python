# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["OrganizationDetail"]


class OrganizationDetail(BaseModel):
    id: str
    """Unique organization ID in Apollo"""

    name: str
    """Organization name"""

    annual_revenue: Optional[str] = None
    """Annual revenue"""

    blog_url: Optional[str] = None
    """Blog URL"""

    competitors: Optional[List[Dict[str, object]]] = None
    """Competitors"""

    department_headcounts: Optional[object] = None
    """Department headcounts"""

    description: Optional[str] = None
    """Description"""

    employee_growth_rate: Optional[float] = None
    """Employee growth rate"""

    facebook_url: Optional[str] = None
    """Facebook URL"""

    founded_year: Optional[int] = None
    """Founded year"""

    funding: Optional[object] = None
    """Funding information"""

    headquarters: Optional[object] = None
    """Headquarters information"""

    industry: Optional[str] = None
    """Industry"""

    keywords: Optional[List[str]] = None
    """Keywords"""

    linkedin_url: Optional[str] = None
    """LinkedIn URL"""

    logo_url: Optional[str] = None
    """Logo URL"""

    naics_codes: Optional[List[str]] = None
    """NAICS codes"""

    num_employees: Optional[int] = None
    """Employee count"""

    num_employees_range: Optional[str] = None
    """Company size"""

    phone: Optional[str] = None
    """Phone number"""

    publicly_traded_symbol: Optional[str] = None
    """Publicly traded status"""

    recent_news: Optional[List[Dict[str, object]]] = None
    """Recent news"""

    sic_codes: Optional[List[str]] = None
    """SIC codes"""

    technologies: Optional[List[Dict[str, object]]] = None
    """Technologies used"""

    twitter_url: Optional[str] = None
    """Twitter URL"""

    website_url: Optional[str] = None
    """Website domain"""
