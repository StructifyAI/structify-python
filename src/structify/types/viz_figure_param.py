# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .viz_figure_definition_param import VizFigureDefinitionParam

__all__ = ["VizFigureParam"]


class VizFigureParam(TypedDict, total=False):
    id: Required[str]

    figure: Required[VizFigureDefinitionParam]

    description: str

    span: int

    title: str
