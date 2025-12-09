# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .chat_event import ChatEvent
from .chat_prompt import ChatPrompt
from .exploration_phase_id import ExplorationPhaseID

__all__ = ["ConnectorExplorerChat"]


class ConnectorExplorerChat(BaseModel):
    """Connector explorer chat with deserialized ChatPrompt for API responses"""

    id: str

    chat_events: List[ChatEvent]

    chat_prompt: ChatPrompt

    connector_id: str

    created_at: datetime

    exploration_run_id: str

    phase_id: ExplorationPhaseID
    """Identifies the phase of connector exploration

    This enum is used to track which phase of exploration a chat session belongs to.
    It's stored as JSONB in the database to allow for flexible phase identification.
    """
