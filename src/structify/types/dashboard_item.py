# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .dashboard_spec import DashboardSpec

__all__ = ["DashboardItem"]


class DashboardItem(BaseModel):
    file_name: str
    """File path relative to repository root."""

    spec: DashboardSpec
