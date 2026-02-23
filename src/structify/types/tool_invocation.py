# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .knowledge_graph import KnowledgeGraph

__all__ = [
    "ToolInvocation",
    "WebSearch",
    "WebSearchInput",
    "WebNavigate",
    "WebNavigateInput",
    "ViewPage",
    "ViewPageInput",
    "Save",
    "SaveInput",
    "SaveEntities",
    "SaveEntitiesInput",
    "Exit",
    "ExitInput",
    "APIExecute",
    "APIExecuteInput",
    "Javascript",
    "JavascriptInput",
    "NavigateToIFrame",
    "NavigateToIFrameInput",
    "InfiniteScroll",
    "InspectStep",
    "InspectStepInput",
    "ReadNodeLogs",
    "ReadNodeLogsInput",
    "DeleteFile",
    "DeleteFileInput",
    "MoveFile",
    "MoveFileInput",
    "RunBash",
    "RunBashInput",
    "RunPython",
    "RunPythonInput",
    "IssueFound",
    "IssueFoundInput",
    "SaveDatabase",
    "SaveDatabaseInput",
    "SaveSchema",
    "SaveSchemaInput",
    "SaveTable",
    "SaveTableInput",
    "SaveColumn",
    "SaveColumnInput",
    "SaveAPIResource",
    "SaveAPIResourceInput",
    "SaveMemory",
    "SaveMemoryInput",
    "SearchConnectorTables",
    "SearchConnectorTablesInput",
    "RequestClarification",
    "RequestClarificationInput",
    "AddDependency",
    "AddDependencyInput",
    "SelectData",
    "SelectDataInput",
    "CreateConnector",
    "CreateConnectorInput",
    "SearchConnectorTypes",
    "SearchConnectorTypesInput",
    "PinPreviousTool",
    "PinPreviousToolInput",
]


class WebSearchInput(BaseModel):
    query: str


class WebSearch(BaseModel):
    input: WebSearchInput

    name: Literal["WebSearch"]


class WebNavigateInput(BaseModel):
    url: str

    output_format: Optional[Literal["Text", "Visual"]] = None


class WebNavigate(BaseModel):
    input: WebNavigateInput

    name: Literal["WebNavigate"]


class ViewPageInput(BaseModel):
    page_number: int


class ViewPage(BaseModel):
    input: ViewPageInput

    name: Literal["ViewPage"]


