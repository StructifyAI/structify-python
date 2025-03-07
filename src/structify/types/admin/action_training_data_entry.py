# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..knowledge_graph import KnowledgeGraph
from ..save_requirement import SaveRequirement

__all__ = [
    "ActionTrainingDataEntry",
    "Input",
    "InputAllStep",
    "Output",
    "OutputOutput",
    "OutputOutputSelectedStep",
    "OutputOutputSelectedStepSelectedStep",
    "OutputOutputSearchStep",
    "OutputOutputSearchStepSearchStep",
    "OutputOutputInvalidAction",
    "OutputOutputInvalidActionInvalidAction",
]


class InputAllStep(BaseModel):
    id: str

    action_name: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None


class Input(BaseModel):
    all_steps: List[InputAllStep]

    extraction_criteria: List[SaveRequirement]

    previous_queries: List[str]

    seeded_kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """


class OutputOutputSelectedStepSelectedStep(BaseModel):
    step_id: str


class OutputOutputSelectedStep(BaseModel):
    selected_step: OutputOutputSelectedStepSelectedStep = FieldInfo(alias="SelectedStep")


class OutputOutputSearchStepSearchStep(BaseModel):
    search_query: str


class OutputOutputSearchStep(BaseModel):
    search_step: OutputOutputSearchStepSearchStep = FieldInfo(alias="SearchStep")


class OutputOutputInvalidActionInvalidAction(BaseModel):
    error: str

    llm_output: str


class OutputOutputInvalidAction(BaseModel):
    invalid_action: OutputOutputInvalidActionInvalidAction = FieldInfo(alias="InvalidAction")


OutputOutput: TypeAlias = Union[OutputOutputSelectedStep, OutputOutputSearchStep, OutputOutputInvalidAction]


class Output(BaseModel):
    id: str

    created_at: datetime

    label: str

    output: OutputOutput


class ActionTrainingDataEntry(BaseModel):
    id: str

    author: str

    created_at: datetime

    input: Input

    outputs: List[Output]
