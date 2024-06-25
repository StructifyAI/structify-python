# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .tool_input_param import ToolInputParam

__all__ = ["SubmitCreateParams"]


class SubmitCreateParams(TypedDict, total=False):
    body: Required[Optional[Iterable[ToolInputParam]]]
