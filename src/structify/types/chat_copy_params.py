# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatCopyParams"]


class ChatCopyParams(TypedDict, total=False):
    copy_name: Required[str]

    project_id: Required[str]

    source_chat_id: Required[str]
