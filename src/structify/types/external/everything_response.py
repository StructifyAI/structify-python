# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .news_article import NewsArticle

__all__ = ["EverythingResponse"]


class EverythingResponse(BaseModel):
    articles: List[NewsArticle]
    """The results of the request"""

    status: str
    """The status of the request"""

    total_results: int
    """The total number of results available for your request"""
