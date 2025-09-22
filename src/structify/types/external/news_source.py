# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["NewsSource"]


class NewsSource(BaseModel):
    name: str
    """The name of the news source"""

    id: Optional[str] = None
    """The identifier id of the news source"""
