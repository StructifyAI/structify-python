# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EntitySummarizeResponse", "EntitySummarizeResponseItem"]


class EntitySummarizeResponseItem(BaseModel):
    id: int

    creation_time: datetime

    dataset_id: object

    label: str

    properties: object


EntitySummarizeResponse: TypeAlias = List[EntitySummarizeResponseItem]
