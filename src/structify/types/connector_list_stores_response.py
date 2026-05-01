# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .llm_information_store import LlmInformationStore

__all__ = ["ConnectorListStoresResponse"]

ConnectorListStoresResponse: TypeAlias = Dict[str, LlmInformationStore]
