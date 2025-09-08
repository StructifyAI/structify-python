# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ChatUpdateSessionParams"]


class ChatUpdateSessionParams(TypedDict, total=False):
    is_favorite: Optional[bool]

    name: Optional[str]

    project_id: Optional[str]
