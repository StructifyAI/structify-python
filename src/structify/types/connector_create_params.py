# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConnectorCreateParams"]


class ConnectorCreateParams(TypedDict, total=False):
    known_connector_type: Required[
        Literal[
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
    ]

    llm_information_store: Required[str]

    name: Required[str]

    project_id: Required[str]

    description: Optional[str]

    refresh_script: Optional[str]

    secrets: Dict[str, str]
    """Optional secrets/environment variables for the connector"""
