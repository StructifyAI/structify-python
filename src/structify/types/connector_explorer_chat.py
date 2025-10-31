# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .chat_prompt import ChatPrompt

__all__ = [
    "ConnectorExplorerChat",
    "PhaseID",
    "PhaseIDDiscoverTables",
    "PhaseIDDiscoverColumns",
    "PhaseIDDiscoverAPIResources",
    "PhaseIDDiscoverAPIFields",
]


class PhaseIDDiscoverTables(BaseModel):
    type: Literal["discover_tables"]


class PhaseIDDiscoverColumns(BaseModel):
    table_name: str

    type: Literal["discover_columns"]


class PhaseIDDiscoverAPIResources(BaseModel):
    known_connector_type: Literal[
        "Slack",
        "Confluence",
        "Dropbox",
        "GoogleDrive",
        "Snowflake",
        "Hubspot",
        "Salesforce",
        "Supabase",
        "Sharepoint",
        "Notion",
        "Jira",
        "Linear",
        "Intercom",
        "Gmail",
        "Airtable",
        "Trello",
        "Postgresql",
        "Sap",
        "Oracle",
        "Manual",
    ]

    type: Literal["discover_api_resources"]


class PhaseIDDiscoverAPIFields(BaseModel):
    known_connector_type: Literal[
        "Slack",
        "Confluence",
        "Dropbox",
        "GoogleDrive",
        "Snowflake",
        "Hubspot",
        "Salesforce",
        "Supabase",
        "Sharepoint",
        "Notion",
        "Jira",
        "Linear",
        "Intercom",
        "Gmail",
        "Airtable",
        "Trello",
        "Postgresql",
        "Sap",
        "Oracle",
        "Manual",
    ]

    resource_name: str

    type: Literal["discover_api_fields"]


PhaseID: TypeAlias = Annotated[
    Union[PhaseIDDiscoverTables, PhaseIDDiscoverColumns, PhaseIDDiscoverAPIResources, PhaseIDDiscoverAPIFields],
    PropertyInfo(discriminator="type"),
]


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
