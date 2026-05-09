# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AnalyticsListTrackersParams"]


class AnalyticsListTrackersParams(TypedDict, total=False):
    team_id: Required[str]
    """Team to list trackers for"""
