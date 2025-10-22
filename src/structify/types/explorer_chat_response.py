# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .connector_explorer_chat import ConnectorExplorerChat

__all__ = ["ExplorerChatResponse"]


class ExplorerChatResponse(BaseModel):
    chats: List[ConnectorExplorerChat]
