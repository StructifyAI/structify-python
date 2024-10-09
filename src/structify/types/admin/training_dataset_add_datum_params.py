# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..execution_step_param import ExecutionStepParam

__all__ = ["TrainingDatasetAddDatumParams"]


class TrainingDatasetAddDatumParams(TypedDict, total=False):
    step: Required[ExecutionStepParam]
