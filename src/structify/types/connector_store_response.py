# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .llm_information_store import LlmInformationStore

__all__ = ["ConnectorStoreResponse"]


class ConnectorStoreResponse(BaseModel):
    store: Optional[LlmInformationStore] = None
    """Information store for connector schema

    Hierarchical structure: Connector → Database → Schema → Table → Column Works for
    both relational databases and API-based data. Distinguishes between the two by
    presence of `endpoint` on tables:

    - Relational DB: all tables have `endpoint: None`
    - API: all tables have `endpoint: Some(...)`
    """
