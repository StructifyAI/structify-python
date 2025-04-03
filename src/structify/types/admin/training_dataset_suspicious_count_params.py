# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .datum_status import DatumStatus

__all__ = ["TrainingDatasetSuspiciousCountParams"]


class TrainingDatasetSuspiciousCountParams(TypedDict, total=False):
    status: Required[DatumStatus]

    dataset_name: Optional[str]

    user_restriction: bool
    """
    If true, the query will only return datums that are suspicious for the current
    user. If false, the query will return datums that are suspicious for any author
    that does not have the Labeler permission.
    """
