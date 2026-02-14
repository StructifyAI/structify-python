# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .image import Image
from .source import Source
from .._models import BaseModel
from .chat_event import ChatEvent
from .chat_prompt import ChatPrompt
from .knowledge_graph import KnowledgeGraph
from .save_requirement import SaveRequirement
from .exploration_phase_id import ExplorationPhaseID

__all__ = [
    "JobGetResponse",
    "Agent",
    "Info",
    "InfoParameters",
    "InfoParametersStructuringInput",
    "InfoParametersStructuringInputAgent",
    "InfoParametersStructuringInputAgentAgent",
    "InfoParametersStructuringInputAgentAgentPdf",
    "InfoParametersStructuringInputAgentAgentPdfPdf",
    "InfoParametersStructuringInputAgentAgentWeb",
    "InfoParametersStructuringInputAgentAgentWebWeb",
    "InfoParametersStructuringInputTransformationPrompt",
    "InfoParametersStructuringInputScrapeFromURLProperty",
    "InfoParametersStructuringInputScrapeFromURLPropertyScrapeFromURLProperty",
    "InfoParametersStructuringInputScrapeURL",
    "InfoParametersStructuringInputScrapeURLScrapeURL",
    "InfoParametersStructuringInputConnectorExploration",
    "InfoParametersStructuringInputConnectorExplorationConnectorExploration",
    "Saved",
    "SavedProperties",
    "SavedPropertiesPartialDateObject",
    "SavedPropertiesURLObject",
    "SavedPropertiesMoneyObject",
    "SavedPropertiesPersonName",
    "SavedPropertiesAddressObject",
    "SavedLocation",
    "SavedLocationText",
    "SavedLocationTextText",
    "SavedLocationVisual",
    "SavedLocationVisualVisual",
    "SavedLocationPage",
    "SavedLocationPagePage",
]


class Agent(BaseModel):
    base_url: str

    is_newly_created: bool

    scraper_created_at: datetime

    scraper_id: str

    scraper_updated_at: datetime

    chat: Optional[ChatPrompt] = None

    code: Optional[str] = None

    events: Optional[List[ChatEvent]] = None

    next_page_code: Optional[str] = None


class InfoParametersStructuringInputAgentAgentPdfPdf(BaseModel):
    """Ingest all pages of a PDF and process them independently."""

    path: str

    page: Optional[int] = None


class InfoParametersStructuringInputAgentAgentPdf(BaseModel):
    pdf: InfoParametersStructuringInputAgentAgentPdfPdf = FieldInfo(alias="PDF")
    """Ingest all pages of a PDF and process them independently."""


class InfoParametersStructuringInputAgentAgentWebWeb(BaseModel):
    banned_domains: Optional[List[str]] = None

    starting_searches: Optional[List[str]] = None

    starting_urls: Optional[List[str]] = None


class InfoParametersStructuringInputAgentAgentWeb(BaseModel):
    web: InfoParametersStructuringInputAgentAgentWebWeb = FieldInfo(alias="Web")


InfoParametersStructuringInputAgentAgent: TypeAlias = Union[
    InfoParametersStructuringInputAgentAgentPdf, InfoParametersStructuringInputAgentAgentWeb
]


class InfoParametersStructuringInputAgent(BaseModel):
    agent: InfoParametersStructuringInputAgentAgent = FieldInfo(alias="Agent")


class InfoParametersStructuringInputTransformationPrompt(BaseModel):
    transformation_prompt: str = FieldInfo(alias="TransformationPrompt")


class InfoParametersStructuringInputScrapeFromURLPropertyScrapeFromURLProperty(BaseModel):
    batch_scrape: bool

    url_property_name: str

    use_markdown: bool


class InfoParametersStructuringInputScrapeFromURLProperty(BaseModel):
    scrape_from_url_property: InfoParametersStructuringInputScrapeFromURLPropertyScrapeFromURLProperty = FieldInfo(
        alias="ScrapeFromUrlProperty"
    )


class InfoParametersStructuringInputScrapeURLScrapeURL(BaseModel):
    batch_scrape: bool

    url: str

    use_markdown: bool


class InfoParametersStructuringInputScrapeURL(BaseModel):
    scrape_url: InfoParametersStructuringInputScrapeURLScrapeURL = FieldInfo(alias="ScrapeUrl")


