# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Click"]


class Click(BaseModel):
    click: Click = FieldInfo(alias="Click")
