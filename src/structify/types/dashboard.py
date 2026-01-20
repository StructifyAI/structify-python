# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .dashboard_page import DashboardPage

__all__ = ["Dashboard"]


class Dashboard(BaseModel):
    """
    A page is the top-level container with title/description
    Can contain multiple dashboards with different datasets
    """

    dashboards: List[DashboardPage]
    """One or more dashboards on this page"""

    title: str
    """Page title"""

    description: Optional[str] = None
    """Optional page description"""
