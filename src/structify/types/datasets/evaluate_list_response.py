# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["EvaluateListResponse"]


class EvaluateListResponse(BaseModel):
    id: str

    dataset_1: str

    dataset_2: str

    email_1: str

    email_2: str

    started_at: datetime
