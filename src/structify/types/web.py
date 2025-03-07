# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Web"]


class Web(BaseModel):
    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None
