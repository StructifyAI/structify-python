# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "WorkflowParam",
    "DefaultStopConditions",
    "Step",
    "StepOperation",
    "StepOperationEnhanceProperties",
    "StepOperationEnhanceRelationship",
    "StepOperationDeriveProperty",
    "StepOperationScrapePage",
    "StepOperationScrapePageScrapePage",
]


class DefaultStopConditions(TypedDict, total=False):
    max_steps_without_save: Required[int]

    max_errors: Optional[int]

    max_execution_time_secs: Optional[int]

    max_total_steps: Optional[int]


class StepOperationEnhanceProperties(TypedDict, total=False):
    enhance_properties: Required[Annotated[List[str], PropertyInfo(alias="EnhanceProperties")]]


class StepOperationEnhanceRelationship(TypedDict, total=False):
    enhance_relationship: Required[Annotated[str, PropertyInfo(alias="EnhanceRelationship")]]


class StepOperationDeriveProperty(TypedDict, total=False):
    derive_property: Required[Annotated[List[str], PropertyInfo(alias="DeriveProperty")]]


class StepOperationScrapePageScrapePage(TypedDict, total=False):
    relationship_name: Required[str]

    starting_url_property_name: Required[str]


class StepOperationScrapePage(TypedDict, total=False):
    scrape_page: Required[Annotated[StepOperationScrapePageScrapePage, PropertyInfo(alias="ScrapePage")]]


StepOperation: TypeAlias = Union[
    StepOperationEnhanceProperties,
    StepOperationEnhanceRelationship,
    StepOperationDeriveProperty,
    StepOperationScrapePage,
    Literal["IngestData"],
]


class Step(TypedDict, total=False):
    id: Required[str]

    children: Required[List[str]]

    operation: Required[StepOperation]

    table_name: Required[str]


class WorkflowParam(TypedDict, total=False):
    default_stop_conditions: Required[DefaultStopConditions]
    """Configuration parameters for the StopChecker"""

    name: Required[str]

    starting_step: Required[str]

    starting_table: Required[str]

    steps: Required[Iterable[Step]]
