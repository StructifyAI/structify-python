# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Connector"]


class Connector(BaseModel):
    id: str

    created_at: datetime

    known_connector_type: Literal[
        "Slack",
        "Confluence",
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

    llm_information_store: str

    name: str

    project_id: str

    updated_at: datetime

    description: Optional[str] = None

    refresh_script: Optional[str] = None
