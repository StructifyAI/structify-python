# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["StructureFindRelationshipParams", "StopConfig"]


class StructureFindRelationshipParams(TypedDict, total=False):
    from_id: Required[str]

    relationship_name: Required[str]

    to_id: Required[str]

    allow_extra_entities: bool

    banned_domains: SequenceNotStr[str]

    special_job_type: Optional[Literal["HumanLLM"]]

    starting_searches: SequenceNotStr[str]

    starting_urls: SequenceNotStr[str]

    stop_config: Optional[StopConfig]
    """Configuration parameters for the StopChecker"""


class StopConfig(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]
