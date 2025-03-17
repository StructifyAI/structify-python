# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import FileTypes

__all__ = ["TrainingDatasetUploadLabeledStepParams"]


class TrainingDatasetUploadLabeledStepParams(TypedDict, total=False):
    dataset_name: Required[FileTypes]

    step_bytes: Required[FileTypes]
