# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ConnectorTablePathResponse"]


class ConnectorTablePathResponse(BaseModel):
    connector_id: str

    database_name: str

    schema_name: str

    table_name: str
