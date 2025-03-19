# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel
from .datum_status import DatumStatus

__all__ = ["LabelingStats"]


class LabelingStats(BaseModel):
    author: str

    capped_prop_count: int

    count: int

    dataset: str

    prop_count: int

    status: DatumStatus

    window_start: datetime
