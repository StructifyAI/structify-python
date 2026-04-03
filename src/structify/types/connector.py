# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .connector_category import ConnectorCategory
from .datahub_secret_map import DatahubSecretMap

__all__ = ["Connector"]


class Connector(BaseModel):
    id: str

    created_at: datetime

    known_connector_type: str

    name: str

    owner_user_id: str

    team_id: str

    team_visibility: Literal["Team", "Private"]

    updated_at: datetime

    connector_category: Optional[ConnectorCategory] = None

    datahub_ingestion_type: Optional[str] = None

    datahub_secret_map: Optional[DatahubSecretMap] = None
    """
    Maps DatahubIngestionKey to the name of the connector secret that holds the
    value.
    """

    datahub_urn: Optional[str] = None

    deleted_at: Optional[datetime] = None

    description: Optional[str] = None

    nango_connection_id: Optional[str] = None

    oauth_scopes: Optional[List[Optional[str]]] = None

    refresh_cron_schedule: Optional[str] = None

    refresh_next_run_at: Optional[datetime] = None

    usage_snippet_override: Optional[str] = None
