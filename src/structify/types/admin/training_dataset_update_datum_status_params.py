# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainingDatasetUpdateDatumStatusParams"]


class TrainingDatasetUpdateDatumStatusParams(TypedDict, total=False):
    id: Required[str]

    status: Required[
        Literal[
            "Unlabeled",
            "NavLabeled",
            "SaveLabeled",
            "Verified",
            "Pending",
            "Skipped",
            "SuspiciousNav",
            "SuspiciousSave",
        ]
    ]

    review_message: Optional[str]
