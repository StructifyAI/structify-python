# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["StructureEnhanceRelationshipParams", "StopConfig"]


class StructureEnhanceRelationshipParams(TypedDict, total=False):
    entity_id: Required[str]

    relationship_name: Required[str]

    allow_extra_entities: bool

    banned_domains: List[str]

    node_id: Optional[str]

    special_job_type: Optional[Literal["HumanLLM"]]

    starting_searches: List[str]

    starting_urls: List[str]

    stop_config: Optional[StopConfig]
    """Configuration parameters for the StopChecker"""


class StopConfig(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]
