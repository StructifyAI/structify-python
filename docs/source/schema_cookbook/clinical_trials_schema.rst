Pharmaceutical Clinical Trials Schema
======================================

Introduction
-------------
The schema below is designed to structure data for pharmaceutical clinical trials, particularly from the outcome tables associated with each clinical trial. At first glance, this information doesn't map super nicely to structured databases.

With a little creativity, though, it's clear that with Structify, this data can be nicely structured. This schema was discussed previously (check that out here: :ref:`schema-guidance` ), but the main takeaway is to note how we chose to put every major component as a table: pharmaceutical, trial, adverse event, outcome, and participant. This gives maximum flexibility.

Design Decisions
-----------------
Overall, the goal of any schema is to best structure the information you're after. In this case, we achieved it by creating a table for each piece that was of interest, and connecting those via relationships. This creates a nice branching nature to the dataset, wherein each trial connects to multiple participant tables to break out the various groups. Then, each participant table connects to outcome and adverse event tables, to further break down those stats. Each trial is also connect of course to the pharmaceutical (or other treatment) that is its subject.

Finally, we also connect journals to the trials they publish, and companies to the trials they sponsor as helpful additional pieces of data, and for sourcing purposes. 

The participant table allows us to nicely store the numbers associated with each participant group, while also elegantly connecting each participant group to their own outcomes and adverse events via relationships. This allows simulation of the various charts that appear in the clinical trials reports.

In this case, its cleaner to use many relationships and tables rather than to try and cram everything into properties. For instance, you could imagine the treatment group just being a property on each outcome and adverse event table. That technically would've worked, but overall is very messy, leads to duplicate information, and is more fallible. Furthermore, you could imagine it being a relationship property on a relationship between the trial table and each of the other two, BUT then it becomes difficult to keep track of the participant group's details.

The solution outlined solves both of those issues and that's why we believe it's the correct way to build this schema.

Detailed Descriptions
----------------------
Most notable from this schema is the way in which it breaks down ranges as well as time periods to cleanly and specifically structure results. In particular, note how we specify what the least number in a range tends to be (because LLMs tend to be really bad at number operations!)

