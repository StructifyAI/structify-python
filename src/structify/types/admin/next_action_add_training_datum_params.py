# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .next_action_input_param import NextActionInputParam

__all__ = [
    "NextActionAddTrainingDatumParams",
    "Output",
    "OutputSelectedStep",
    "OutputSelectedStepSelectedStep",
    "OutputSearchStep",
    "OutputSearchStepSearchStep",
    "OutputInvalidAction",
    "OutputInvalidActionInvalidAction",
]


class NextActionAddTrainingDatumParams(TypedDict, total=False):
    input: Required[NextActionInputParam]

    label: Required[str]

    output: Required[Output]

    job_id: Optional[str]


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
