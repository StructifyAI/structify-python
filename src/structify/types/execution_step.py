# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .tool_call import ToolCall
from .chat_prompt import ChatPrompt

__all__ = ["ExecutionStep", "Response"]


class Response(BaseModel):
    completion_tokens: int

    cost: float
    """Cost in dollars"""

    llm: str

    prompt_tokens: int
    """New tokens"""

    text: str

    tool_calls: List[ToolCall]


class ExecutionStep(BaseModel):
    id: str

    prompt: ChatPrompt

    response: Response
