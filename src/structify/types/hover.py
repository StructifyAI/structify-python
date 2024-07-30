# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel
from .hover_params import HoverParams

__all__ = ["Hover"]


class Hover(BaseModel):
    hover: HoverParams = FieldInfo(alias="Hover")