class InfoParametersStructuringInputConnectorExplorationConnectorExploration(BaseModel):
    connector_id: str

    exploration_phase_id: ExplorationPhaseID
    """Identifies the phase of connector exploration

    This enum is used to track which phase of exploration a chat session belongs to.
    It's stored as JSONB in the database to allow for flexible phase identification.
    """

    exploration_run_id: str

    stage: Literal["both", "ingestion", "annotation"]
    """Which exploration stage to run"""


class InfoParametersStructuringInputConnectorExploration(BaseModel):
    connector_exploration: InfoParametersStructuringInputConnectorExplorationConnectorExploration = FieldInfo(
        alias="ConnectorExploration"
    )


InfoParametersStructuringInput: TypeAlias = Union[
    InfoParametersStructuringInputAgent,
    InfoParametersStructuringInputTransformationPrompt,
    InfoParametersStructuringInputScrapeFromURLProperty,
    InfoParametersStructuringInputScrapeURL,
    InfoParametersStructuringInputConnectorExploration,
]


class InfoParameters(BaseModel):
    allow_extra_entities: bool

    extraction_criteria: List[SaveRequirement]

    seeded_kg: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """

    structuring_input: InfoParametersStructuringInput

    instructions: Optional[str] = None

    model: Optional[str] = None


class Info(BaseModel):
    id: str

    created_at: datetime

    dataset_id: str

    job_type: Literal["Web", "Pdf", "Derive", "Scrape", "Match", "ConnectorExplore"]

    status: Literal["Queued", "Running", "Completed", "Failed"]

    user_id: str

    message: Optional[str] = None

    parameters: Optional[InfoParameters] = None

    reason: Optional[str] = None

    run_started_time: Optional[datetime] = None

    run_time_milliseconds: Optional[int] = None


class SavedPropertiesPartialDateObject(BaseModel):
    original_string: str

    year: int

    day: Optional[int] = None

    month: Optional[int] = None


class SavedPropertiesURLObject(BaseModel):
    original_string: str

    url: str


class SavedPropertiesMoneyObject(BaseModel):
    amount: float

    currency_code: Literal[
        "USD",
        "EUR",
        "GBP",
        "JPY",
        "CNY",
        "INR",
        "RUB",
        "CAD",
        "AUD",
        "CHF",
        "ILS",
        "NZD",
        "SGD",
        "HKD",
        "NOK",
        "SEK",
        "PLN",
        "TRY",
        "DKK",
        "MXN",
        "ZAR",
        "PHP",
        "VND",
        "THB",
        "BRL",
        "KRW",
    ]

    original_string: str


class SavedPropertiesPersonName(BaseModel):
    name: str


class SavedPropertiesAddressObject(BaseModel):
    components: Dict[str, str]

    original_address: str


SavedProperties: TypeAlias = Union[
    str,
    bool,
    float,
    SavedPropertiesPartialDateObject,
    str,
    str,
    SavedPropertiesURLObject,
    str,
    SavedPropertiesMoneyObject,
    Image,
    SavedPropertiesPersonName,
    SavedPropertiesAddressObject,
    str,
]


class SavedLocationTextText(BaseModel):
    byte_offset: int


class SavedLocationText(BaseModel):
    text: SavedLocationTextText = FieldInfo(alias="Text")


class SavedLocationVisualVisual(BaseModel):
    x: int

    y: int


class SavedLocationVisual(BaseModel):
    visual: SavedLocationVisualVisual = FieldInfo(alias="Visual")


class SavedLocationPagePage(BaseModel):
    page_number: int


class SavedLocationPage(BaseModel):
    page: SavedLocationPagePage = FieldInfo(alias="Page")


SavedLocation: TypeAlias = Union[SavedLocationText, SavedLocationVisual, SavedLocationPage, None]


class Saved(BaseModel):
    id: str

    created_at: datetime

    is_summary: bool

    label: str

    llm_id: int

    properties: Dict[str, SavedProperties]

    source_id: str

    user_specified: bool

    job_id: Optional[str] = None

    kg_entity_id: Optional[str] = None

    link: Optional[Source] = None

    location: Optional[SavedLocation] = None

    scraper_id: Optional[str] = None


class JobGetResponse(BaseModel):
    agents: List[Agent]

    info: Info

    saved: List[List[Saved]]
