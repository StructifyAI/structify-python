# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..chat_prompt_param import ChatPromptParam

__all__ = [
    "NextActionLabelTrainingDatumParams",
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


class NextActionLabelTrainingDatumParams(TypedDict, total=False):
    id: Required[str]

    label: Required[str]

    output: Required[Output]


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
