# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GoogleSearchResult"]


class GoogleSearchResult(BaseModel):
    link: str
    """Search result URL"""

    snippet: str
    """Search result snippet/description"""

    title: str
    """Search result title"""

    display_link: Optional[str] = None
    """Display URL"""
