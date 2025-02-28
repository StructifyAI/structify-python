# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainingDatasetGetNextForLabelingParams"]


class TrainingDatasetGetNextForLabelingParams(TypedDict, total=False):
    dataset_name: Required[str]

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
