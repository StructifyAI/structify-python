# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .dashboard_layout_param import DashboardLayoutParam

__all__ = ["SessionUploadDashboardLayoutParams"]


class SessionUploadDashboardLayoutParams(TypedDict, total=False):
    layout: Required[DashboardLayoutParam]
