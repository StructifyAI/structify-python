# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from ..execution_step import ExecutionStep

__all__ = ["TrainingDatumResponse"]


class TrainingDatumResponse(BaseModel):
    id: str

    status: Literal["Unverified", "Verified", "Pending", "Skipped"]

    step: ExecutionStep
