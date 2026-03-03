# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolMetadata"]


class ToolMetadata(BaseModel):
    description: str

    name: Literal[
        "WebSearch",
        "WebNavigate",
        "ViewPage",
        "Save",
        "SaveEntities",
        "Exit",
        "ApiExecute",
        "Javascript",
        "NavigateToIFrame",
        "InfiniteScroll",
        "InspectStep",
        "ReadNodeLogs",
        "DeleteFile",
        "MoveFile",
        "ApplyPatch",
        "RunBash",
        "RunPython",
        "IssueFound",
        "SaveDatabase",
        "SaveSchema",
        "SaveTable",
        "SaveColumn",
        "SaveApiResource",
        "SaveMemory",
        "SearchConnectorTables",
        "RequestClarification",
        "AddDependency",
        "SelectData",
        "CreateConnector",
        "SearchConnectorTypes",
        "PinPreviousTool",
    ]

    regex_validator: str
