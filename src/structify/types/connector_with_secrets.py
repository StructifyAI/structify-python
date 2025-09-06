# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .connector import Connector

__all__ = ["ConnectorWithSecrets", "ConnectorWithSecretsSecret"]


class ConnectorWithSecretsSecret(BaseModel):
    id: str

    created_at: datetime

    secret_name: str

    updated_at: datetime


class ConnectorWithSecrets(Connector):
    secrets: List[ConnectorWithSecretsSecret]
