# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .viz_date_control_type import VizDateControlType

__all__ = ["VizDateControlParam"]


class VizDateControlParam(TypedDict, total=False):
    label: Required[str]

    type: Required[VizDateControlType]
