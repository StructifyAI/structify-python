# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Google"]


class Google(BaseModel):
    google: Google = FieldInfo(alias="Google")
