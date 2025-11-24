# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .connector import Connector

__all__ = ["ConnectorWithSnippets"]


class ConnectorWithSnippets(Connector):
    usage_snippet_global: Optional[str] = None
