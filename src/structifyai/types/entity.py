# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional

from .._models import BaseModel

__all__ = ["Entity"]


class Entity(BaseModel):
    id: int

    label: str
    """
    Since all Entities have exactly two labels (ENTITY_LABEL and their table name),
    we only store the non-ENTITY_LABEL label here.
    """

    properties: Dict[str, Union[Optional[str], Optional[bool], Optional[int]]]
