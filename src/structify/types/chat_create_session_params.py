# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCreateSessionParams", "Config"]


class ChatCreateSessionParams(TypedDict, total=False):
    team_id: Required[str]

    config: Optional[Config]
    """Configuration for chat session with system prompt and LLM key"""

    ephemeral: Optional[bool]

    project_id: Optional[str]


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
