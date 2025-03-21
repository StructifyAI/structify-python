Schema Recipes for Success
==========================

Art versus Science in Schema Design
------------------------------------
The way we at Structify approach schema design is to think of it as both an art **and** a science. The proper recipe for a robust and powerful schema will include both creativity in how you build and connect tables, as well as precision in how you define the parameters (properties and relationships) that you're looking to structure.

- **Creativity**
    One of the coolest (and most powerful) things about **structifying** data is that you're fully in control of how the data transforms from unstructured to structured. A lot of thought work can (and should, in complex use cases) go into how you go about building the set of tables and how they connect (the schema for short).
    - Example: I recently built a schema for a use case that wanted to structure pharmaceutical clinical trial results, from graphs and charts present in the write-up. These outcomes can be incredibly convoluted, as they span multiple trial groups, including a control group, as well as results at different dosages. A naive approach (and my first one) was to try and cram all these as properties into one table. After some discussion and whiteboarding with one of my brilliant co-workers, I transformed the schema to look a little different, leveraging creativity in tables and their relationships to build something that more properly encapsulated the data we were looking at. Check out the finished product below.
- **Advice**
    My biggest recommendation when trying to think about how to map your data is to take a step back and think about the problem. Consider what you're trying to structure as a whole, and break it into pieces. What are you interested in seeing atomically? Those are your entities (or **rows**) in a table. Consider what elements describe these things (making them different from each other). Get a list of those, and those are your properties (or **columns**). Now you've got a table for a specific type of entity! Create a table for each **kind** of entity that makes up your data. Finally, consider the things that connect different kinds of entities. These are your relationships! Now you've got a schema! See below for a word on relationship properties.

The Science: Precision in Descriptions
---------------------------------------

Accuracy and clarity in descriptions are fundamental. When defining entities, tables, and properties, make sure to:

- Provide clear and concise definitions.
- Use precise language to avoid ambiguity.
- Avoid overloading properties with too many different kinds of information.
- Consider edge cases, and delineate exact behavior you want for best results.

