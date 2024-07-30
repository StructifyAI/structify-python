# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Hover"]


class Hover(BaseModel):
    hover: Hover = FieldInfo(alias="Hover")
