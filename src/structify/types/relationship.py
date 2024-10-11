# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Relationship"]


class Relationship(BaseModel):
    source: int

    target: int

    type: str

    properties: Optional[Dict[str, str]] = None
