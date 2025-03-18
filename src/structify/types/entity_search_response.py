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

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntitySearchResponseItemProperties]

    updated_at: datetime


EntitySearchResponse: TypeAlias = List[EntitySearchResponseItem]
