# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ChatCreateChatFromFilesParams"]


class ChatCreateChatFromFilesParams(TypedDict, total=False):
    files: Required[Dict[str, str]]
    """Map of relative file path to base64-encoded file bytes."""

    name: Required[str]

    project_id: Optional[str]
