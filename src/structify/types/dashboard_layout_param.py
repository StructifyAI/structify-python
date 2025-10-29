# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .dashboard_component_param import DashboardComponentParam

__all__ = ["DashboardLayoutParam"]


class DashboardLayoutParam(TypedDict, total=False):
    components: Required[Iterable[DashboardComponentParam]]

    title: Required[str]

    description: Optional[str]
