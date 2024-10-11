# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TrainingDatasetGetStepByIDParams"]


class TrainingDatasetGetStepByIDParams(TypedDict, total=False):
    step_id: Required[str]
