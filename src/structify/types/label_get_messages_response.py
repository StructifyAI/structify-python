# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel
from .chat_prompt import ChatPrompt

__all__ = ["LabelGetMessagesResponse"]


class LabelGetMessagesResponse(BaseModel):
    chat: ChatPrompt

    run_id: str

    uuid: str
