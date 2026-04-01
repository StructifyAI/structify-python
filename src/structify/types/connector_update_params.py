# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr
from .chat_session_role import ChatSessionRole
from .connector_category import ConnectorCategory
from .datahub_secret_map_param import DatahubSecretMapParam

__all__ = ["ConnectorUpdateParams"]


class ConnectorUpdateParams(TypedDict, total=False):
    connector_category: Optional[ConnectorCategory]

    datahub_ingestion_type: Optional[str]

    datahub_secret_map: Optional[DatahubSecretMapParam]
    """
    Maps DatahubIngestionKey to the name of the connector secret that holds the
    value.
    """

    datahub_urn: Optional[str]

    description: Optional[str]

    known_connector_type: Optional[str]

    name: Optional[str]

    nango_connection_id: Optional[str]

    oauth_scopes: Optional[SequenceNotStr[Optional[str]]]

    owner_user_id: Optional[str]

    refresh_cron_schedule: Optional[str]

    shared_user_roles: Optional[Dict[str, ChatSessionRole]]

    team_visibility: Optional[Literal["Team", "Private"]]

    usage_snippet_override: Optional[str]
