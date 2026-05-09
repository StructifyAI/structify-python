# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .viz_date_control_type import VizDateControlType

__all__ = ["VizDateControl"]


class VizDateControl(BaseModel):
    label: str

    type: VizDateControlType
