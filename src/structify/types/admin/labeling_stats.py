# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .datum_status import DatumStatus

__all__ = ["LabelingStats"]


class LabelingStats(BaseModel):
    author: str

    count: int

    dataset: str

    period: datetime

    status: DatumStatus

    capped_count: Optional[int] = None
