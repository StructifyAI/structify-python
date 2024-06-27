# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from datetime import datetime

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["RunGetResponse"]


class RunGetResponse(BaseModel):
    date: datetime

    steps: List["ExecutionStep"]

    uuid: str
    """Used to identify this history"""


from .execution_step import ExecutionStep

if PYDANTIC_V2:
    RunGetResponse.model_rebuild()
else:
    RunGetResponse.update_forward_refs()  # type: ignore
