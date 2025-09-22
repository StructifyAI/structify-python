# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from .google_search_result import GoogleSearchResult

__all__ = ["GoogleSearchResponse"]


class GoogleSearchResponse(BaseModel):
    organic_results: List[GoogleSearchResult]
    """Array of search results"""

    related_searches: Optional[List[Dict[str, object]]] = None
    """Related searches"""

    search_information: Optional[object] = None
    """Total number of results found"""
