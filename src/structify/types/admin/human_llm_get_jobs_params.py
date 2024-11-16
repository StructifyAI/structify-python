# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["HumanLlmGetJobsParams"]


class HumanLlmGetJobsParams(TypedDict, total=False):
    status: Optional[Literal["Queued", "Running", "Completed", "Failed"]]
