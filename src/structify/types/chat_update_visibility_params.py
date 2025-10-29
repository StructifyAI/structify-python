# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .chat_visibility import ChatVisibility

__all__ = ["ChatUpdateVisibilityParams"]


class ChatUpdateVisibilityParams(TypedDict, total=False):
    visibility: Required[ChatVisibility]
