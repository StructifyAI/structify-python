# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolMetadataParam"]


class ToolMetadataParam(TypedDict, total=False):
    description: Required[str]

    name: Required[
        Literal[
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
    ]

    regex_validator: Required[str]
