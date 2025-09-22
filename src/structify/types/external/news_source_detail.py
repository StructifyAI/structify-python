# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["NewsSourceDetail"]


class NewsSourceDetail(BaseModel):
    id: str
    """The identifier of the news source"""

    category: str
    """The type of news to expect from this news source"""

    country: str
    """The country this news source is based in (or primarily targets)"""

    description: str
    """A description of the news source"""

    language: str
    """The language that this news source writes in"""

    name: str
    """A display-suitable name for the news source"""

    url: str
    """The URL of the homepage"""
