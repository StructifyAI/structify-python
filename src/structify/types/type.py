# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel
from .type_params import TypeParams

__all__ = ["Type"]


class Type(BaseModel):
    type: TypeParams = FieldInfo(alias="Type")
