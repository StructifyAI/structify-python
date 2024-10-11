# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..execution_step import ExecutionStep

__all__ = ["TrainingDatumResponse"]


class TrainingDatumResponse(BaseModel):
    id: str

    labelers: List[str]

    last_updated: datetime

    status: Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped"]

    step: ExecutionStep
