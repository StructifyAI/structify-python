# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .viz_number_control_type import VizNumberControlType

__all__ = ["VizNumberControlParam"]


class VizNumberControlParam(TypedDict, total=False):
    label: Required[str]

    max: Required[float]

    min: Required[float]

    type: Required[VizNumberControlType]

    step: float
