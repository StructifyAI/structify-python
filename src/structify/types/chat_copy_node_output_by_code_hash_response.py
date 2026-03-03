# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ChatCopyNodeOutputByCodeHashResponse"]


class ChatCopyNodeOutputByCodeHashResponse(BaseModel):
    cached_node_id: Optional[str] = None
