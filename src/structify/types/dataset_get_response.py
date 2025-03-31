# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .dataset_descriptor import DatasetDescriptor

__all__ = ["DatasetGetResponse"]


class DatasetGetResponse(DatasetDescriptor):
    id: str

    created_timestamp: datetime
