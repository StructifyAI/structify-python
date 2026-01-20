# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .dashboard_param import DashboardParam

__all__ = ["SessionUploadDashboardLayoutParams"]


class SessionUploadDashboardLayoutParams(TypedDict, total=False):
    layout: Required[DashboardParam]
    """
    A page is the top-level container with title/description Can contain multiple
    dashboards with different datasets
    """
