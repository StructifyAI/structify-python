# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .chat_prompt import ChatPrompt

__all__ = ["ConnectorExplorerChat", "PhaseID", "PhaseIDDiscoverTables", "PhaseIDDiscoverColumns"]


class PhaseIDDiscoverTables(BaseModel):
    type: Literal["discover_tables"]


class PhaseIDDiscoverColumns(BaseModel):
    table_name: str

    type: Literal["discover_columns"]


PhaseID: TypeAlias = Annotated[Union[PhaseIDDiscoverTables, PhaseIDDiscoverColumns], PropertyInfo(discriminator="type")]


class ConnectorExplorerChat(BaseModel):
    id: str

    chat_prompt: ChatPrompt

    connector_id: str

    created_at: datetime

    exploration_run_id: str

    phase_id: PhaseID
    """Identifies the phase of connector exploration

    This enum is used to track which phase of exploration a chat session belongs to.
    It's stored as JSONB in the database to allow for flexible phase identification.
    """
