# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .viz_control_option import VizControlOption
from .viz_string_control_type import VizStringControlType

__all__ = ["VizStringControl"]


class VizStringControl(BaseModel):
    label: str

    options: List[VizControlOption]

    type: VizStringControlType
