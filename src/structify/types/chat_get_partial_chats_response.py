# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .chat_prompt import ChatPrompt

__all__ = ["ChatGetPartialChatsResponse"]

ChatGetPartialChatsResponse: TypeAlias = List[ChatPrompt]
