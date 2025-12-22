# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AdminUpdateCredentialFieldParams"]


class AdminUpdateCredentialFieldParams(TypedDict, total=False):
    default_value: Optional[str]

    description: Optional[str]

    display_order: Optional[int]

    field_type: Optional[str]

    is_optional: Optional[bool]

    label: Optional[str]

    name: Optional[str]

    options: object
