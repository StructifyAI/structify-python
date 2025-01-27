# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainingDatasetGetNextDatumParams"]


class TrainingDatasetGetNextDatumParams(TypedDict, total=False):
    dataset_name: Required[str]

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