Example: the Name property. You'll come up with this one a lot, whether it's a person's name, a fictional character's name, or a company's name. Let's take a Person Table and the Name property; you might be tempted to write a description like this: "The name of the person". Here's why that might lead to unexpected results:
    1. People generally have first and last names. What happens if the model comes back with 10 different Alex's, and didn't grab a last name?
        a. Consider this description instead: "A person's full name, including when possible first, middle, and last name, but always AT LEAST a last name" See the difference?
    2. What about titles? Mr. , Mrs. , Dr. Hon. (Honorable, if you didn't know), M.D. , Ph.D. Maybe you want these, maybe you don't. Either way, you should make it clear in the schema!

Enums: When to use Them
-----------------------

The obvious usefulness of enums is that they allow us to restrict values to a pre-determined set (say goodbye to painful data cleaning) and in doing so enable use cases for properties that are naturally limited. For instance, if we had a dataset about professional athletes, and we were interested in looking at their college level as a property we might write an enum that takes in D3, D2, D1 etc.
The hidden power of enums lies in their ability to let dora INFER. For instance, let's say that we're interested in a company's market type (B2B - Business to Businesss vs. B2C -- business to consumer). This is something you'll rarely see written somewhere on a company's website*, so it might be useful to you as an enum. Intuition here is that if we see the company's website, that talks about a product that handles all browser needs for AI companies, we can safely conclude that they're B2B.

*Note: It is of course possible that a separate blog has directly written about a company being B2B SaaS -- in which case, we'll find it. So if you want to find it spelled out, we can do that too, no ENUM necessary. That's the beauty of Structify.*

Below are a few more bonuses to enums:
- Maintain integrity by restricting property values to a predefined set.
- Ensure clarity when representing data that has specific categories, such as "status" or "type."

Relationship Properties -- When to Use Them
--------------------------------------------
Relationships can also have **properties** attached to them, which is where the design gets interesting. For example, a "supplies" relationship between a manufacturer and a product could have a property like "supply rate."

This is a good example of a relationship property because it applies to THAT SPECIFIC relationship between entities. This is because a different manufacturer, that might also supply that product, could have a different supply rate. This means it can't be a property in the product table. Since a manufacturer likely supplies multiple different products, with different supply rates, it can't be in the manufacturer table either. Thus, it's a relationship property. Pretty cool right?

Schema Appendix
----------------

Find below a set of schemas you might find useful, that put these design principles into practice. Give them a try, and let us know what you think!

Schema 1: Semiconductor Parts
------------------------------
.. code-block:: python

    def schema():
        return DatasetDescriptor(
            name=DATASET_NAME,
            description="Detailed information about product parts, including pricing details",
            tables=[
                Table(
                    name=PRODUCT_PART_TABLE,
                    description="Information about individual product parts including manufacturer and specifications",  # noqa: E501
                    expected_cardinality=100_000,
                    properties=[
                        Property(
                            name=MANUFACTURER_NAME,
                            description="The name of the company that manufactures the part",
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=10_000, match_transfer_probability=0.4)
                            ),
                        ),
                        Property(
                            name=SKU_NAME,
                            description="The Stock Keeping Unit identifier for the part",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=DESCRIPTION_NAME,
                            description="A detailed description of the what the part is used for, what it is used in, and any other relevant details",  # noqa: E501
                        ),
                        Property(
                            name=SPECIFICATIONS_NAME,
                            description="The specifications of the part, including any quantitative metrics such as dimensions, weight, and other relevant details",  # noqa: E501
                        ),
                        Property(
                            name=IMAGE_NAME,
                            description="An image of the part",
                            prop_type="Image",
                        ),
                    ],
                ),
                Table(
                    name=PRICE_TABLE,
                    description="The pricing structure for the part at a certain scale",
                    properties=[
                        Property(
                            name=QUANTITY_NAME,
                            description="The minimum quantity of the part that can be purchased for a given price",
                            prop_type="Integer",
                        ),
                        Property(
                            name=UNIT_PRICE_NAME,
                            description="The price per unit of the part",
                            prop_type="Money",
                        ),
                        Property(
                            name=SOURCE_URL_NAME,
                            description="The URL where the part can be purchased",
                            prop_type="URL",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=LABEL_UNIT_PRICE_NAME,
                            description="The listed price per unit of the part",
                            prop_type="Money",
                        ),
                        Property(
                            name=TOTAL_PRICE_NAME,
                            description="The total price for the quantity of the part, if explicitly stated",
                            prop_type="Money",
                        ),
                    ],
                ),
            ],
            relationships=[
                Relationship(
                    name=PRICING_RELATIONSHIP_NAME,
                    description="The relationship between a product part and its pricing structure",
                    source_table=PRODUCT_PART_TABLE,
                    target_table=PRICE_TABLE,
                ),
            ],
        )

