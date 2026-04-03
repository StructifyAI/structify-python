# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from ..template_question_param import TemplateQuestionParam

__all__ = ["ChatTemplateUpdateParams"]


class ChatTemplateUpdateParams(TypedDict, total=False):
    description: Optional[str]

    display_order: Optional[int]

    image_url: Optional[str]

    is_active: Optional[bool]

    questions: Optional[Iterable[TemplateQuestionParam]]

    title: Optional[str]

    updated_by: Optional[str]
