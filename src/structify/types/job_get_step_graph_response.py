# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .knowledge_graph import KnowledgeGraph

__all__ = ["JobGetStepGraphResponse", "Step", "Transition", "TransitionToolCall"]


class Step(BaseModel):
    id: str

    creation_time: datetime

    status: Literal["Queued", "Ignored", "Executed"]

    prompt: Optional[str] = None

    queued_message: Optional[str] = None

    save: Optional[KnowledgeGraph] = None
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    screenshot: Optional[object] = None

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
