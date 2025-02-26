# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .datum_status import DatumStatus

__all__ = ["TrainingDatasetMarkDatumSuspiciousParams"]


class TrainingDatasetMarkDatumSuspiciousParams(TypedDict, total=False):
    id: Required[str]

    message: Required[str]

    status: Required[DatumStatus]

    suspicious_id: Required[str]
