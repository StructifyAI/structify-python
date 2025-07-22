# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SessionMarkErroredParams"]


class SessionMarkErroredParams(TypedDict, total=False):
    error_message: Required[str]

    error_traceback: Optional[str]
