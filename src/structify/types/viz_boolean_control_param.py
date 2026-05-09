# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .viz_boolean_control_type import VizBooleanControlType

__all__ = ["VizBooleanControlParam"]


class VizBooleanControlParam(TypedDict, total=False):
    label: Required[str]

    type: Required[VizBooleanControlType]
