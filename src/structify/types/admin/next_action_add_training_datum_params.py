# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..chat_prompt_param import ChatPromptParam
from ..knowledge_graph_param import KnowledgeGraphParam
from ..save_requirement_param import SaveRequirementParam
from ..dataset_descriptor_param import DatasetDescriptorParam

__all__ = [
    "NextActionAddTrainingDatumParams",
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
    "OutputSelectedStep",
    "OutputSelectedStepSelectedStep",
    "OutputSelectedStepSelectedStepInfo",
    "OutputSearchStep",
    "OutputSearchStepSearchStep",
    "OutputInvalidAction",
    "OutputInvalidActionInvalidAction",
    "OutputExit",
    "OutputExitExit",
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


class InputPreviousActionSelectedStepSelectedStepInfo(TypedDict, total=False):
    id: Required[str]

    action_name: str

    metadata: Dict[str, str]


class InputPreviousActionSelectedStepSelectedStep(TypedDict, total=False):
    info: Required[InputPreviousActionSelectedStepSelectedStepInfo]

    llm_input: Required[ChatPromptParam]

    llm_output: Required[str]

    step_id: Required[str]


class InputPreviousActionSelectedStep(TypedDict, total=False):
    selected_step: Required[Annotated[InputPreviousActionSelectedStepSelectedStep, PropertyInfo(alias="SelectedStep")]]


class InputPreviousActionSearchStepSearchStep(TypedDict, total=False):
    llm_input: Required[ChatPromptParam]

    llm_output: Required[str]

    search_query: Required[str]


class InputPreviousActionSearchStep(TypedDict, total=False):
    search_step: Required[Annotated[InputPreviousActionSearchStepSearchStep, PropertyInfo(alias="SearchStep")]]


class InputPreviousActionInvalidActionInvalidAction(TypedDict, total=False):
    error: Required[str]

    llm_input: Required[ChatPromptParam]

    llm_output: Required[str]


class InputPreviousActionInvalidAction(TypedDict, total=False):
    invalid_action: Required[
        Annotated[InputPreviousActionInvalidActionInvalidAction, PropertyInfo(alias="InvalidAction")]
    ]


class InputPreviousActionExitExit(TypedDict, total=False):
    llm_input: Required[ChatPromptParam]

    llm_output: Required[str]


class InputPreviousActionExit(TypedDict, total=False):
    exit: Required[Annotated[InputPreviousActionExitExit, PropertyInfo(alias="Exit")]]


InputPreviousAction: TypeAlias = Union[
    InputPreviousActionSelectedStep,
    InputPreviousActionSearchStep,
    InputPreviousActionInvalidAction,
    InputPreviousActionExit,
]


class Input(TypedDict, total=False):
    all_steps: Required[Iterable[InputAllStep]]

    descriptor: Required[DatasetDescriptorParam]
    """A dataset is where you put multiple referential schemas.

    A dataset is a complete namespace where all references between schemas are held
    within the dataset.
    """

    extraction_criteria: Required[Iterable[SaveRequirementParam]]

    previous_actions: Required[Iterable[InputPreviousAction]]

    seeded_kg: Required[KnowledgeGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """


class OutputSelectedStepSelectedStepInfo(TypedDict, total=False):
    id: Required[str]

    action_name: str

    metadata: Dict[str, str]


class OutputSelectedStepSelectedStep(TypedDict, total=False):
    info: Required[OutputSelectedStepSelectedStepInfo]

    llm_input: Required[ChatPromptParam]

    llm_output: Required[str]

    step_id: Required[str]


class OutputSelectedStep(TypedDict, total=False):
    selected_step: Required[Annotated[OutputSelectedStepSelectedStep, PropertyInfo(alias="SelectedStep")]]


class OutputSearchStepSearchStep(TypedDict, total=False):
    llm_input: Required[ChatPromptParam]

    llm_output: Required[str]

    search_query: Required[str]


class OutputSearchStep(TypedDict, total=False):
    search_step: Required[Annotated[OutputSearchStepSearchStep, PropertyInfo(alias="SearchStep")]]


class OutputInvalidActionInvalidAction(TypedDict, total=False):
    error: Required[str]

    llm_input: Required[ChatPromptParam]

    llm_output: Required[str]


class OutputInvalidAction(TypedDict, total=False):
    invalid_action: Required[Annotated[OutputInvalidActionInvalidAction, PropertyInfo(alias="InvalidAction")]]


class OutputExitExit(TypedDict, total=False):
    llm_input: Required[ChatPromptParam]

    llm_output: Required[str]


class OutputExit(TypedDict, total=False):
    exit: Required[Annotated[OutputExitExit, PropertyInfo(alias="Exit")]]


Output: TypeAlias = Union[OutputSelectedStep, OutputSearchStep, OutputInvalidAction, OutputExit]
