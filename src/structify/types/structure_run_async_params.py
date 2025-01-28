# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .entity_param import EntityParam
from .property_type_param import PropertyTypeParam
from .knowledge_graph_param import KnowledgeGraphParam
from .extraction_criteria_param import ExtractionCriteriaParam

__all__ = [
    "StructureRunAsyncParams",
    "StructureInput",
    "StructureInputSecIngestor",
    "StructureInputSecIngestorSecIngestor",
    "StructureInputPdfIngestor",
    "StructureInputPdfIngestorPdfIngestor",
    "StructureInputEnhanceIngestor",
    "StructureInputEnhanceIngestorEnhanceIngestor",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptor",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorProperty",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyProperty",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategy",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategyProbabilistic",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategyProbabilisticProbabilistic",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationship",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationship",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipMergeStrategy",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipMergeStrategyProbabilistic",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipProperty",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategy",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategyProbabilistic",
    "StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategyProbabilisticProbabilistic",
    "StructureInputBasic",
    "StructureInputBasicBasic",
    "StructureInputBasicBasicTextDocument",
    "StructureInputBasicBasicTextDocumentTextDocument",
    "StructureInputBasicBasicWebSearch",
    "StructureInputBasicBasicWebSearchWebSearch",
    "StructureInputBasicBasicImageDocument",
    "StructureInputBasicBasicImageDocumentImageDocument",
]


class StructureRunAsyncParams(TypedDict, total=False):
    name: Required[str]

    structure_input: Required[StructureInput]
    """These are all the types that can be converted into a BasicInputType"""

    extraction_criteria: Iterable[ExtractionCriteriaParam]

    seeded_entity: KnowledgeGraphParam
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    special_job_type: Optional[Literal["HumanLLM"]]


class StructureInputSecIngestorSecIngestor(TypedDict, total=False):
    accession_number: Optional[str]

    quarter: Optional[int]

    year: Optional[int]


class StructureInputSecIngestor(TypedDict, total=False):
    sec_ingestor: Required[Annotated[StructureInputSecIngestorSecIngestor, PropertyInfo(alias="SECIngestor")]]


class StructureInputPdfIngestorPdfIngestor(TypedDict, total=False):
    path: Required[str]


class StructureInputPdfIngestor(TypedDict, total=False):
    pdf_ingestor: Required[Annotated[StructureInputPdfIngestorPdfIngestor, PropertyInfo(alias="PDFIngestor")]]
    """This is currently a very simple ingestor.

    It converts everything to an image and processes them independently.
    """


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategyProbabilisticProbabilistic(
    TypedDict, total=False
):
    baseline_cardinality: Required[int]
    """
    The number of unique values that are expected to be present in the complete
    dataset

    This is used for merging to determine how significant a match is. (i.e. if there
    are only 2 possible values, a match gives less confidence than if there are 100)
    """

    match_transfer_probability: Required[float]
    """The estimated probability that, given an entity match, the properties also match

    For a person's full name, this would be quite high. For a person's job title, it
    would be lower because people can have multiple job titles over time or at
    different companies at the same time.
    """

    comparison_strategy: Literal["Default", "EnforceUniqueness"]


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategyProbabilistic(
    TypedDict, total=False
):
    probabilistic: Required[
        Annotated[
            StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategyProbabilisticProbabilistic,
            PropertyInfo(alias="Probabilistic"),
        ]
    ]


StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategy: TypeAlias = Union[
    Literal["Unique", "NoSignal"],
    StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategyProbabilistic,
]


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyProperty(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    merge_strategy: StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyPropertyMergeStrategy

    prop_type: PropertyTypeParam


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorProperty(TypedDict, total=False):
    property: Required[
        Annotated[
            StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorPropertyProperty, PropertyInfo(alias="Property")
        ]
    ]


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipMergeStrategyProbabilistic(
    TypedDict, total=False
):
    source_cardinality_given_target_match: Optional[int]
    """
    Describes the expected cardinality of the source table when a match is found in
    the target table

    For example, if we have a source company and a target funding round, we expect
    the source company to appear in multiple funding rounds, but not _too_ many. So
    if we have a funding round match, the expected number of unique companies is
    relatively small. This is an estimate of that number.
    """

    target_cardinality_given_source_match: Optional[int]
    """
    Describes the expected cardinality of the target table when a match is found in
    the source table

    For example, if we have a source company and a target funding round, we usually
    expect some number of funding rounds to be associated with a single company but
    not _too_ many. So if we have a company match, the expected number of unique
    funding rounds is relatively small. This is an estimate of that number.
    """


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipMergeStrategy(
    TypedDict, total=False
):
    probabilistic: Required[
        Annotated[
            StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipMergeStrategyProbabilistic,
            PropertyInfo(alias="Probabilistic"),
        ]
    ]


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategyProbabilisticProbabilistic(
    TypedDict, total=False
):
    baseline_cardinality: Required[int]
    """
    The number of unique values that are expected to be present in the complete
    dataset

    This is used for merging to determine how significant a match is. (i.e. if there
    are only 2 possible values, a match gives less confidence than if there are 100)
    """

    match_transfer_probability: Required[float]
    """The estimated probability that, given an entity match, the properties also match

    For a person's full name, this would be quite high. For a person's job title, it
    would be lower because people can have multiple job titles over time or at
    different companies at the same time.
    """

    comparison_strategy: Literal["Default", "EnforceUniqueness"]


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategyProbabilistic(
    TypedDict, total=False
):
    probabilistic: Required[
        Annotated[
            StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategyProbabilisticProbabilistic,
            PropertyInfo(alias="Probabilistic"),
        ]
    ]


StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategy: TypeAlias = Union[
    Literal["Unique", "NoSignal"],
    StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategyProbabilistic,
]


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipProperty(
    TypedDict, total=False
):
    description: Required[str]

    name: Required[str]

    merge_strategy: (
        StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipPropertyMergeStrategy
    )

    prop_type: PropertyTypeParam


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationship(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    source_table: Required[str]

    target_table: Required[str]

    merge_strategy: Optional[
        StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipMergeStrategy
    ]

    properties: Iterable[StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationshipProperty]


class StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationship(TypedDict, total=False):
    relationship: Required[
        Annotated[
            StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationshipRelationship,
            PropertyInfo(alias="Relationship"),
        ]
    ]


StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptor: TypeAlias = Union[
    StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorProperty,
    StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptorRelationship,
]


class StructureInputEnhanceIngestorEnhanceIngestor(TypedDict, total=False):
    central_entity: Required[EntityParam]

    surrounding_kg: Required[KnowledgeGraphParam]
    """
    Knowledge graph info structured to deserialize and display in the same format
    that the LLM outputs. Also the first representation of an LLM output in the
    pipeline from raw tool output to being merged into a Neo4j DB
    """

    target_descriptor: Required[StructureInputEnhanceIngestorEnhanceIngestorTargetDescriptor]

    allow_new_entities: bool


class StructureInputEnhanceIngestor(TypedDict, total=False):
    enhance_ingestor: Required[
        Annotated[StructureInputEnhanceIngestorEnhanceIngestor, PropertyInfo(alias="EnhanceIngestor")]
    ]


class StructureInputBasicBasicTextDocumentTextDocument(TypedDict, total=False):
    content: Optional[str]

    path: Optional[str]


class StructureInputBasicBasicTextDocument(TypedDict, total=False):
    text_document: Required[
        Annotated[StructureInputBasicBasicTextDocumentTextDocument, PropertyInfo(alias="TextDocument")]
    ]


class StructureInputBasicBasicWebSearchWebSearch(TypedDict, total=False):
    description: Optional[str]

    starting_website: str

    title: Optional[str]


class StructureInputBasicBasicWebSearch(TypedDict, total=False):
    web_search: Required[Annotated[StructureInputBasicBasicWebSearchWebSearch, PropertyInfo(alias="WebSearch")]]


class StructureInputBasicBasicImageDocumentImageDocument(TypedDict, total=False):
    document_name: Required[str]

    document_page: Required[int]


class StructureInputBasicBasicImageDocument(TypedDict, total=False):
    image_document: Required[
        Annotated[StructureInputBasicBasicImageDocumentImageDocument, PropertyInfo(alias="ImageDocument")]
    ]


StructureInputBasicBasic: TypeAlias = Union[
    StructureInputBasicBasicTextDocument, StructureInputBasicBasicWebSearch, StructureInputBasicBasicImageDocument
]


class StructureInputBasic(TypedDict, total=False):
    basic: Required[Annotated[StructureInputBasicBasic, PropertyInfo(alias="Basic")]]
    """
    These are all the types for which we have an agent that is directly capable of
    navigating. There should be a one to one mapping between them.
    """


StructureInput: TypeAlias = Union[
    StructureInputSecIngestor, StructureInputPdfIngestor, StructureInputEnhanceIngestor, StructureInputBasic
]
