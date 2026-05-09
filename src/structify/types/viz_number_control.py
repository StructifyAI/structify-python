# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .viz_number_control_type import VizNumberControlType

__all__ = ["VizNumberControl"]


class VizNumberControl(BaseModel):
    label: str

    max: float

    min: float

    type: VizNumberControlType

    step: Optional[float] = None
