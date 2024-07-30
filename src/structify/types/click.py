# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel
from .click_params import ClickParams

__all__ = ["Click"]


class Click(BaseModel):
    click: ClickParams = FieldInfo(alias="Click")
