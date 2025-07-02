# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .dataset_descriptor import DatasetDescriptor

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]


class DatasetListResponseItem(DatasetDescriptor):
    id: str

    created_timestamp: datetime


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
