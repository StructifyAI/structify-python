# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..tool_call import ToolCall
from .datum_status import DatumStatus
from ..execution_step import ExecutionStep

__all__ = ["TrainingDatumResponse", "Update", "UpdateResponse"]


class UpdateResponse(BaseModel):
    llm: str

    text: str

    tool_calls: List[ToolCall]


class Update(BaseModel):
    id: str

    author: str

    status: DatumStatus

    timestamp: datetime

    response: Optional[UpdateResponse] = None

    review_message: Optional[str] = None

    target_id: Optional[str] = None


class TrainingDatumResponse(BaseModel):
    id: str

    last_updated: datetime

    status: DatumStatus

    step: ExecutionStep

    updates: List[Update]
    """All updates for the datum, sorted by ascending timestamp."""
