# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..tool_call import ToolCall

__all__ = ["HumanLlmPrelabelStepResponse"]


class HumanLlmPrelabelStepResponse(BaseModel):
    llm: str

    text: str

    tool_calls: List[ToolCall]
