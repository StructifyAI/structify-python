# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..template_question_param import TemplateQuestionParam

__all__ = ["ChatTemplateCreateParams"]


class ChatTemplateCreateParams(TypedDict, total=False):
    chat_session_id: Required[str]

    description: Required[str]

    display_order: Required[int]

    image_url: Required[str]

    is_active: Required[bool]

    questions: Required[Iterable[TemplateQuestionParam]]

    title: Required[str]
