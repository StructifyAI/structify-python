# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .autofix_context import AutofixContext

__all__ = ["SessionMarkErroredParams"]


class SessionMarkErroredParams(TypedDict, total=False):
    error_message: Required[str]

    autofix: bool

    autofix_context: Optional[AutofixContext]

    error_traceback: Optional[str]
