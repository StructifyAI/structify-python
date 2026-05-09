# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .chat_prompt_param import ChatPromptParam

__all__ = ["ChatSimulatePromptParams"]


class ChatSimulatePromptParams(TypedDict, total=False):
    chat_prompt: Required[ChatPromptParam]
