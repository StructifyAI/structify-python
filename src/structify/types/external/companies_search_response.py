# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .company_search_result import CompanySearchResult

__all__ = ["CompaniesSearchResponse"]


class CompaniesSearchResponse(BaseModel):
    organizations: List[CompanySearchResult]
    """Array of organization results"""

    pagination: object
    """Pagination information"""

    breadcrumbs: Optional[List[Dict[str, object]]] = None
    """Breadcrumbs"""

    disable_eu_prospecting: Optional[bool] = None
    """Disable eu prospecting"""

    partial_results_limit: Optional[int] = None
    """Partial results limit"""

    partial_results_only: Optional[bool] = None
    """Partial results only"""
