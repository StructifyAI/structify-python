# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "NextActionLabelTrainingDatumParams",
    "Output",
    "OutputSelectedStep",
    "OutputSelectedStepSelectedStep",
    "OutputSearchStep",
    "OutputSearchStepSearchStep",
    "OutputInvalidAction",
    "OutputInvalidActionInvalidAction",
]


class NextActionLabelTrainingDatumParams(TypedDict, total=False):
    id: Required[str]

    label: Required[str]

    output: Required[Output]


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
