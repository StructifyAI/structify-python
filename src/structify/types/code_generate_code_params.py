# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CodeGenerateCodeParams", "FileContent"]


class CodeGenerateCodeParams(TypedDict, total=False):
    chat_session_id: Required[Annotated[str, PropertyInfo(alias="chatSessionId")]]

    prompt: Required[str]

    file_contents: Annotated[Iterable[FileContent], PropertyInfo(alias="fileContents")]


class FileContent(TypedDict, total=False):
    content: Required[str]

    path: Required[str]
