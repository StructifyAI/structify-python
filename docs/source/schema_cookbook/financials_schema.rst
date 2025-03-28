Financial Data Schema
======================

Introduction
-------------
The schema below is designed to structure data for Venture Capital firms, including information about VC firms that have previously invested, which rounds they've raised, and the respective raise amounts. This information can help connect investors with companies looking for capital.

Design Decisions
-----------------
A couple of highlights from this schema, from a design perspective: 

* Notice how we restricted stages to ENUMS because they're naturally limited to certain choices
* Take a look at the relationship properties. This is a good example to think about how you should use these when something is a characteristic of the relationship itself (i.e. the led round relationship, that doesn't fit in either the company table funding round table, but it does on the relationship!)

Also, consider how we decided to link the company table and the vc firm table not directly, but rather with another table. 

This allows the data to be structured very neatly, even though it may seem intuitive to make the funding round itself the relationship.

Detailed Descriptions
----------------------
Take a look at the address property. In its description, we're extremely clear about what we're looking to extract. This gives a lot of guidance to our model and creates better results.

The business description property is another good example; it's different between VC firm and company! This is because we're interested in different things about each. Attention to detail like this can make all the difference, so make sure to keep an eye on the specificity of your descriptions!

.. code-block:: python

    STAGES = [
        "Seed",
        "Series A",
        "Series B",
        "Series C",
        "Series D",
        "Series E",
        "Series F",
        "Series G",
        "Series H",
        "Series I",
        "Series J",
        "Pre-Seed",
        "Pre-Series A",
        "Pre-Series B",
        "Growth",
        "Debt",
        "Crowd Funding",
        "Bridge",
        "Angel",
        "Accelerator",
        "Merger or Acquisition",
        "Venture",
    ]

    DatasetDescriptor(
        name="venture_capital_funding",
        description=(
            "This dataset encompasses comprehensive information about privately held companies that have received "
            "venture capital backing, including details on their funding rounds and investors."
        ),
        tables=[
            Table(
                name="vc_firm",
                description="Detailed information about venture capital firms that invest in privately held companies.",
                expected_cardinality=10_000,
                properties=[
                    Property(
                        name="name",
                        description="The name the venture capital firm commonly goes by.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=10_000, match_transfer_probability=0.9)
                        ),
                    ),
                    Property(
                        name="website",
                        description=(
                            "The URL of the firm's official website, providing detailed informat"
                            "ion about their services, portfolio, and team."
                        ),
                        merge_strategy="Unique",
                        prop_type="URL",
                    ),
                    Property(
                        name="description",
                        description=(
                            "A comprehensive description of the firm's operations, investment st"
                            "rategy, key focus areas, and notable investments."
                        ),
                    ),
                    Property(
                        name="founded_date",
                        description="The date when the firm was founded.",
                        prop_type="Date",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=50, match_transfer_probability=0.6)
                        ),
                    ),
                    Property(
                        name="headcount",
                        description="The total number of employees working at the firm.",
                        prop_type="Integer",
                    ),
                    Property(
                        name="linkedin_url",
                        description="The URL of the firm's LinkedIn profile, used for professional networking and updates.",
                        merge_strategy="Unique",
                        prop_type="URL",
                    ),
                    Property(
                        name="address",
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
                        name="logo",
                        description="The firm's logo, used for visual identification.",
                        prop_type="Image",
                    ),
                ],
            ),
            Table(
                name="funding_round",
                description="Detailed information about individual transactions and deals between companies and investors.",
                expected_cardinality=200_000,
                properties=[
                    Property(
                        name="announced_date",
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
                        name="raised_amount",
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
                        name="stage",
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
                name="company",
                description=(
                    "Comprehensive details about companies that have received venture capital investment,"
                    " including their operations, financial performance, and ownership."
                ),
                expected_cardinality=50_000,
                properties=[
                    Property(
                        name="name",
                        description="The common name under which the company operates.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=30_000, match_transfer_probability=0.9)
                        ),
                    ),
                    Property(
                        name="website",
                        description=(
                            "The URL of the company's main website, providing information about "
                            "their products, services, and corporate information."
                        ),
                        prop_type="URL",
                        merge_strategy="Unique",
                    ),
                    Property(
                        name="description",
                        description=(
                            "A brief yet detailed summary of what the company does, includin"
                            "g its products, services, target market, and value proposition."
                        ),
                    ),
                    Property(
                        name="founded_date",
                        description="The date when the company was founded.",
                        prop_type="Date",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=50, match_transfer_probability=0.6)
                        ),
                    ),
                    Property(
                        name="headcount",
                        description="The total number of employees working at the company.",
                        prop_type="Integer",
                    ),
                    Property(
                        name="address",
                        description="The address of the company's headquarters, including as much information as possible. If present, extract the following: building number, street name, city, state, country, and postal code.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(
                                baseline_cardinality=500,
                                match_transfer_probability=0.5,
                            )
                        ),
                    ),
                    Property(
                        name="logo",
                        description="The company's logo, used for visual identification.",
                        prop_type="Image",
                    ),
                ],
            ),
        ],
        relationships =[
            Relationship(
                    name="Transaction",
                    description="Links companies to the individual funding rounds they have completed, detailing their financial transactions.",
                    source_table="company",
                    target_table="funding_round",
                    merge_strategy=RelationshipMergeStrategy(
                        source_cardinality_given_target_match=100,
                        target_cardinality_given_source_match=5,
                    ),
                ),
                Relationship(
                    name="PortfolioCompany",
                    description=(
                        "Links venture capital firms to the companies in which they have invested,"
                        "detailing their portfolio of investments."
                    ),
                    source_table="vc_firm",
                    target_table="company",
                    merge_strategy=RelationshipMergeStrategy(
                        source_cardinality_given_target_match=10,
                        target_cardinality_given_source_match=500,
                    ),
                ),
                Relationship(
                    name="DealParticipant",
                    description=(
                        "Links venture capital firms to the deals "
                        "they have participated in, detailing their investment activities."
                    ),
                    source_table="vc_firm",
                    target_table="funding_round",
                    merge_strategy=RelationshipMergeStrategy(
                        source_cardinality_given_target_match=10,
                        target_cardinality_given_source_match=5_000,
                    ),
                    properties=[
                        RelationshipProperty(
                            name="led_round",
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
