# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel
from .wait_params import WaitParams

__all__ = ["Wait"]


class Wait(BaseModel):
    wait: WaitParams = FieldInfo(alias="Wait")
