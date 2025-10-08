# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CodeGenerateCodeParams", "Config"]


class CodeGenerateCodeParams(TypedDict, total=False):
    chat_session_id: Required[Annotated[str, PropertyInfo(alias="chatSessionId")]]

    prompt: Required[str]

    assistant_message_id: Annotated[Optional[str], PropertyInfo(alias="assistantMessageId")]

    config: Optional[Config]
    """Configuration for chat session with system prompt and LLM key"""

    trigger_workflow_execution: Annotated[bool, PropertyInfo(alias="triggerWorkflowExecution")]

    user_message_id: Annotated[Optional[str], PropertyInfo(alias="userMessageId")]


class Config(TypedDict, total=False):
    llm_key: Required[
        Literal[
            "vllm.gpt-5-mini-2025-08-07",
            "vllm.gpt-4.1-mini-2025-04-14",
            "vllm.gpt-5-nano-2025-08-07",
            "vllm.gpt-5-2025-08-07",
            "vllm.ft:gpt-4o-2024-08-06:structify::ADrF00Gq",
            "vllm.ft:gpt-4o-mini-2024-07-18:structify::ABCLHTsN",
            "vllm.action",
            "vllm.dora",
            "vllm.boring_dora",
            "vllm.claude-3-7-sonnet-20250219",
            "vllm.claude-sonnet-4-20250514",
            "vllm.qwen-3-coder-480b",
            "test_llm.test",
            "bedrock.claude-sonnet-4-bedrock",
            "bedrock.claude-sonnet-4-5-bedrock",
            "gemini.gemini-2.5-pro",
        ]
    ]
    """LLM model keys available in the system. Format: <provider>.<model-name>"""

    system_prompt: Optional[str]