Schema 2: E-Commerce
---------------------
.. code-block:: python

    def schema():
        return DatasetDescriptor(
            name=DATASET_NAME,
            description=(
                "Dataset tracking e-commerce products and merchants, like Louis Vitton or Craftsman, "
                "including product details, merchant information, and relationships. We specifically "
                "want these, not aggregators like Amazon or Shopify."
            ),
            tables=[
                Table(
                    name=PRODUCT_TABLE,
                    description="Information about e-commerce products, including pricing, images, and descriptions.",
                    expected_cardinality=10_000_000,
                    properties=[
                        Property(
                            name=PRODUCT_NAME_PROPERTY,
                            description="The name of the product being sold.",
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=1_000_000, match_transfer_probability=0.9)
                            ),
                        ),
                        Property(
                            name=PRODUCT_IMAGE_PROPERTY,
                            description="The image of the product.",
                            prop_type="Image",
                        ),
                        Property(
                            name=PRODUCT_PRICE_PROPERTY,
                            description="The price of the product",
                            prop_type="Money",
                        ),
                        Property(
                            name=PRODUCT_DESCRIPTION_PROPERTY,
                            description="A detailed description of the product, including specifications and features.",
                        ),
                        Property(
                            name=PRODUCT_AMAZON_PAGE_PROPERTY,
                            description="The URL to the product's page on Amazon or "
                            "another e-commerce platform., if available",
                            prop_type="URL",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=QUANTITY_PROPERTY, description="The quantity of the product in stock", prop_type="Integer"
                        ),
                    ],
                ),
                Table(
                    name=COMPANY_TABLE,
                    description="Details about merchants selling products online.",
                    expected_cardinality=500_000,
                    properties=[
                        Property(
                            name=NAME_PROPERTY,
                            description="The name of the merchant or store.",
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=100_000, match_transfer_probability=0.9)
                            ),
                        ),
                        Property(
                            name=WEBSITE_PROPERTY,
                            description="The official website of the merchant.",
                            prop_type="URL",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=BUSINESS_DESCRIPTION_PROPERTY,
                            description="A brief but detailed description of the merchant,"
                            " including the types of products they sell.",
                        ),
                    ],
                ),
            ],
            relationships=[
                Relationship(
                    name=SELLS_RELATIONSHIP,
                    description="Links merchants to the products they sell.",
                    source_table=COMPANY_TABLE,
                    target_table=PRODUCT_TABLE,
                ),
            ],
        )

Schema 3: Financial Data
-------------------------
.. code-block:: python

    def schema():
        return DatasetDescriptor(
            name=DATASET_NAME,
            description=(
                "This dataset encompasses comprehensive information about privately held companies that have received "
                "venture capital backing, including details on their employees, funding rounds, and investors."
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
                            name=LEGAL_NAME_PROPERTY,
                            description="The official legal name of the venture capital firm.",
                            merge_strategy="Unique",
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
                            name=STATUS_PROPERTY,
                            description="The current operational status of the firm, such as 'Active' or 'No Longer Investing'.",  # noqa: E501
                            prop_type=Enum(Enum=INVESTOR_STATUSES),
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
                            description="The URL of the firm's LinkedIn profile, used for professional networking and updates.",  # noqa: E501
                            merge_strategy="Unique",
                            prop_type="URL",
                        ),
                        Property(
                            name=TWITTER_PROPERTY,
                            description="The URL of the firm's Twitter profile, used for social media engagement and updates.",  # noqa: E501
                            merge_strategy="Unique",
                            prop_type="URL",
                        ),
                        Property(
                            name=VC_SECTOR_PROPERTY,
                            description="The specific industry sectors in which the firm prefers to invest.",
                            prop_type=Enum(Enum=list(GICS_INDUSTRIES.keys())),
                        ),
                        Property(
                            name=VC_GEOGRAPHY_PROPERTY,
                            description=(
                                "The specific regions or countries where the firm prefers to invest,"
                                " such as 'North America', 'Europe', or 'Southeast Asia'."
                            ),
                        ),
                        Property(
                            name=ADDRESS_PROPERTY,
                            description="The address of the firm's headquarters. Give as much information as is present, including building number, street name, city, state, country, and postal code",  # noqa: E501
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
                    description="Detailed information about individual transactions and deals between companies and investors.",  # noqa: E501
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
                            name=ROUND_VALUATION_PROPERTY,
                            description=(
                                "The post-money valuation of the company after the completion of the funding ro"
                                "und, reflecting its market value."
                            ),
                            prop_type="Money",
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=1_000, match_transfer_probability=0.7)
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
                        Property(
                            name=ROUND_ADVISOR_PROPERTY,
                            description=(
                                "Any law firms or investment banks that advised the company during the funding round."
                            ),
                        ),
                        Property(
                            name=ROUND_USE_PROPERTY,
                            description=(
                                "The intended purpose for which the raised capital will be used by t"
                                "he company, such as 'expanding operations', 'product development', or 'market expansion'."
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
                            name=COMPANY_CIK_PROPERTY, description="The legal SEC identifier", merge_strategy="Unique"
                        ),
                        Property(
                            name=NAME_PROPERTY,
                            description="The common name under which the company operates.",
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=30_000, match_transfer_probability=0.9)
                            ),
                        ),
                        Property(
                            name=LEGAL_NAME_PROPERTY,
                            description="The official legal name of the company.",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=STATUS_PROPERTY,
                            description="The current operational status of the company, such as 'Active' or 'Acquired'.",
                            prop_type=Enum(Enum=COMPANY_STATUSES),
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
                            name=LINKEDIN_PROPERTY,
                            description="The URL of the company's LinkedIn profile, used for professional networking and updates.",  # noqa: E501
                            prop_type="URL",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=TWITTER_PROPERTY,
                            description="The URL of the company's Twitter profile, used for social media engagement and updates.",  # noqa: E501
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
                            name=COMPANY_SECTOR_PROPERTY,
                            description=(
                                "The specific sector in which the company operates, such as"
                                " 'Technology', 'Healthcare', or 'Finance'."
                            ),
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=20, match_transfer_probability=0.2)
                            ),
                            prop_type=Enum(Enum=list(GICS_INDUSTRIES.keys())),
                        ),
                        Property(
                            name=COMPANY_VERTICAL_PROPERTY,
                            description=(
                                "The specific vertical or niche market that the company operates in," "and sells to."
                            ),
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=50, match_transfer_probability=0.2)
                            ),
                            prop_type=Enum(Enum=list(NAICS_VERTICALS.keys())),
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
                            description="The address of the company's headquarters, including as much information as possible. If present, extract the following: building number, street name, city, state, country, and postal code.",  # noqa: E501
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
                        description="Links companies to the individual funding rounds they have completed, detailing their financial transactions.",  # noqa: E501
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

