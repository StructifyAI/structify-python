# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AnalyticsCreateTrackerParams"]


class AnalyticsCreateTrackerParams(TypedDict, total=False):
    name: Required[str]

    team_id: Required[str]

    allowed_origins: SequenceNotStr[str]
