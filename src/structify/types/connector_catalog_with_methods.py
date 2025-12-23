# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .connector_auth_method_with_fields import ConnectorAuthMethodWithFields
from .connector_catalog.connector_catalog import ConnectorCatalog

__all__ = ["ConnectorCatalogWithMethods"]


class ConnectorCatalogWithMethods(ConnectorCatalog):
    auth_methods: List[ConnectorAuthMethodWithFields]
