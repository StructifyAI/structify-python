# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..knowledge_graph import KnowledgeGraph

__all__ = [
    "StepChoices",
    "ExtractionCriterion",
    "ExtractionCriterionRelationship",
    "ExtractionCriterionRelationshipRelationship",
    "ExtractionCriterionEntity",
    "ExtractionCriterionEntityEntity",
    "ExtractionCriterionProperty",
    "ExtractionCriterionPropertyProperty",
    "StepOption",
]


class ExtractionCriterionRelationshipRelationship(BaseModel):
    relationship_name: str


class ExtractionCriterionRelationship(BaseModel):
    relationship: ExtractionCriterionRelationshipRelationship = FieldInfo(alias="Relationship")


class ExtractionCriterionEntityEntity(BaseModel):
    seeded_kg_id: int
    """The integer id corresponding to an entity in the seeded kg"""

    dataset_entity_id: Optional[str] = None


class ExtractionCriterionEntity(BaseModel):
    entity: ExtractionCriterionEntityEntity = FieldInfo(alias="Entity")


class ExtractionCriterionPropertyProperty(BaseModel):
    property_names: List[str]

    table_name: str
    """Vec<ExtractionCriteria> = it has to meet every one."""


class ExtractionCriterionProperty(BaseModel):
    property: ExtractionCriterionPropertyProperty = FieldInfo(alias="Property")


ExtractionCriterion: TypeAlias = Union[
    ExtractionCriterionRelationship, ExtractionCriterionEntity, ExtractionCriterionProperty
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
