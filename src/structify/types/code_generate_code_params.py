# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CodeGenerateCodeParams"]


class CodeGenerateCodeParams(TypedDict, total=False):
    chat_session_id: Required[Annotated[str, PropertyInfo(alias="chatSessionId")]]

    prompt: Required[str]

    message_id: Annotated[Optional[str], PropertyInfo(alias="messageId")]
