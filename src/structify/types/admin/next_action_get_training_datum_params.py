# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NextActionGetTrainingDatumParams"]


class NextActionGetTrainingDatumParams(TypedDict, total=False):
    id: Required[str]
    """ID of the training datum to get"""
