# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..knowledge_graph import KnowledgeGraph

__all__ = [
    "StepChoices",
    "ExtractionCriterion",
    "ExtractionCriterionRequiredRelationship",
    "ExtractionCriterionRequiredEntity",
    "ExtractionCriterionRequiredProperty",
    "StepOption",
]


class ExtractionCriterionRequiredRelationship(BaseModel):
    relationship_name: str


class ExtractionCriterionRequiredEntity(BaseModel):
    seeded_entity_id: int
    """
    The integer id corresponding to an entity in the seeded entity graph (different
    from the global dataset entity id)
    """

    entity_id: Optional[str] = None


class ExtractionCriterionRequiredProperty(BaseModel):
    property_names: List[str]
    """If there are multiple properties, it can match just one of them"""

    table_name: str
    """The table name of the entity to update"""


ExtractionCriterion: TypeAlias = Union[
    ExtractionCriterionRequiredRelationship, ExtractionCriterionRequiredEntity, ExtractionCriterionRequiredProperty
]


class StepOption(BaseModel):
    id: str

    action_name: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None


class StepChoices(BaseModel):
    extraction_criteria: List[ExtractionCriterion]

    job_id: str

    seeded_kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    step_options: List[StepOption]
