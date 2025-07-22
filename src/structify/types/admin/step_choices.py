# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from ..knowledge_graph import KnowledgeGraph
from ..save_requirement import SaveRequirement

__all__ = ["StepChoices", "StepOption"]


class StepOption(BaseModel):
    id: str

    action_name: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None


class StepChoices(BaseModel):
    extraction_criteria: List[SaveRequirement]

    job_id: str

    seeded_kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """

    step_options: List[StepOption]
