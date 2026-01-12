# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["ConnectorAuthMethodScope"]


class ConnectorAuthMethodScope(BaseModel):
    id: str

    connector_auth_method_id: str

    created_at: datetime

    is_recommended: bool

    is_required: bool

    query_parameter: str

    scope_value: str

    updated_at: datetime
