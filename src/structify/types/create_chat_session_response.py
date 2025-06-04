# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .chat_session_with_messages import ChatSessionWithMessages

__all__ = ["CreateChatSessionResponse"]


class CreateChatSessionResponse(BaseModel):
    session: ChatSessionWithMessages
