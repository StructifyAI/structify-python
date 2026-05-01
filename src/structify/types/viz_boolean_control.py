# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .viz_boolean_control_type import VizBooleanControlType

__all__ = ["VizBooleanControl"]


class VizBooleanControl(BaseModel):
    label: str

    type: VizBooleanControlType
