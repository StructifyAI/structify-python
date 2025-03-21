Bonus Schema: Pharmaceutical Clinical Trials
--------------------------------------------
.. code-block:: python

    DatasetDescriptor(
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