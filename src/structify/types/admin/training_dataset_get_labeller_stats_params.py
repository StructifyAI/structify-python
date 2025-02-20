# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TrainingDatasetGetLabellerStatsParams"]


class TrainingDatasetGetLabellerStatsParams(TypedDict, total=False):
    status: Required[
        Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "NavVerified",
            "SaveVerified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
            "PotentialSuspiciousNav",
            "PotentialSuspiciousSave",
        ]
    ]

    dataset_name: Optional[str]

    end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    labeled_status: Literal["NonSuspicious", "SuspiciousOnly", "VerifiedOnly"]

    return_prop_count: bool

    start_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
