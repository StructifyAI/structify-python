# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DatumStatus"]

DatumStatus: TypeAlias = Literal[
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
