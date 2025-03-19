# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["FindRelationship"]


class FindRelationship(BaseModel):
    from_id: str

    relationship_name: str

    to_id: str

    allow_extra_entities: Optional[bool] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None
