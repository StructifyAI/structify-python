# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .person_search_result import PersonSearchResult

__all__ = ["PeopleSearchResponse"]


class PeopleSearchResponse(BaseModel):
    pagination: object
    """Pagination information"""

    people: List[PersonSearchResult]
    """Array of people results"""

    breadcrumbs: Optional[List[Dict[str, object]]] = None
    """Breadcrumbs"""

    disable_eu_prospecting: Optional[bool] = None
    """Disable eu prospecting"""

    partial_results_limit: Optional[int] = None
    """Partial results limit"""

    partial_results_only: Optional[bool] = None
    """Partial results only"""
