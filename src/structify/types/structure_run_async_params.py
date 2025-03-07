# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .pdf_param import PdfParam
from .web_param import WebParam
from .knowledge_graph_param import KnowledgeGraphParam
from .save_requirement_param import SaveRequirementParam

__all__ = ["StructureRunAsyncParams", "Source"]


class StructureRunAsyncParams(TypedDict, total=False):
    dataset: Required[str]

    source: Required[Source]
    """These are all the types that can be converted into a BasicInputType"""

    save_requirement: Iterable[SaveRequirementParam]

    seeded_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    special_job_type: Optional[Literal["HumanLLM"]]


Source: TypeAlias = Union[PdfParam, WebParam]
