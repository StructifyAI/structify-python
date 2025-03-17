# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .datum_status import DatumStatus

__all__ = ["TrainingDatasetUpdateDatumStatusParams"]


class TrainingDatasetUpdateDatumStatusParams(TypedDict, total=False):
    id: Required[str]

    status: Required[DatumStatus]

    review_message: Optional[str]
