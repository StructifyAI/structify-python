# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .connector_auth_method import ConnectorAuthMethod
from .connector_credential_field import ConnectorCredentialField

__all__ = ["ConnectorAuthMethodWithFields"]


class ConnectorAuthMethodWithFields(ConnectorAuthMethod):
    credential_fields: List[ConnectorCredentialField]
