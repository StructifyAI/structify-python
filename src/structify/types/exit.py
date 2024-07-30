# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel
from .exit_params import ExitParams

__all__ = ["Exit"]


class Exit(BaseModel):
    exit: ExitParams = FieldInfo(alias="Exit")
    """For tools with no inputs."""
