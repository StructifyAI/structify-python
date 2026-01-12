# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .connector_auth_method_scope import ConnectorAuthMethodScope

__all__ = ["ListScopesResponse"]


class ListScopesResponse(BaseModel):
    scopes: List[ConnectorAuthMethodScope]
