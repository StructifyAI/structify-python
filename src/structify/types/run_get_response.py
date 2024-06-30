# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .execution_step import ExecutionStep

__all__ = ["RunGetResponse"]


class RunGetResponse(BaseModel):
    date: datetime

    steps: List[ExecutionStep]

    uuid: str
    """Used to identify this history"""
