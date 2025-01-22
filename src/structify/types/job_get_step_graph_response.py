# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .execution_step import ExecutionStep

__all__ = ["JobGetStepGraphResponse", "Step", "Transition", "TransitionToolCall"]


class Step(BaseModel):
    id: str

    creation_time: datetime

    status: Literal["Queued", "Ignored", "Started", "Executed"]

    execution_step: Optional[ExecutionStep] = None

    queued_message: Optional[str] = None

    skipped_reason: Optional[str] = None

    state_change_message: Optional[str] = None

    step_index: Optional[int] = None


class TransitionToolCall(BaseModel):
    action: str

    formatted_input: str

    name: str


class Transition(BaseModel):
    from_: str = FieldInfo(alias="from")

    to: str

    tool_call: TransitionToolCall


class JobGetStepGraphResponse(BaseModel):
    steps: List[Step]

    transitions: List[Transition]
