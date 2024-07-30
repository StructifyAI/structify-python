# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Exit"]


class Exit(BaseModel):
    exit: Exit = FieldInfo(alias="Exit")
    """For tools with no inputs."""
