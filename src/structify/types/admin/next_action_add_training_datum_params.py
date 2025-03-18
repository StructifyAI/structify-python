# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..knowledge_graph_param import KnowledgeGraphParam
from ..save_requirement_param import SaveRequirementParam

__all__ = [
    "NextActionAddTrainingDatumParams",
    "Input",
    "InputAllStep",
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


class Input(TypedDict, total=False):
    all_steps: Required[Iterable[InputAllStep]]

    extraction_criteria: Required[Iterable[SaveRequirementParam]]

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
