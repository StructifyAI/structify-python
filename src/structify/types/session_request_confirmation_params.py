# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionRequestConfirmationParams"]


class SessionRequestConfirmationParams(TypedDict, total=False):
    operation: Required[Literal["tag", "pdf", "web", "match"]]

    row_count: Required[int]
