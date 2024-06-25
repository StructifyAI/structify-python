# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._compat import PYDANTIC_V2
from .._models import BaseModel

__all__ = ["LabelGetMessagesResponse"]


class LabelGetMessagesResponse(BaseModel):
    chat: "ChatPrompt"

    run_id: str

    uuid: str


from .chat_prompt import ChatPrompt

if PYDANTIC_V2:
    LabelGetMessagesResponse.model_rebuild()
else:
    LabelGetMessagesResponse.update_forward_refs()  # type: ignore
