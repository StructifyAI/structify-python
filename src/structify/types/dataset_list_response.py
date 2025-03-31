# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]


class DatasetListResponseItem(BaseModel):
    id: str

    description: str

    name: str


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
