# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = ["EntitySearchResponse", "EntitySearchResponseItem", "EntitySearchResponseItemProperties"]

EntitySearchResponseItemProperties: TypeAlias = Union[str, bool, float, Image]


class EntitySearchResponseItem(BaseModel):
    id: str

    creation_time: datetime

    label: str

    properties: Dict[str, EntitySearchResponseItemProperties]


EntitySearchResponse: TypeAlias = List[EntitySearchResponseItem]
