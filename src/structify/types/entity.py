# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from .._models import BaseModel

__all__ = ["Entity"]


class Entity(BaseModel):
    id: int

    properties: Dict[str, str]

    type: str
