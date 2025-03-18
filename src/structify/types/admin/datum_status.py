# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DatumStatus"]

DatumStatus: TypeAlias = Literal[
    "unlabeled",
    "nav_labeled",
    "save_labeled",
    "nav_verified",
    "save_verified",
    "pending",
    "skipped",
    "suspicious_nav",
    "suspicious_save",
    "potential_suspicious_nav",
    "potential_suspicious_save",
]
