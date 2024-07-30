# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel
from .error_params import ErrorParams

__all__ = ["Error"]


class Error(BaseModel):
    error: ErrorParams = FieldInfo(alias="Error")
