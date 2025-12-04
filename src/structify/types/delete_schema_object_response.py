# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DeleteSchemaObjectResponse"]


class DeleteSchemaObjectResponse(BaseModel):
    object_id: str
    """The ID of the schema object that was deleted"""

    object_type: str
    """The type of schema object that was deleted"""
