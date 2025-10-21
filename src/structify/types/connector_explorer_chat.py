# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .chat_prompt import ChatPrompt

__all__ = ["ConnectorExplorerChat"]


class ConnectorExplorerChat(BaseModel):
    id: str

    chat_prompt: ChatPrompt

    connector_id: str

    created_at: datetime

    exploration_run_id: str
