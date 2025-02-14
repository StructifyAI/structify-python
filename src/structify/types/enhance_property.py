# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["EnhanceProperty"]


class EnhanceProperty(BaseModel):
    entity_id: str

    property_name: str

    allow_extra_entities: Optional[bool] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None
