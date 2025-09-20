# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatLoadFilesParams"]


class ChatLoadFilesParams(TypedDict, total=False):
    chat_id: Required[str]

    commit_hash: Optional[str]
