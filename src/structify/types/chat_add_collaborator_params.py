# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .chat_session_role import ChatSessionRole

__all__ = ["ChatAddCollaboratorParams"]


class ChatAddCollaboratorParams(TypedDict, total=False):
    email: Required[str]

    role: Required[ChatSessionRole]
