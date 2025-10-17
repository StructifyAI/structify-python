# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .exploration_status import ExplorationStatus
from .llm_information_store import LlmInformationStore

__all__ = ["ExploreStatusResponse"]


class ExploreStatusResponse(BaseModel):
    status: ExplorationStatus

    error: Optional[str] = None

    result: Optional[LlmInformationStore] = None
    """Information store for LLM context about a connector

    This enum represents different types of connector information that can be
    provided to LLMs for context. It's stored as JSON in the database.

    When deserializing from the database, we attempt to parse into the most specific
    variant first (RelationalDatabase), and fall back to Other if the structure
    doesn't match.
    """

    started_at: Optional[datetime] = None
