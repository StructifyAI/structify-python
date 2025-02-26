# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .datum_status import DatumStatus

__all__ = ["TrainingDatasetGetNextForQaParams"]


class TrainingDatasetGetNextForQaParams(TypedDict, total=False):
    dataset_name: Required[str]

    status: Required[DatumStatus]
