# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .next_action_input import NextActionInput

__all__ = [
    "ActionTrainingDataEntry",
    "Output",
    "OutputOutput",
    "OutputOutputSelectedStep",
    "OutputOutputSelectedStepSelectedStep",
    "OutputOutputSearchStep",
    "OutputOutputSearchStepSearchStep",
    "OutputOutputInvalidAction",
    "OutputOutputInvalidActionInvalidAction",
]


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

    input: NextActionInput

    outputs: List[Output]
