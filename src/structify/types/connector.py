# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .connector_category import ConnectorCategory
from .exploration_status import ExplorationStatus

__all__ = ["Connector"]


class Connector(BaseModel):
    id: str

    created_at: datetime

    exploration_status: ExplorationStatus

    known_connector_type: str

    name: str

    team_id: str

    team_visibility: Literal["Team", "Private"]

    updated_at: datetime

    connector_category: Optional[ConnectorCategory] = None

    datahub_urn: Optional[str] = None

    deleted_at: Optional[datetime] = None

    description: Optional[str] = None

    exploration_error: Optional[str] = None

    exploration_started_at: Optional[datetime] = None

    nango_connection_id: Optional[str] = None

    nango_integration_id: Optional[str] = None

    oauth_scopes: Optional[List[Optional[str]]] = None

    usage_snippet_override: Optional[str] = None
