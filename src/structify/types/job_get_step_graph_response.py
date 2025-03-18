# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .execution_step import ExecutionStep

__all__ = ["JobGetStepGraphResponse", "JobGetStepGraphResponseItem", "JobGetStepGraphResponseItemParentTransition"]


class JobGetStepGraphResponseItemParentTransition(BaseModel):
    parent_id: str

    tool_input: str

    tool_name: str


class JobGetStepGraphResponseItem(BaseModel):
    id: str

    creation_time: datetime

    status: Literal["queued", "started", "executed", "skipped"]

    execution_step: Optional[ExecutionStep] = None

    parent_transition: Optional[JobGetStepGraphResponseItemParentTransition] = None

    queued_message: Optional[str] = None

    skipped_reason: Optional[str] = None

    state_change_message: Optional[str] = None

    step_index: Optional[int] = None


JobGetStepGraphResponse: TypeAlias = List[JobGetStepGraphResponseItem]
