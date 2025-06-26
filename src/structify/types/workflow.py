# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Workflow",
    "Step",
    "StepOperation",
    "StepOperationEnhanceProperties",
    "StepOperationEnhanceRelationship",
    "StepOperationDeriveProperty",
    "StepOperationScrapePage",
    "StepOperationScrapePageScrapePage",
    "DefaultStopConditions",
]


class StepOperationEnhanceProperties(BaseModel):
    enhance_properties: List[str] = FieldInfo(alias="EnhanceProperties")


class StepOperationEnhanceRelationship(BaseModel):
    enhance_relationship: str = FieldInfo(alias="EnhanceRelationship")


class StepOperationDeriveProperty(BaseModel):
    derive_property: List[str] = FieldInfo(alias="DeriveProperty")


class StepOperationScrapePageScrapePage(BaseModel):
    relationship_name: str

    starting_url_property_name: str


class StepOperationScrapePage(BaseModel):
    scrape_page: StepOperationScrapePageScrapePage = FieldInfo(alias="ScrapePage")


StepOperation: TypeAlias = Union[
    StepOperationEnhanceProperties,
    StepOperationEnhanceRelationship,
    StepOperationDeriveProperty,
    StepOperationScrapePage,
    Literal["IngestData"],
]


class Step(BaseModel):
    id: str

    children: List[str]

    operation: StepOperation

    table_name: str


class DefaultStopConditions(BaseModel):
    max_steps_without_save: int

    max_errors: Optional[int] = None

    max_execution_time_secs: Optional[int] = None

    max_total_steps: Optional[int] = None


class Workflow(BaseModel):
    name: str

    starting_step: str

    starting_table: str

    steps: List[Step]

    default_banned_domains: Optional[List[str]] = None

    default_stop_conditions: Optional[DefaultStopConditions] = None
    """Configuration parameters for the StopChecker"""
