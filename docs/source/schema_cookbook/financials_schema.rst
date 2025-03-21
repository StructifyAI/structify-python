Financial Data Schema
-------------------------
.. code-block:: python

    DatasetDescriptor(
        name=DATASET_NAME,
        description=(
            "This dataset encompasses comprehensive information about privately held companies that have received "
            "venture capital backing, including details on their funding rounds and investors."
        ),
        tables=[
            Table(
                name=VC_FIRM_TABLE,
                description="Detailed information about venture capital firms that invest in privately held companies.",
                expected_cardinality=10_000,
                properties=[
                    Property(
                        name=NAME_PROPERTY,
                        description="The name the venture capital firm commonly goes by.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=10_000, match_transfer_probability=0.9)
                        ),
                    ),
                    Property(
                        name=WEBSITE_PROPERTY,
                        description=(
                            "The URL of the firm's official website, providing detailed informat"
                            "ion about their services, portfolio, and team."
                        ),
                        merge_strategy="Unique",
                        prop_type="URL",
                    ),
                    Property(
                        name=BUSINESS_DESCRIPTION_PROPERTY,
                        description=(
                            "A comprehensive description of the firm's operations, investment st"
                            "rategy, key focus areas, and notable investments."
                        ),
                    ),
                    Property(
                        name=FOUNDING_DATE_PROPERTY,
                        description="The date when the firm was founded.",
                        prop_type="Date",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=50, match_transfer_probability=0.6)
                        ),
                    ),
                    Property(
                        name=HEADCOUNT_PROPERTY,
                        description="The total number of employees working at the firm.",
                        prop_type="Integer",
                    ),
                    Property(
                        name=LINKEDIN_PROPERTY,
                        description="The URL of the firm's LinkedIn profile, used for professional networking and updates.",
                        merge_strategy="Unique",
                        prop_type="URL",
                    ),
                    Property(
                        name=VC_SECTOR_PROPERTY,
                        description="The specific industry sectors in which the firm prefers to invest.",
                        prop_type=Enum(Enum=list(GICS_INDUSTRIES.keys())),
                    ),
                    Property(
                        name=ADDRESS_PROPERTY,
                        description="The address of the firm's headquarters. Give as much information as is present, including building number, street name, city, state, country, and postal code",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(
                                # VC firms often have multiple addresses in multiple cities
                                baseline_cardinality=1_000,
                                match_transfer_probability=0.4,
                            )
                        ),
                    ),
                    Property(
                        name=LOGO_PROPERTY,
                        description="The firm's logo, used for visual identification.",
                        prop_type="Image",
                    ),
                ],
            ),
            Table(
                name=FUNDING_ROUND_TABLE,
                description="Detailed information about individual transactions and deals between companies and investors.",
                expected_cardinality=200_000,
                properties=[
                    Property(
                        name=ROUND_ANNOUNCED_DATE_PROPERTY,
                        description=(
                            "The date when the funding round was publicly announced, per a press release or other "
                            "publicly available source online."
                        ),
                        prop_type="Date",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=500, match_transfer_probability=0.4)
                        ),
                    ),
                    Property(
                        name=ROUND_RAISED_AMOUNT_PROPERTY,
                        description=(
                            "The total amount of capital raised during this funding round, expre"
                            "ssed in monetary terms, per a publicly available source online such as a press release."
                        ),
                        prop_type="Money",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=1_000, match_transfer_probability=0.6)
                        ),
                    ),
                    Property(
                        name=ROUND_STAGE_PROPERTY,
                        description=(
                            "The specific stage of the funding round, such as 'Seed', 'Series A'"
                            ", 'Series C', or 'Growth'."
                        ),
                        prop_type=Enum(Enum=STAGES),
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=10, match_transfer_probability=0.8)
                        ),
                    ),
                ],
            ),
            Table(
                name=COMPANY_TABLE,
                description=(
                    "Comprehensive details about companies that have received venture capital investment,"
                    " including their operations, financial performance, and ownership."
                ),
                expected_cardinality=50_000,
                properties=[
                    Property(
                        name=NAME_PROPERTY,
                        description="The common name under which the company operates.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=30_000, match_transfer_probability=0.9)
                        ),
                    ),
                    Property(
                        name=WEBSITE_PROPERTY,
                        description=(
                            "The URL of the company's main website, providing information about "
                            "their products, services, and corporate information."
                        ),
                        prop_type="URL",
                        merge_strategy="Unique",
                    ),
                    Property(
                        name=BUSINESS_DESCRIPTION_PROPERTY,
                        description=(
                            "A brief yet detailed summary of what the company does, includin"
                            "g its products, services, target market, and value proposition."
                        ),
                    ),
                    Property(
                        name=FOUNDING_DATE_PROPERTY,
                        description="The date when the company was founded.",
                        prop_type="Date",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=50, match_transfer_probability=0.6)
                        ),
                    ),
                    Property(
                        name=HEADCOUNT_PROPERTY,
                        description="The total number of employees working at the company.",
                        prop_type="Integer",
                    ),
                    Property(
                        name=ADDRESS_PROPERTY,
                        description="The address of the company's headquarters, including as much information as possible. If present, extract the following: building number, street name, city, state, country, and postal code.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(
                                baseline_cardinality=500,
                                match_transfer_probability=0.5,
                            )
                        ),
                    ),
                    Property(
                        name=LOGO_PROPERTY,
                        description="The company's logo, used for visual identification.",
                        prop_type="Image",
                    ),
                ],
            ),
        ],
        relationships =[
            Relationship(
                    name=RAISED_RELATIONSHIP,
                    description="Links companies to the individual funding rounds they have completed, detailing their financial transactions.",
                    source_table=COMPANY_TABLE,
                    target_table=FUNDING_ROUND_TABLE,
                    merge_strategy=RelationshipMergeStrategy(
                        source_cardinality_given_target_match=100,
                        target_cardinality_given_source_match=5,
                    ),
                    properties=[
                        RelationshipProperty(
                            name=TRANSACTION_TYPE_PROPERTY,
                            description=("The specific type of financial transaction that took place."),
                            prop_type=Enum(Enum=TRANSACTION_TYPES),
                        ),
                        RelationshipProperty(
                            name=TRANSACTION_FEATURES_PROPERTY,
                            description=("The key feature or grouping of the financial transaction."),
                            prop_type=Enum(Enum=TRANSACTION_FEATURES),
                        ),
                    ],
                ),
                Relationship(
                    name=PORTFOLIO_COMPANY_RELATIONSHIP,
                    description=(
                        "Links venture capital firms to the companies in which they have invested,"
                        "detailing their portfolio of investments."
                    ),
                    source_table=VC_FIRM_TABLE,
                    target_table=COMPANY_TABLE,
                    merge_strategy=RelationshipMergeStrategy(
                        source_cardinality_given_target_match=10,
                        target_cardinality_given_source_match=500,
                    ),
                ),
                Relationship(
                    name=INVESTED_IN_ROUND_RELATIONSHIP,
                    description=(
                        "Links venture capital firms to the deals "
                        "they have participated in, detailing their investment activities."
                    ),
                    source_table=VC_FIRM_TABLE,
                    target_table=FUNDING_ROUND_TABLE,
                    merge_strategy=RelationshipMergeStrategy(
                        source_cardinality_given_target_match=10,
                        target_cardinality_given_source_match=5_000,
                    ),
                    properties=[
                        RelationshipProperty(
                            name=LED_ROUND_PROPERTY,
                            description=(
                                "A value indicating whether the venture capital firm "
                                "led the funding round as the primary investor."
                            ),
                            prop_type="Boolean",
                        ),
                    ],
                ),
            ],
        )