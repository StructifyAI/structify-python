# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["RunGetResponse"]


class RunGetResponse(BaseModel):
    date: object

    steps: List[object]

    uuid: str
    """Used to identify this history"""
