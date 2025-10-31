# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ConnectorUpdateParams"]


class ConnectorUpdateParams(TypedDict, total=False):
    description: Optional[str]

    known_connector_type: Optional[
        Literal[
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
    ]

    name: Optional[str]

    refresh_script: Optional[str]
