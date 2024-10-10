# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..execution_step_param import ExecutionStepParam

__all__ = ["TrainingDatasetUpdateDatumParams"]


class TrainingDatasetUpdateDatumParams(TypedDict, total=False):
    id: Required[str]

    status: Required[Literal["Unverified", "Verified", "Pending", "Skipped"]]

    step: Required[ExecutionStepParam]
