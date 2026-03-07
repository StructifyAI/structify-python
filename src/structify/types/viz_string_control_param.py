# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .viz_string_control_type import VizStringControlType
from .viz_control_option_param import VizControlOptionParam

__all__ = ["VizStringControlParam"]


class VizStringControlParam(TypedDict, total=False):
    label: Required[str]

    options: Required[Iterable[VizControlOptionParam]]

    type: Required[VizStringControlType]
