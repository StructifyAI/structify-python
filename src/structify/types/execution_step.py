# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .chat_prompt import ChatPrompt

__all__ = ["ExecutionStep", "Response", "ResponseToolCall"]


class ResponseToolCall(BaseModel):
    formatted_input: str

    name: str


class Response(BaseModel):
    completion_tokens: int

    cost: float
    """Cost in dollars"""

    llm: str

    prompt_tokens: int
    """New tokens"""

    text: str

    tool_calls: List[ResponseToolCall]


class ExecutionStep(BaseModel):
    id: str

    prompt: ChatPrompt

    response: Response
