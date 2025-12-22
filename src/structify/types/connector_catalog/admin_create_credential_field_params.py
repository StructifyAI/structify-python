# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AdminCreateCredentialFieldParams"]


class AdminCreateCredentialFieldParams(TypedDict, total=False):
    auth_method_id: Required[str]

    display_order: Required[int]

    field_type: Required[str]

    is_optional: Required[bool]

    name: Required[str]

    default_value: Optional[str]

    description: Optional[str]

    label: Optional[str]

    options: object
