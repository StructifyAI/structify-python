# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .dashboard_item import DashboardItem

__all__ = ["ListDashboardsResponse"]


class ListDashboardsResponse(BaseModel):
    commit_hash: str
    """Commit hash used to load dashboard specs."""

    dashboards: List[DashboardItem]
    """All dashboard specs in src/visualizations/\\**.viz.json."""
