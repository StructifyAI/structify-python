# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["EntitySummarizeResponse", "EntitySummarizeResponseItem"]


class EntitySummarizeResponseItem(BaseModel):
    id: str

    created_at: datetime

    dataset_id: object

    label: str

    properties: object

    updated_at: datetime


EntitySummarizeResponse: TypeAlias = List[EntitySummarizeResponseItem]
