# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ExternalSearchResponse", "ExternalSearchResponseItem"]


class ExternalSearchResponseItem(BaseModel):
    description: str
    """Description/snippet of the search result"""

    query: str
    """The search query that produced this result"""

    title: str
    """Title of the search result"""

    url: str
    """URL of the search result"""


ExternalSearchResponse: TypeAlias = List[ExternalSearchResponseItem]
