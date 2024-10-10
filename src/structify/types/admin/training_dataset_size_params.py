# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainingDatasetSizeParams"]


class TrainingDatasetSizeParams(TypedDict, total=False):
    dataset_name: Required[str]

    status: Optional[Literal["Unverified", "Verified", "Pending", "Skipped"]]
