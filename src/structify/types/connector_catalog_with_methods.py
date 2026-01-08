# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .connector_auth_method_with_fields import ConnectorAuthMethodWithFields
from .connector_catalog.connector_catalog import ConnectorCatalog

__all__ = ["ConnectorCatalogWithMethods"]


class ConnectorCatalogWithMethods(ConnectorCatalog):
    auth_methods: List[ConnectorAuthMethodWithFields]

    logo_url: Optional[str] = None
    """Base64 data URI for the logo (e.g., "data:image/svg+xml;base64,...")"""
