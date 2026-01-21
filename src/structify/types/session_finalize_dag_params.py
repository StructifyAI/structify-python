# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .dashboard_param import DashboardParam
from .edge_spec_param import EdgeSpecParam
from .node_spec_param import NodeSpecParam

__all__ = ["SessionFinalizeDagParams"]


class SessionFinalizeDagParams(TypedDict, total=False):
    edges: Required[Iterable[EdgeSpecParam]]

    nodes: Required[Iterable[NodeSpecParam]]

    dashboard_layout: Optional[DashboardParam]
    """
    A page is the top-level container with title/description Can contain multiple
    dashboards with different datasets
    """
