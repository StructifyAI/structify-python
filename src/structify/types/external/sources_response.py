# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .news_source_detail import NewsSourceDetail

__all__ = ["SourcesResponse"]


class SourcesResponse(BaseModel):
    sources: List[NewsSourceDetail]
    """The array of news sources"""

    status: str
    """The status of the request"""