class SaveInput(BaseModel):
    knowledge_graph: KnowledgeGraph
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a DB
    """

    reason: str

    sources: List[str]


class Save(BaseModel):
    input: SaveInput

    name: Literal["Save"]


class SaveEntitiesInput(BaseModel):
    entities: List[Dict[str, Dict[str, object]]]

    reason: str

    sources: List[str]


class SaveEntities(BaseModel):
    input: SaveEntitiesInput

    name: Literal["SaveEntities"]


class ExitInput(BaseModel):
    reason: str


class Exit(BaseModel):
    input: ExitInput

    name: Literal["Exit"]


class APIExecuteInput(BaseModel):
    code: str


class APIExecute(BaseModel):
    input: APIExecuteInput

    name: Literal["ApiExecute"]


class JavascriptInput(BaseModel):
    code: str


class Javascript(BaseModel):
    input: JavascriptInput

    name: Literal["Javascript"]


class NavigateToIFrameInput(BaseModel):
    index: int


class NavigateToIFrame(BaseModel):
    input: NavigateToIFrameInput

    name: Literal["NavigateToIFrame"]


class InfiniteScroll(BaseModel):
    input: object

    name: Literal["InfiniteScroll"]


class InspectStepInput(BaseModel):
    step_name: str


class InspectStep(BaseModel):
    input: InspectStepInput

    name: Literal["InspectStep"]


class ReadNodeLogsInput(BaseModel):
    end_line: int

    node_function_name: str

    start_line: int

    log_type: Optional[str] = None


class ReadNodeLogs(BaseModel):
    input: ReadNodeLogsInput

    name: Literal["ReadNodeLogs"]


class DeleteFileInput(BaseModel):
    file: str


class DeleteFile(BaseModel):
    input: DeleteFileInput

    name: Literal["DeleteFile"]


class MoveFileInput(BaseModel):
    file: str

    new_path: str


class MoveFile(BaseModel):
    input: MoveFileInput

    name: Literal["MoveFile"]


class RunBashInput(BaseModel):
    command: str

    connector: Optional[str] = None

    working_dir: Optional[str] = None


class RunBash(BaseModel):
    input: RunBashInput

    name: Literal["RunBash"]


class RunPythonInput(BaseModel):
    code: str

    connector: Optional[str] = None

    timeout_seconds: Optional[int] = None

    working_dir: Optional[str] = None


class RunPython(BaseModel):
    input: RunPythonInput

    name: Literal["RunPython"]


class IssueFoundInput(BaseModel):
    admin_override: bool

    description: str

    title: str


class IssueFound(BaseModel):
    input: IssueFoundInput

    name: Literal["IssueFound"]


class SaveDatabaseInput(BaseModel):
    name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class SaveDatabase(BaseModel):
    input: SaveDatabaseInput

    name: Literal["SaveDatabase"]


class SaveSchemaInput(BaseModel):
    name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class SaveSchema(BaseModel):
    input: SaveSchemaInput

    name: Literal["SaveSchema"]


class SaveTableInput(BaseModel):
    name: str

    description: Optional[str] = None

    notes: Optional[str] = None

    tag: Optional[str] = None


class SaveTable(BaseModel):
    input: SaveTableInput

    name: Literal["SaveTable"]


class SaveColumnInput(BaseModel):
    column_name: str

    column_type: str

    notes: Optional[str] = None


class SaveColumn(BaseModel):
    input: SaveColumnInput

    name: Literal["SaveColumn"]


class SaveAPIResourceInput(BaseModel):
    endpoint: str

    name: str

    description: Optional[str] = None

    notes: Optional[str] = None


class SaveAPIResource(BaseModel):
    input: SaveAPIResourceInput

    name: Literal["SaveApiResource"]


class SaveMemoryInput(BaseModel):
    key: str

    value: str


class SaveMemory(BaseModel):
    input: SaveMemoryInput

    name: Literal["SaveMemory"]


class SearchConnectorTablesInput(BaseModel):
    query: str

    wiki_tag: Optional[str] = None


class SearchConnectorTables(BaseModel):
    input: SearchConnectorTablesInput

    name: Literal["SearchConnectorTables"]


class RequestClarificationInput(BaseModel):
    question: str

    table_name: str

    column_name: Optional[str] = None


class RequestClarification(BaseModel):
    input: RequestClarificationInput

    name: Literal["RequestClarification"]


class AddDependencyInput(BaseModel):
    package_name: str

    version_spec: Optional[str] = None


class AddDependency(BaseModel):
    input: AddDependencyInput

    name: Literal["AddDependency"]


class SelectDataInput(BaseModel):
    node_ids: List[str]


class SelectData(BaseModel):
    input: SelectDataInput

    name: Literal["SelectData"]


class CreateConnectorInput(BaseModel):
    connector_type: str

    name: str

    description: Optional[str] = None

    secrets: Optional[List[str]] = None


class CreateConnector(BaseModel):
    input: CreateConnectorInput

    name: Literal["CreateConnector"]


class SearchConnectorTypesInput(BaseModel):
    query: Optional[str] = None


class SearchConnectorTypes(BaseModel):
    input: SearchConnectorTypesInput

    name: Literal["SearchConnectorTypes"]


class PinPreviousToolInput(BaseModel):
    path: str


class PinPreviousTool(BaseModel):
    input: PinPreviousToolInput

    name: Literal["PinPreviousTool"]


ToolInvocation: TypeAlias = Annotated[
    Union[
        WebSearch,
        WebNavigate,
        ViewPage,
        Save,
        SaveEntities,
        Exit,
        APIExecute,
        Javascript,
        NavigateToIFrame,
        InfiniteScroll,
        InspectStep,
        ReadNodeLogs,
        DeleteFile,
        MoveFile,
        RunBash,
        RunPython,
        IssueFound,
        SaveDatabase,
        SaveSchema,
        SaveTable,
        SaveColumn,
        SaveAPIResource,
        SaveMemory,
        SearchConnectorTables,
        RequestClarification,
        AddDependency,
        SelectData,
        CreateConnector,
        SearchConnectorTypes,
        PinPreviousTool,
    ],
    PropertyInfo(discriminator="name"),
]
