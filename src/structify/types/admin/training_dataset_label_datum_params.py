# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .datum_status import DatumStatus
from ..tool_call_param import ToolCallParam

__all__ = ["TrainingDatasetLabelDatumParams"]


class TrainingDatasetLabelDatumParams(TypedDict, total=False):
    id: Required[str]

    status: Required[DatumStatus]

    updated_tool_calls: Required[Iterable[ToolCallParam]]
