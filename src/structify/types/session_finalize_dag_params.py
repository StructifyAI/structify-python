# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .edge_spec_param import EdgeSpecParam
from .node_spec_param import NodeSpecParam
from .dashboard_layout_param import DashboardLayoutParam

__all__ = ["SessionFinalizeDagParams"]


class SessionFinalizeDagParams(TypedDict, total=False):
    edges: Required[Iterable[EdgeSpecParam]]

    nodes: Required[Iterable[NodeSpecParam]]

    dashboard_layout: Optional[DashboardLayoutParam]
