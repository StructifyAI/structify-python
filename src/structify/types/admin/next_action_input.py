# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..entity_graph import EntityGraph
from .step_choice_info import StepChoiceInfo
from ..extraction_criteria import ExtractionCriteria

__all__ = ["NextActionInput"]


class NextActionInput(BaseModel):
    all_steps: List[StepChoiceInfo]

    extraction_criteria: List[ExtractionCriteria]

    previous_queries: List[str]

    seeded_kg: EntityGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """
