# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..dataset_descriptor import DatasetDescriptor

__all__ = ["AdminDatasetReturn"]


class AdminDatasetReturn(DatasetDescriptor):
    id: str

    created_timestamp: datetime

    user_id: str
