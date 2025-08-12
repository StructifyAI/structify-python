# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatCopyNodeOutputByCodeHashParams"]


class ChatCopyNodeOutputByCodeHashParams(TypedDict, total=False):
    code_md5_hash: Required[str]

    new_node_id: Optional[str]
