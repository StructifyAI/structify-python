# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["WaitParams"]


class WaitParams(BaseModel):
    seconds: int
    """Time in seconds to wait"""
