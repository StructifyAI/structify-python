# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetGetByIDParams"]


class DatasetGetByIDParams(TypedDict, total=False):
    id: Required[str]
    """ID of the dataset to retrieve"""
