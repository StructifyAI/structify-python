# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .exploration_status import ExplorationStatus

__all__ = ["Connector"]


class Connector(BaseModel):
    id: str

    created_at: datetime

    known_connector_type: str

    name: str

    team_id: str

    updated_at: datetime

    active_store_version_id: Optional[str] = None

    datahub_urn: Optional[str] = None

    description: Optional[str] = None

    exploration_error: Optional[str] = None

    exploration_started_at: Optional[datetime] = None

    exploration_status: Optional[ExplorationStatus] = None

    pipedream_account_id: Optional[str] = None

    refresh_script: Optional[str] = None
