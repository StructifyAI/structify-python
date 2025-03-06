# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from ..entity_graph_param import EntityGraphParam
from .step_choice_info_param import StepChoiceInfoParam
from ..extraction_criteria_param import ExtractionCriteriaParam

__all__ = ["NextActionInputParam"]


class NextActionInputParam(TypedDict, total=False):
    all_steps: Required[Iterable[StepChoiceInfoParam]]

    extraction_criteria: Required[Iterable[ExtractionCriteriaParam]]

    previous_queries: Required[List[str]]

    seeded_kg: Required[EntityGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """
