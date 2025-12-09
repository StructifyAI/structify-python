# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..dataset_descriptor import DatasetDescriptor

__all__ = ["AdminDatasetReturn"]


class AdminDatasetReturn(DatasetDescriptor):
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas
    are held within the dataset.
    """

    id: str

    created_timestamp: datetime

    user_id: str
