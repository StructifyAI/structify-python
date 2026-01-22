# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ToolResult",
    "Error",
    "Text",
    "CodeExecution",
    "CodeExecutionCodeExecution",
    "WebMarkdown",
    "WebSearch",
    "WebSearchWebSearch",
    "ConnectorSearch",
    "ConnectorSearchConnectorSearch",
    "ConnectorSearchConnectorSearchColumn",
    "NodeLogs",
    "Image",
    "ImageImage",
]


class Error(BaseModel):
    error: str = FieldInfo(alias="Error")


class Text(BaseModel):
    text: str = FieldInfo(alias="Text")


class CodeExecutionCodeExecution(BaseModel):
    return_code: int

    stderr: str

    stdout: str


class CodeExecution(BaseModel):
    code_execution: CodeExecutionCodeExecution = FieldInfo(alias="CodeExecution")


class WebMarkdown(BaseModel):
    web_markdown: str = FieldInfo(alias="WebMarkdown")


class WebSearchWebSearch(BaseModel):
    snippet: str

    title: str

    url: str


class WebSearch(BaseModel):
    web_search: List[WebSearchWebSearch] = FieldInfo(alias="WebSearch")


class ConnectorSearchConnectorSearchColumn(BaseModel):
    name: str

    type: str

    notes: Optional[str] = None


class ConnectorSearchConnectorSearch(BaseModel):
    columns: List[ConnectorSearchConnectorSearchColumn]

    database: str

    schema_: str = FieldInfo(alias="schema")

    table_name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class ConnectorSearch(BaseModel):
    connector_search: List[ConnectorSearchConnectorSearch] = FieldInfo(alias="ConnectorSearch")


class NodeLogs(BaseModel):
    node_logs: List[str] = FieldInfo(alias="NodeLogs")


class ImageImage(BaseModel):
    image_bytes: object

    ocr_text: Optional[str] = None


class Image(BaseModel):
    image: ImageImage = FieldInfo(alias="Image")


ToolResult: TypeAlias = Union[
    Literal["Pending", "NoResult", "Completed"],
    Error,
    Text,
    CodeExecution,
    WebMarkdown,
    WebSearch,
    ConnectorSearch,
    NodeLogs,
    Image,
]
