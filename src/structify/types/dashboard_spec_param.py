# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

from .viz_param_param import VizParamParam
from .viz_query_param import VizQueryParam
from .viz_figure_param import VizFigureParam

__all__ = ["DashboardSpecParam"]


class DashboardSpecParam(TypedDict, total=False):
    dataset: Required[str]

    description: Required[str]

    figures: Required[Iterable[VizFigureParam]]

    params: Required[Dict[str, VizParamParam]]

    queries: Required[Iterable[VizQueryParam]]

    title: Required[str]

    version: Required[str]
