# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .create_scope_request_param import CreateScopeRequestParam

__all__ = ["AdminBatchCreateScopesParams"]


class AdminBatchCreateScopesParams(TypedDict, total=False):
    scopes: Required[Iterable[CreateScopeRequestParam]]
