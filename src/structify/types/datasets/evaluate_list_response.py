# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EvaluateListResponse"]


class EvaluateListResponse(BaseModel):
    id: str

    dataset_1: str

    dataset_2: str

    iou: float

    matched: int

    started_at: datetime

    status: Literal["Running", "Completed", "Failed"]

    unmatched: int

    run_message: Optional[str] = None
