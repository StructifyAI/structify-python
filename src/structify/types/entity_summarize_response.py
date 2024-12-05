# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "EntitySummarizeResponse",
    "EntitySummarizeResponseItem",
    "EntitySummarizeResponseItemProperties",
    "EntitySummarizeResponseItemPropertiesImage",
]


class EntitySummarizeResponseItemPropertiesImage(BaseModel):
    number: int

    hash: Optional[str] = None


EntitySummarizeResponseItemProperties: TypeAlias = Union[str, bool, float, EntitySummarizeResponseItemPropertiesImage]


class EntitySummarizeResponseItem(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, EntitySummarizeResponseItemProperties]


EntitySummarizeResponse: TypeAlias = List[EntitySummarizeResponseItem]
