# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SessionUpdateNodeProgressParams"]


class SessionUpdateNodeProgressParams(TypedDict, total=False):
    current: Required[int]

    elapsed_seconds: Required[float]

    title: Required[str]

    total: Required[int]
