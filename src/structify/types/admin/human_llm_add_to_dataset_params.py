# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..tool_call_param import ToolCallParam

__all__ = ["HumanLlmAddToDatasetParams"]


class HumanLlmAddToDatasetParams(TypedDict, total=False):
    extraction_criteria_met: Required[bool]

    job_id: Required[str]

    step_id: Required[str]

    tool_calls: Required[Iterable[ToolCallParam]]
