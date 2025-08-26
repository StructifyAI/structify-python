# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .knowledge_graph_param import KnowledgeGraphParam
from .save_requirement_param import SaveRequirementParam

__all__ = ["ScrapeScrapeParams", "StopConfig"]


class ScrapeScrapeParams(TypedDict, total=False):
    dataset_name: Required[str]

    extraction_criteria: Required[Iterable[SaveRequirementParam]]

    url: Required[str]

    node_id: Optional[str]

    seeded_kg: Optional[KnowledgeGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """

    stop_config: Optional[StopConfig]
    """Configuration parameters for the StopChecker"""

    use_proxy: Optional[bool]


class StopConfig(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]
