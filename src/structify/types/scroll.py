# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel
from .scroll_params import ScrollParams

__all__ = ["Scroll"]


class Scroll(BaseModel):
    scroll: ScrollParams = FieldInfo(alias="Scroll")
    """For tools with no inputs."""
