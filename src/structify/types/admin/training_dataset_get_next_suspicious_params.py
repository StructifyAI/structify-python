# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainingDatasetGetNextSuspiciousParams"]


class TrainingDatasetGetNextSuspiciousParams(TypedDict, total=False):
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

    user_restriction: bool
