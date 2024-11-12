# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainingDatasetGetNextUnverifiedParams"]


class TrainingDatasetGetNextUnverifiedParams(TypedDict, total=False):
    dataset_name: Required[str]

    status: Required[Literal["Unlabeled", "Labeled", "Verified", "Pending", "Skipped", "Suspicious"]]
