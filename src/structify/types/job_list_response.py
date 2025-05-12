# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .id import ID
from .._models import BaseModel
from .knowledge_graph import KnowledgeGraph
from .save_requirement import SaveRequirement

__all__ = [
    "JobListResponse",
    "Parameters",
    "ParametersStructuringInput",
    "ParametersStructuringInputAgent",
    "ParametersStructuringInputAgentAgent",
    "ParametersStructuringInputAgentAgentPdf",
    "ParametersStructuringInputAgentAgentPdfPdf",
    "ParametersStructuringInputAgentAgentWeb",
    "ParametersStructuringInputAgentAgentWebWeb",
    "ParametersStructuringInputTransformationPrompt",
    "ParametersStructuringInputScrapePage",
]


class ParametersStructuringInputAgentAgentPdfPdf(BaseModel):
    path: str


class ParametersStructuringInputAgentAgentPdf(BaseModel):
    pdf: ParametersStructuringInputAgentAgentPdfPdf = FieldInfo(alias="PDF")
    """Ingest all pages of a PDF and process them independently."""


class ParametersStructuringInputAgentAgentWebWeb(BaseModel):
    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None


class ParametersStructuringInputAgentAgentWeb(BaseModel):
    web: ParametersStructuringInputAgentAgentWebWeb = FieldInfo(alias="Web")


ParametersStructuringInputAgentAgent: TypeAlias = Union[
    ParametersStructuringInputAgentAgentPdf, ParametersStructuringInputAgentAgentWeb
]


class ParametersStructuringInputAgent(BaseModel):
    agent: ParametersStructuringInputAgentAgent = FieldInfo(alias="Agent")
    """These are all the types that can be converted into a BasicInputType"""


class ParametersStructuringInputTransformationPrompt(BaseModel):
    transformation_prompt: str = FieldInfo(alias="TransformationPrompt")


class ParametersStructuringInputScrapePage(BaseModel):
    scrape_page: str = FieldInfo(alias="ScrapePage")


ParametersStructuringInput: TypeAlias = Union[
    ParametersStructuringInputAgent,
    ParametersStructuringInputTransformationPrompt,
    ParametersStructuringInputScrapePage,
]


class Parameters(BaseModel):
    allow_extra_entities: bool

    extraction_criteria: List[SaveRequirement]

    seeded_kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    structuring_input: ParametersStructuringInput


class JobListResponse(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    job_type: Literal["Web", "Pdf", "Derive", "Scrape"]

    selected_next_workflow_step: bool

    status: Literal["Queued", "Running", "Completed", "Failed"]

    user_id: str

    parameters: Optional[Parameters] = None

    reason: Optional[str] = None

    run_started_time: Optional[datetime] = None

    run_time_milliseconds: Optional[int] = None

    special_job_type: Optional[Literal["HumanLLM"]] = None

    workflow_group_id: Optional[str] = None

    workflow_id: Optional[ID] = None

    workflow_step_id: Optional[str] = None
