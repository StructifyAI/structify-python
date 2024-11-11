# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..knowledge_graph import KnowledgeGraph
from ..extraction_criteria import ExtractionCriteria

__all__ = ["StepChoices", "StepOption"]


class StepOption(BaseModel):
    id: str

    description: str


class StepChoices(BaseModel):
    extraction_criteria: List[ExtractionCriteria]

    job_id: str

    seeded_kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    step_options: List[StepOption]
