# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .viz_figure_kind import VizFigureKind

__all__ = ["VizFigureDefinition"]


class VizFigureDefinition(BaseModel):
    expression: str

    kind: VizFigureKind
