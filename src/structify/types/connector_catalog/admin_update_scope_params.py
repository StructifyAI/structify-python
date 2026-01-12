# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["AdminUpdateScopeParams"]


class AdminUpdateScopeParams(TypedDict, total=False):
    is_recommended: Optional[bool]

    is_required: Optional[bool]

    query_parameter: Optional[str]

    scope_value: Optional[str]
