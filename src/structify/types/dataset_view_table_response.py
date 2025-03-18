# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["DatasetViewTableResponse"]


class DatasetViewTableResponse(BaseModel):
    id: int

    creation_time: datetime

    dataset_id: object

    label: str

    properties: object
