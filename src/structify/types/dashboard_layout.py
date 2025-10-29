# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .dashboard_component import DashboardComponent

__all__ = ["DashboardLayout"]


class DashboardLayout(BaseModel):
    components: List[DashboardComponent]

    title: str

    description: Optional[str] = None
