# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from .image import Image
from .._models import BaseModel

__all__ = ["EntitySummarizeResponse", "EntitySummarizeResponseItem", "EntitySummarizeResponseItemProperties"]

EntitySummarizeResponseItemProperties: TypeAlias = Union[str, bool, float, Image]


class EntitySummarizeResponseItem(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: Dict[str, EntitySummarizeResponseItemProperties]

    updated_at: datetime


EntitySummarizeResponse: TypeAlias = List[EntitySummarizeResponseItem]
