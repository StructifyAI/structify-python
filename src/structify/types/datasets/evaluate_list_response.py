# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EvaluateListResponse", "Status", "StatusFailed"]


class StatusFailed(BaseModel):
    failed: str = FieldInfo(alias="Failed")


Status: TypeAlias = Union[Literal["Running", "Completed"], StatusFailed]


class EvaluateListResponse(BaseModel):
    id: str

    dataset_1: str

    dataset_2: str

    email_1: str

    email_2: str

    iou: float

    matched: int

    started_at: datetime

    status: Status

    unmatched: int
