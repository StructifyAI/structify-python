# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "EntitySearchResponse",
    "EntitySearchResponseItem",
    "EntitySearchResponseItemProperties",
    "EntitySearchResponseItemPropertiesImage",
]


class EntitySearchResponseItemPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


EntitySearchResponseItemProperties: TypeAlias = Union[str, bool, float, EntitySearchResponseItemPropertiesImage]


class EntitySearchResponseItem(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, EntitySearchResponseItemProperties]


EntitySearchResponse: TypeAlias = List[EntitySearchResponseItem]