Bonus Schema: Pharmaceutical Clinical Trials
--------------------------------------------
.. code-block:: python

    def schema():
        return DatasetDescriptor(
            name=DATASET_NAME,
            description=(
                "This dataset tracks the results of pharmaceutical clinical trials, including "
                "participant flow, primary and secondary outcomes, subgroup analyses, and adverse events."
                " It also tracks the pharmaceutical treatments being tested, linking them to clinical trial results."
            ),
            tables=[
                Table(
                    name=TRIAL_TABLE,
                    description="Details about clinical trials, including their phase, "
                    "sponsor, targeted disease, and enrollment size.",
                    expected_cardinality=50_000,
                    properties=[
                        Property(
                            name=TRIAL_NAME_PROPERTY,
                            description="The official name of the clinical trial.",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=TRIAL_PHASE_PROPERTY,
                            description="The phase of the clinical trial.",
                            prop_type=Enum(Enum=TRIAL_PHASES),
                        ),
                        Property(
                            name=DISEASE_TARGETED_PROPERTY,
                            description="The disease or condition being studied in the trial.",
                        ),
                        Property(
                            name=ENROLLMENT_SIZE_PROPERTY,
                            description="The total number of participants enrolled in the trial.",
                            prop_type="Integer",
                        ),
                        Property(
                            name=START_DATE_PROPERTY,
                            description="The date when the trial began.",
                            prop_type="Date",
                        ),
                        Property(
                            name=END_DATE_PROPERTY,
                            description="The date when the trial was completed or terminated.",
                            prop_type="Date",
                        ),
                        Property(
                            name=PRIMARY_OUTCOME_PROPERTY,
                            description="The primary endpoint being measured to determine the trial's success.",
                        ),
                        Property(
                            name=SECONDARY_OUTCOME_PROPERTY,
                            description="Any additional secondary outcome measured in the study. "
                            "If multiple, extract the one of most importance based on the page.",
                        ),
                    ],
                ),
                Table(
                    name=PHARMACEUTICAL_TABLE,
                    description="Details about the pharmaceutical treatments used in the clinical trials.",
                    expected_cardinality=100_000,
                    properties=[
                        Property(
                            name=PHARMACEUTICAL_NAME_PROPERTY,
                            description="The name of the pharmaceutical treatment.",
                        ),
                        Property(
                            name=PHARMACEUTICAL_TYPE_PROPERTY,
                            description="The type of pharmaceutical product "
                            "(e.g., small molecule drug, biologic, vaccine).",
                            prop_type=Enum(Enum=PHARMACEUTICAL_TYPES),
                        ),
                        Property(
                            name=ACTIVE_INGREDIENT_PROPERTY,
                            description="The active ingredient(s) in the pharmaceutical product.",
                        ),
                        Property(
                            name=FDA_APPROVAL_STATUS_PROPERTY,
                            description="The FDA approval status of the pharmaceutical product.",
                            prop_type=Enum(Enum=FDA_APPROVAL_STATUSES),
                        ),
                    ],
                ),
                Table(
                    name=PARTICIPANT_TABLE,
                    description="Details about participant flow, including enrollment, completion, and withdrawal.",
                    expected_cardinality=500_000,
                    properties=[
                        Property(
                            name=GROUP_ASSIGNMENT_PROPERTY,
                            description="The assigned treatment group (e.g., experimental, placebo, control).",
                        ),
                        Property(
                            name=NUMBER_ENROLLED_PROPERTY,
                            description="The number of participants initially enrolled in this group.",
                            prop_type="Integer",
                        ),
                        Property(
                            name=NUMBER_COMPLETED_PROPERTY,
                            description="The number of participants who completed the trial in this group.",
                            prop_type="Integer",
                        ),
                        Property(
                            name=NUMBER_WITHDRAWN_PROPERTY,
                            description="The number of participants who withdrew or were lost to follow-up.",
                            prop_type="Integer",
                        ),
                        Property(
                            name=NUMBER_ANALYZED_PROPERTY,
                            description="The number of participants included in the final analysis.",
                            prop_type="Integer",
                        ),
                    ],
                ),
                Table(
                    name=OUTCOME_TABLE,
                    description="Outcome measures from the trial, including effect size and statistical significance.",
                    expected_cardinality=1_000_000,
                    properties=[
                        Property(
                            name=OUTCOME_NAME_PROPERTY,
                            description="The specific clinical endpoint being measured.",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=TREATMENT_GROUP_PROPERTY,
                            description="The treatment group to which this outcome applies.",
                        ),
                        Property(
                            name=OUTCOME_MEASURE_PROPERTY,
                            description="The numerical value of the outcome measure (e.g., risk ratio, mean difference).",
                            prop_type="Float",
                        ),
                        Property(
                            name=OUTCOME_UNIT_PROPERTY,
                            description="The unit of measurement and qualitative name of the outcome measure",
                        ),
                        Property(
                            name=STATISTICAL_SIGNIFICANCE_PROPERTY,
                            description="Whether the result reached statistical significance.",
                            prop_type="Boolean",
                        ),
                        Property(
                            name=CONFIDENCE_INTERVAL_PROPERTY,
                            description="The confidence interval for the outcome measure.",
                        ),
                        Property(
                            name=P_VALUE_PROPERTY,
                            description="The p-value indicating the significance of the result.",
                            prop_type="Float",
                        ),
                        Property(
                            name=IS_PRIMARY_PROPERTY,
                            description="A boolean to indicate whether or not this was the primary outcome"
                            "being measured for the trial",
                            prop_type="Boolean",
                        ),
                        Property(
                            name=TIME_RANGE_PROPERTY,
                            description="The time range over which this outcome was measured, "
                            "if available and applicable i.e. in 'x lb weight loss over n days', "
                            "n days would be the time range",
                        ),
                    ],
                ),
                Table(
                    name=ADVERSE_EVENT_TABLE,
                    description="Adverse events reported during the trial, including severity and frequency.",
                    expected_cardinality=250_000,
                    properties=[
                        Property(
                            name=EVENT_NAME_PROPERTY,
                            description="The name of the adverse event," " or a phrase that describes its effects.",
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=100_000, match_transfer_probability=0.9)
                            ),
                        ),
                        Property(
                            name=SEVERITY_PROPERTY,
                            description="The severity of the adverse event.",
                            prop_type=Enum(Enum=SEVERITY_LEVELS),
                        ),
                        Property(
                            name=FREQUENCY_PROPERTY,
                            description="The frequency of the adverse event.",
                            prop_type="Integer",
                        ),
                        Property(
                            name=TREATMENT_GROUP_AFFECTED_PROPERTY,
                            description="The treatment group in which the adverse event occurred.",
                        ),
                    ],
                ),
                Table(
                    name=JOURNAL_TABLE,
                    description="Table that contains information about various journals",
                    expected_cardinality=1000,
                    properties=[
                        Property(name=NAME_PROPERTY, description="The name of the journal", merge_strategy="Unique"),
                        Property(
                            name=WEBSITE_PROPERTY,
                            description="The base website of the journal",
                            merge_strategy="Unique",
                            prop_type="URL",
                        ),
                    ],
                ),
                Table(
                    name=COMPANY_TABLE,
                    description="Table that contains information about various pharmaceutical companies"
                    " research organizations, and other groups that sponsor clinical trials",
                    expected_cardinality=10_000,
                    properties=[
                        Property(name=NAME_PROPERTY, description="The name of the company", merge_strategy="Unique"),
                        Property(
                            name=WEBSITE_PROPERTY,
                            description="The website of the company",
                            merge_strategy="Unique",
                            prop_type="URL",
                        ),
                        Property(
                            name=DESCRIPTION_PROPERTY,
                            description="A detailed but concise description of what kinds of "
                            "drugs and treatments the company develops",
                        ),
                        Property(
                            name=LOCATION_PROPERTY,
                            description="The geographical location of the company, being as specific as possible. "
                            "As general as just the state is acceptable if the company is U.S. based",
                            merge_strategy=Probabilistic(
                                Probabilistic=MergeConfig(baseline_cardinality=10_000, match_transfer_probability=0.7),
                            ),
                        ),
                    ],
                ),
            ],
            relationships=[
                Relationship(
                    name=PHARMA_USED_RELATIONSHIP,
                    description="Links a clinical trial to the pharmaceutical treatment being tested.",
                    source_table=TRIAL_TABLE,
                    target_table=PHARMACEUTICAL_TABLE,
                ),
                Relationship(
                    name=OUTCOME_RELATIONSHIP,
                    description="Links a clinical trial to its measured outcomes.",
                    source_table=TRIAL_TABLE,
                    target_table=OUTCOME_TABLE,
                ),
                Relationship(
                    name=ADVERSE_EVENT_RELATIONSHIP,
                    description="Links a clinical trial to its adverse events.",
                    source_table=TRIAL_TABLE,
                    target_table=ADVERSE_EVENT_TABLE,
                ),
                Relationship(
                    name=TRIAL_RELATIONSHIP,
                    description="Links a journal to the clinical trials it publishes",
                    source_table=JOURNAL_TABLE,
                    target_table=TRIAL_TABLE,
                ),
                Relationship(
                    name=SPONSOR_RELATIONSHIP,
                    description="The relationship that links a pharmaceutical company or research"
                    " organization to the clinical trial(s) it sponsors.",
                    source_table=TRIAL_TABLE,
                    target_table=COMPANY_TABLE,
                ),
            ],
        )