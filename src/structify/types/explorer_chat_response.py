# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .connector_explorer_chat import ConnectorExplorerChat

__all__ = ["ExplorerChatResponse"]


class ExplorerChatResponse(BaseModel):
    chat: ConnectorExplorerChat
    """Connector explorer chat with deserialized ChatPrompt for API responses"""
