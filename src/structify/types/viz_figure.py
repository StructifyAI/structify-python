# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .viz_figure_definition import VizFigureDefinition

__all__ = ["VizFigure"]


class VizFigure(BaseModel):
    id: str

    figure: VizFigureDefinition

    description: Optional[str] = None

    span: Optional[int] = None

    title: Optional[str] = None
