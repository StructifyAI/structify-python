# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel
from .viz_param import VizParam
from .viz_query import VizQuery
from .viz_figure import VizFigure

__all__ = ["DashboardSpec"]


class DashboardSpec(BaseModel):
    dataset: str

    description: str

    figures: List[VizFigure]

    params: Dict[str, VizParam]

    queries: List[VizQuery]

    title: str

    version: str
