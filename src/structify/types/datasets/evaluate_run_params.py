# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluateRunParams"]


class EvaluateRunParams(TypedDict, total=False):
    dataset_1: Required[str]

    dataset_2: Required[str]

    dataset_2_is_ground_truth: Required[bool]

    merge_threshold_override: Optional[float]
