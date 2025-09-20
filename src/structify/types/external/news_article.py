# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .news_source import NewsSource

__all__ = ["NewsArticle"]


class NewsArticle(BaseModel):
    published_at: str
    """The date and time that the article was published"""

    source: NewsSource

    title: str
    """The headline or title of the article"""

    url: str
    """The direct URL to the article"""

    author: Optional[str] = None
    """The author of the article"""

    content: Optional[str] = None
    """The unformatted content of the article"""

    description: Optional[str] = None
    """A description or snippet from the article"""

    url_to_image: Optional[str] = None
    """The URL to a relevant image for the article"""
