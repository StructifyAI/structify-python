# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .connector import Connector

__all__ = ["ConnectorGetResponse", "ConnectorGetResponseSecret"]


class ConnectorGetResponseSecret(BaseModel):
    created_at: datetime

    secret_name: str

    secret_value: str

    updated_at: datetime


class ConnectorGetResponse(Connector):
    secrets: List[ConnectorGetResponseSecret]
