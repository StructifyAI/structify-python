# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .viz_figure_kind import VizFigureKind

__all__ = ["VizFigureDefinitionParam"]


class VizFigureDefinitionParam(TypedDict, total=False):
    expression: Required[str]

    kind: Required[VizFigureKind]
