# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PlanPauseAllParams"]


class PlanPauseAllParams(TypedDict, total=False):
    dataset_name: Required[str]
    """Name of the dataset to pause plans for"""
