# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["FunctionalTestLinkChatParams"]


class FunctionalTestLinkChatParams(TypedDict, total=False):
    chat_session_id: Required[str]

    functional_test_id: Required[str]

    results: Required[Dict[str, object]]

    sample_name: Required[str]
