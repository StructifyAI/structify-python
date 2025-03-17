# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .execution_step import ExecutionStep

__all__ = ["JobGetStepGraphResponse", "Step", "Transition"]


class Step(BaseModel):
    id: int

    creation_time: datetime

    status: Literal["queued", "started", "executed", "skipped"]

    execution_step: Optional[ExecutionStep] = None

    queued_message: Optional[str] = None

    skipped_reason: Optional[str] = None

    state_change_message: Optional[str] = None

    step_index: Optional[int] = None


class Transition(BaseModel):
    id: object

    from_step_id: int

    to_step_id: int

    transition_time: datetime

    tool_call: Optional[object] = None


class JobGetStepGraphResponse(BaseModel):
    steps: List[Step]

    transitions: List[Transition]