.. code-block:: python

    DATASET_NAME = "Pharmaceutical_Clinical_Trial_Results"
    TRIAL_TABLE = "Clinical_Trials"
    PHARMACEUTICAL_TABLE = "Pharmaceuticals"
    PARTICIPANT_TABLE = "Trial_Participants"
    OUTCOME_TABLE = "Trial_Outcomes"
    ADVERSE_EVENT_TABLE = "adverse_events"
    JOURNAL_TABLE = "journals"
    COMPANY_TABLE = "pharmaceutical_companies"

    # Clinical Trial Properties
    TRIAL_NAME_PROPERTY = "Trial_Name"
    TRIAL_PHASE_PROPERTY = "Trial_Phase"
    DISEASE_TARGETED_PROPERTY = "Disease_Targeted"
    ENROLLMENT_SIZE_PROPERTY = "Enrollment_Size"
    START_DATE_PROPERTY = "Start_Date"
    END_DATE_PROPERTY = "End_Date"
    PRIMARY_OUTCOME_PROPERTY = "Primary_Outcome"
    SECONDARY_OUTCOME_PROPERTY = "Secondary_Outcome"
    NAME_PROPERTY = "Name"
    WEBSITE_PROPERTY = "Website"

    # Pharmaceutical (Treatment) Properties
    PHARMACEUTICAL_NAME_PROPERTY = "Pharmaceutical_Name"
    PHARMACEUTICAL_TYPE_PROPERTY = "Pharmaceutical_Type"
    ACTIVE_INGREDIENT_PROPERTY = "Active_Ingredient"
    FDA_APPROVAL_STATUS_PROPERTY = "FDA_Approval_Status"

    # Participant Flow Properties
    GROUP_ASSIGNMENT_PROPERTY = "Group_Assignment"
    NUMBER_ENROLLED_PROPERTY = "Number_Enrolled"
    NUMBER_COMPLETED_PROPERTY = "Number_Completed"
    NUMBER_WITHDRAWN_PROPERTY = "Number_Withdrawn"
    NUMBER_ANALYZED_PROPERTY = "Number_Analyzed"

    # Outcome Properties
    OUTCOME_NAME_PROPERTY = "Outcome_Name"
    OUTCOME_MEASURE_PROPERTY = "Outcome_Measure"
    STATISTICAL_SIGNIFICANCE_PROPERTY = "Statistical_Significance"
    CONFIDENCE_INTERVAL_MIN_PROPERTY = "Confidence_Interval_Min"
    CONFIDENCE_INTERVAL_MAX_PROPERTY = "Confidence_Interval_Max"
    P_VALUE_PROPERTY = "P_Value"
    IS_PRIMARY_PROPERTY = "Is_Primary"
    TIME_RANGE_PROPERTY = "Time_Range"
    OUTCOME_UNIT_PROPERTY = "outcome_measure_unit"
    TREATMENT_GROUP_WITH_OUTCOME = "treatment_group"

    # Adverse Event Properties
    EVENT_NAME_PROPERTY = "Event_Name"
    SEVERITY_PROPERTY = "Severity"
    FREQUENCY_PROPERTY = "Frequency"
    TREATMENT_GROUP_AFFECTED_PROPERTY = "Treatment_Group_Affected"

    LOCATION_PROPERTY = "Location"
    DESCRIPTION_PROPERTY = "company_description"
    # Relationships
    ADVERSE_EVENT_RELATIONSHIP = "adverse_event_happened"
    OUTCOME_RELATIONSHIP = "outcome_measured"
    PHARMA_USED_RELATIONSHIP = "pharmaceutical_used"
    TRIAL_RELATIONSHIP = "trial_published"
    SPONSOR_RELATIONSHIP = "trial_sponsored_by"
    PARTICIPANT_RELATIONSHIP = "had_participant_group"


    # Enum Values
    TRIAL_PHASES = [
        "Preclinical",
        "Phase 1",
        "Phase 2",
        "Phase 3",
        "Phase 4",
    ]

    PHARMACEUTICAL_TYPES = [
        "Small Molecule Drug",
        "Biologic",
        "Vaccine",
        "Gene Therapy",
        "Monoclonal Antibody",
        "Other",
    ]

    SEVERITY_LEVELS = ["Mild", "Moderate", "Severe", "Life-Threatening", "Fatal"]

    FDA_APPROVAL_STATUSES = ["Not Approved", "Pending Approval", "Emergency Approval", "Approved"]


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
                    description="Details about the pharmaceutical treatments (often drugs) used in the clinical trials.",
                    expected_cardinality=100_000,
                    properties=[
                        Property(
                            name=PHARMACEUTICAL_NAME_PROPERTY,
                            description="The name of the pharmaceutical treatment.",
                        ),
                        Property(
                            name=PHARMACEUTICAL_TYPE_PROPERTY,
                            description="The type of pharmaceutical product",
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
                    expected_cardinality=150_000,
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
                            name=CONFIDENCE_INTERVAL_MIN_PROPERTY,
                            description="The minimum (left-most number in N-N) confidence interval for the outcome measure.",
                            prop_type="Integer",
                        ),
                        Property(
                            name=CONFIDENCE_INTERVAL_MAX_PROPERTY,
                            description="The maximum (right-most number in N-N) confidence interval for the outcome measure.",
                            prop_type="Integer",
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
                            description="The name of the adverse event, or a phrase that describes its effects.",
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
                    description="Links a participant group to its measured outcomes.",
                    source_table=PARTICIPANT_TABLE,
                    target_table=OUTCOME_TABLE,
                ),
                Relationship(
                    name=ADVERSE_EVENT_RELATIONSHIP,
                    description="Links a clinical trial to its adverse events.",
                    source_table=PARTICIPANT_TABLE,
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
                Relationship(
                    name=PARTICIPANT_RELATIONSHIP,
                    description="The relationship that links a clinical trial to the various "
                    "kinds of participant groups that were a part of it",
                    source_table=TRIAL_TABLE,
                    target_table=PARTICIPANT_TABLE,
                ),
            ],
        )