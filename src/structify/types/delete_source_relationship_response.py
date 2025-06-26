# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DeleteSourceRelationshipResponse"]


class DeleteSourceRelationshipResponse(BaseModel):
    message: str
    """Optional message about the deletion"""

    success: bool
    """Whether the deletion was successful"""
