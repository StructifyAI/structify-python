# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["EntityTriggerMergeResponse"]


class EntityTriggerMergeResponse(BaseModel):
    id: str

    created_at: datetime

    dataset_id: object

    label: str

    properties: object

    updated_at: datetime
