# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ActionTrainingDatumMetadata"]


class ActionTrainingDatumMetadata(BaseModel):
    id: str

    author: str

    created_at: datetime

    label_count: int

    latest_label: Optional[str] = None

    latest_label_at: Optional[datetime] = None
