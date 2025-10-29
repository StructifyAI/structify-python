# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .chat_visibility import ChatVisibility

__all__ = ["UpdateVisibilityResponse"]


class UpdateVisibilityResponse(BaseModel):
    visibility: ChatVisibility
