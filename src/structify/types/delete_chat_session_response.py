# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DeleteChatSessionResponse"]


class DeleteChatSessionResponse(BaseModel):
    """Success response for delete operations"""

    message: str

    success: bool
