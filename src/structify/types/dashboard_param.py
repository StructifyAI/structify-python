# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .dashboard_page_param import DashboardPageParam

__all__ = ["DashboardParam"]


class DashboardParam(TypedDict, total=False):
    """
    A page is the top-level container with title/description
    Can contain multiple dashboards with different datasets
    """

    dashboards: Required[Iterable[DashboardPageParam]]
    """One or more dashboards on this page"""

    title: Required[str]
    """Page title"""

    description: Optional[str]
    """Optional page description"""
