# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..knowledge_graph_param import KnowledgeGraphParam

__all__ = [
    "NextActionAddTrainingDatumParams",
    "Input",
    "InputAllStep",
    "InputExtractionCriterion",
    "InputExtractionCriterionRequiredRelationship",
    "InputExtractionCriterionRequiredEntity",
    "InputExtractionCriterionRequiredProperty",
    "Output",
    "OutputSelectedStep",
    "OutputSelectedStepSelectedStep",
    "OutputSearchStep",
    "OutputSearchStepSearchStep",
    "OutputInvalidAction",
    "OutputInvalidActionInvalidAction",
]


class NextActionAddTrainingDatumParams(TypedDict, total=False):
    input: Required[Input]

    label: Required[str]

    output: Required[Output]

    job_id: Optional[str]


class InputAllStep(TypedDict, total=False):
    id: Required[str]

    action_name: str

    metadata: Dict[str, str]


class InputExtractionCriterionRequiredRelationship(TypedDict, total=False):
    relationship_name: Required[str]


class InputExtractionCriterionRequiredEntity(TypedDict, total=False):
    seeded_entity_id: Required[int]
    """
    The integer id corresponding to an entity in the seeded entity graph (different
    from the global dataset entity id)
    """

    entity_id: Optional[str]


class InputExtractionCriterionRequiredProperty(TypedDict, total=False):
    property_names: Required[List[str]]
    """If there are multiple properties, it can match just one of them"""

    table_name: Required[str]
    """The table name of the entity to update"""


InputExtractionCriterion: TypeAlias = Union[
    InputExtractionCriterionRequiredRelationship,
    InputExtractionCriterionRequiredEntity,
    InputExtractionCriterionRequiredProperty,
]


class Input(TypedDict, total=False):
    all_steps: Required[Iterable[InputAllStep]]

    extraction_criteria: Required[Iterable[InputExtractionCriterion]]

    previous_queries: Required[List[str]]

    seeded_kg: Required[KnowledgeGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class OutputSelectedStepSelectedStep(TypedDict, total=False):
    step_id: Required[str]


class OutputSelectedStep(TypedDict, total=False):
    selected_step: Required[Annotated[OutputSelectedStepSelectedStep, PropertyInfo(alias="SelectedStep")]]


class OutputSearchStepSearchStep(TypedDict, total=False):
    search_query: Required[str]


class OutputSearchStep(TypedDict, total=False):
    search_step: Required[Annotated[OutputSearchStepSearchStep, PropertyInfo(alias="SearchStep")]]


class OutputInvalidActionInvalidAction(TypedDict, total=False):
    error: Required[str]

    llm_output: Required[str]


class OutputInvalidAction(TypedDict, total=False):
    invalid_action: Required[Annotated[OutputInvalidActionInvalidAction, PropertyInfo(alias="InvalidAction")]]


Output: TypeAlias = Union[OutputSelectedStep, OutputSearchStep, OutputInvalidAction]
