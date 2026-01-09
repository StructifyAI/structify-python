# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ToolInvocation",
    "WebSearch",
    "WebSearchInput",
    "WebNavigate",
    "WebNavigateInput",
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
]


class WebSearchInput(BaseModel):
    query: str


class WebSearch(BaseModel):
    input: WebSearchInput

    name: Literal["WebSearch"]


class WebNavigateInput(BaseModel):
    url: str


class WebNavigate(BaseModel):
    input: WebNavigateInput

    name: Literal["WebNavigate"]


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


ToolInvocation: TypeAlias = Annotated[
    Union[
        WebSearch,
        WebNavigate,
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
    ],
    PropertyInfo(discriminator="name"),
]
