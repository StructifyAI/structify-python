# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .datum_status import DatumStatus

__all__ = ["TrainingDatasetGetNextSuspiciousParams"]


class TrainingDatasetGetNextSuspiciousParams(TypedDict, total=False):
    status: Required[DatumStatus]

    dataset_name: Optional[str]

    user_restriction: bool
