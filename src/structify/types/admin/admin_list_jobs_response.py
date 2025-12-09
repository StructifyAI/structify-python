# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..knowledge_graph import KnowledgeGraph
from ..save_requirement import SaveRequirement
from ..exploration_phase_id import ExplorationPhaseID

__all__ = [
    "AdminListJobsResponse",
    "Parameters",
    "ParametersStructuringInput",
    "ParametersStructuringInputAgent",
    "ParametersStructuringInputAgentAgent",
    "ParametersStructuringInputAgentAgentPdf",
    "ParametersStructuringInputAgentAgentPdfPdf",
    "ParametersStructuringInputAgentAgentWeb",
    "ParametersStructuringInputAgentAgentWebWeb",
    "ParametersStructuringInputTransformationPrompt",
    "ParametersStructuringInputScrapeFromURLProperty",
    "ParametersStructuringInputScrapeFromURLPropertyScrapeFromURLProperty",
    "ParametersStructuringInputScrapeURL",
    "ParametersStructuringInputScrapeURLScrapeURL",
    "ParametersStructuringInputConnectorExploration",
    "ParametersStructuringInputConnectorExplorationConnectorExploration",
]


class ParametersStructuringInputAgentAgentPdfPdf(BaseModel):
    """Ingest all pages of a PDF and process them independently."""

    path: str


class ParametersStructuringInputAgentAgentPdf(BaseModel):
    pdf: ParametersStructuringInputAgentAgentPdfPdf = FieldInfo(alias="PDF")
    """Ingest all pages of a PDF and process them independently."""


class ParametersStructuringInputAgentAgentWebWeb(BaseModel):
    banned_domains: Optional[List[str]] = None

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


class ParametersStructuringInputScrapeFromURLPropertyScrapeFromURLProperty(BaseModel):
    batch_scrape: bool

    url_property_name: str

    use_markdown: bool


class ParametersStructuringInputScrapeFromURLProperty(BaseModel):
    scrape_from_url_property: ParametersStructuringInputScrapeFromURLPropertyScrapeFromURLProperty = FieldInfo(
        alias="ScrapeFromUrlProperty"
    )


class ParametersStructuringInputScrapeURLScrapeURL(BaseModel):
    batch_scrape: bool

    url: str

    use_markdown: bool


class ParametersStructuringInputScrapeURL(BaseModel):
    scrape_url: ParametersStructuringInputScrapeURLScrapeURL = FieldInfo(alias="ScrapeUrl")


class ParametersStructuringInputConnectorExplorationConnectorExploration(BaseModel):
    connector_id: str

    exploration_phase_id: ExplorationPhaseID
    """Identifies the phase of connector exploration

    This enum is used to track which phase of exploration a chat session belongs to.
    It's stored as JSONB in the database to allow for flexible phase identification.
    """

    exploration_run_id: str

    stage: Literal["both", "ingestion", "annotation"]
    """Which exploration stage to run"""


class ParametersStructuringInputConnectorExploration(BaseModel):
    connector_exploration: ParametersStructuringInputConnectorExplorationConnectorExploration = FieldInfo(
        alias="ConnectorExploration"
    )


ParametersStructuringInput: TypeAlias = Union[
    ParametersStructuringInputAgent,
    ParametersStructuringInputTransformationPrompt,
    ParametersStructuringInputScrapeFromURLProperty,
    ParametersStructuringInputScrapeURL,
    ParametersStructuringInputConnectorExploration,
]


class Parameters(BaseModel):
    allow_extra_entities: bool

    extraction_criteria: List[SaveRequirement]

    seeded_kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """

    structuring_input: ParametersStructuringInput


class AdminListJobsResponse(BaseModel):
    id: str

    dataset_id: str

    job_type: Literal["Web", "Pdf", "Derive", "Scrape", "Match", "ConnectorExplore"]

    status: Literal["Queued", "Running", "Completed", "Failed"]

    user_id: str

    parameters: Optional[Parameters] = None
