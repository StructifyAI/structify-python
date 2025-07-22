# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..chat_prompt import ChatPrompt
from ..knowledge_graph import KnowledgeGraph
from ..save_requirement import SaveRequirement
from ..dataset_descriptor import DatasetDescriptor

__all__ = [
    "ActionTrainingDataEntry",
    "Input",
    "InputAllStep",
    "InputPreviousAction",
    "InputPreviousActionSelectedStep",
    "InputPreviousActionSelectedStepSelectedStep",
    "InputPreviousActionSelectedStepSelectedStepInfo",
    "InputPreviousActionSearchStep",
    "InputPreviousActionSearchStepSearchStep",
    "InputPreviousActionInvalidAction",
    "InputPreviousActionInvalidActionInvalidAction",
    "InputPreviousActionExit",
    "InputPreviousActionExitExit",
    "Output",
    "OutputOutput",
    "OutputOutputSelectedStep",
    "OutputOutputSelectedStepSelectedStep",
    "OutputOutputSelectedStepSelectedStepInfo",
    "OutputOutputSearchStep",
    "OutputOutputSearchStepSearchStep",
    "OutputOutputInvalidAction",
    "OutputOutputInvalidActionInvalidAction",
    "OutputOutputExit",
    "OutputOutputExitExit",
]


class InputAllStep(BaseModel):
    id: str

    action_name: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None


class InputPreviousActionSelectedStepSelectedStepInfo(BaseModel):
    id: str

    action_name: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None


class InputPreviousActionSelectedStepSelectedStep(BaseModel):
    info: InputPreviousActionSelectedStepSelectedStepInfo

    llm_input: ChatPrompt

    llm_output: str

    step_id: str


class InputPreviousActionSelectedStep(BaseModel):
    selected_step: InputPreviousActionSelectedStepSelectedStep = FieldInfo(alias="SelectedStep")


class InputPreviousActionSearchStepSearchStep(BaseModel):
    llm_input: ChatPrompt

    llm_output: str

    search_query: str


class InputPreviousActionSearchStep(BaseModel):
    search_step: InputPreviousActionSearchStepSearchStep = FieldInfo(alias="SearchStep")


class InputPreviousActionInvalidActionInvalidAction(BaseModel):
    error: str

    llm_input: ChatPrompt

    llm_output: str


class InputPreviousActionInvalidAction(BaseModel):
    invalid_action: InputPreviousActionInvalidActionInvalidAction = FieldInfo(alias="InvalidAction")


class InputPreviousActionExitExit(BaseModel):
    llm_input: ChatPrompt

    llm_output: str


class InputPreviousActionExit(BaseModel):
    exit: InputPreviousActionExitExit = FieldInfo(alias="Exit")


InputPreviousAction: TypeAlias = Union[
    InputPreviousActionSelectedStep,
    InputPreviousActionSearchStep,
    InputPreviousActionInvalidAction,
    InputPreviousActionExit,
]


class Input(BaseModel):
    all_steps: List[InputAllStep]

    descriptor: DatasetDescriptor
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extraction_criteria: List[SaveRequirement]

    previous_actions: List[InputPreviousAction]

    seeded_kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class OutputOutputSelectedStepSelectedStepInfo(BaseModel):
    id: str

    action_name: Optional[str] = None

    metadata: Optional[Dict[str, str]] = None


class OutputOutputSelectedStepSelectedStep(BaseModel):
    info: OutputOutputSelectedStepSelectedStepInfo

    llm_input: ChatPrompt

    llm_output: str

    step_id: str


class OutputOutputSelectedStep(BaseModel):
    selected_step: OutputOutputSelectedStepSelectedStep = FieldInfo(alias="SelectedStep")


class OutputOutputSearchStepSearchStep(BaseModel):
    llm_input: ChatPrompt

    llm_output: str

    search_query: str


class OutputOutputSearchStep(BaseModel):
    search_step: OutputOutputSearchStepSearchStep = FieldInfo(alias="SearchStep")


class OutputOutputInvalidActionInvalidAction(BaseModel):
    error: str

    llm_input: ChatPrompt

    llm_output: str


class OutputOutputInvalidAction(BaseModel):
    invalid_action: OutputOutputInvalidActionInvalidAction = FieldInfo(alias="InvalidAction")


class OutputOutputExitExit(BaseModel):
    llm_input: ChatPrompt

    llm_output: str


class OutputOutputExit(BaseModel):
    exit: OutputOutputExitExit = FieldInfo(alias="Exit")


OutputOutput: TypeAlias = Union[
    OutputOutputSelectedStep, OutputOutputSearchStep, OutputOutputInvalidAction, OutputOutputExit
]


class Output(BaseModel):
    id: str

    created_at: datetime

    label: Literal["HumanLLMLabel", "LLMOutput", "Pending", "Reviewed", "Verified", "Others"]

    output: OutputOutput


class ActionTrainingDataEntry(BaseModel):
    id: str

    author: str

    created_at: datetime

    input: Input

    input_prompt: str

    outputs: List[Output]
