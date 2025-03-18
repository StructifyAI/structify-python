# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["DatasetViewTableResponse"]


class DatasetViewTableResponse(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    label: str

    properties: object

    updated_at: datetime
