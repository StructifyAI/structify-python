# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import TypeAlias

from .dataset_descriptor import DatasetDescriptor

__all__ = ["DatasetListResponse", "DatasetListResponseItem"]


class DatasetListResponseItem(DatasetDescriptor):
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas
    are held within the dataset.
    """

    id: str

    created_timestamp: datetime


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]
