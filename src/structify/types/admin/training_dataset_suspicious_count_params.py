# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainingDatasetSuspiciousCountParams"]


class TrainingDatasetSuspiciousCountParams(TypedDict, total=False):
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

    user_restrict: bool
