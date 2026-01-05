# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ChatTemplateUpdateParams"]


class ChatTemplateUpdateParams(TypedDict, total=False):
    description: Optional[str]

    display_order: Optional[int]

    image_url: Optional[str]

    is_active: Optional[bool]

    title: Optional[str]

    updated_by: Optional[str]
