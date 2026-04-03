# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CodeGenerateCodeParams", "Config"]


class CodeGenerateCodeParams(TypedDict, total=False):
    chat_session_id: Required[Annotated[str, PropertyInfo(alias="chatSessionId")]]

    prompt: Required[str]

    assistant_message_id: Annotated[Optional[str], PropertyInfo(alias="assistantMessageId")]

    config: Optional[Config]
    """Configuration for chat session with system prompt and LLM key"""

    connector_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="connectorIds")]

    file_paths: Annotated[SequenceNotStr[str], PropertyInfo(alias="filePaths")]

    override_previous_message_id: Annotated[Optional[str], PropertyInfo(alias="overridePreviousMessageId")]

    trigger_workflow_execution: Annotated[bool, PropertyInfo(alias="triggerWorkflowExecution")]

    user_message_id: Annotated[Optional[str], PropertyInfo(alias="userMessageId")]


class Config(TypedDict, total=False):
    """Configuration for chat session with system prompt and LLM key"""

    llm_key: Optional[
        Literal[
            "claude-sonnet-4-5",
            "claude-opus-4-5",
            "claude-opus-4-6",
            "claude-haiku-4-5",
            "gpt-5-mini",
            "gpt-5-nano",
            "gpt-5",
            "gemini-2.5-pro",
            "gemini-2.5-flash",
            "gemini-3-flash-preview",
            "gemini-3.1-flash-lite-preview",
            "test_llm.test",
        ]
    ]
    """LLM model keys available in the system."""

    max_steps: Optional[int]

    reminder_message: Optional[str]

    system_prompt: Optional[str]
