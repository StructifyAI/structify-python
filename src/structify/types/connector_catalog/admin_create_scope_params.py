# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AdminCreateScopeParams"]


class AdminCreateScopeParams(TypedDict, total=False):
    connector_auth_method_id: Required[str]

    scope_value: Required[str]

    is_recommended: bool

    is_required: bool

    query_parameter: str
