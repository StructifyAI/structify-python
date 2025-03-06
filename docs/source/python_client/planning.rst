Managing Plans
=============

In many cases, you may have a "plan of attack" in mind for how to best populate a dataset. In order to streamline this process, we've created the ``plan`` API.

Plans allow you to orchestrate a series of enhancement steps that run consecutively as each step completes. This is useful for complex data enrichment workflows.

Creating Plans
-------------
To create a new plan:

.. code-block:: python

    from structify.types.enhance_property_param import EnhancePropertyParam
    from structify.types.enhance_relationship_param import EnhanceRelationshipParam
    from structify.types.plan_param import PlanParam

    ENTITY_ID = "Entity-12345678-abcd-efgh-ijkl-987654321"

    # Define enhancement steps for the given entity
    steps = [
        # Enhance company properties
        EnhancePropertyParam(
            entity_id=ENTITY_ID,
            property_name="business_description"
        ),
        
        # Find relationships
        EnhanceRelationshipParam(
            entity_id=ENTITY_ID, 
            relationship_name="investors",
            allow_extra_entities=True
        ),
        
        # Multiple parallel steps
        [
            EnhancePropertyParam(
                entity_id=ENTITY_ID,
                property_name="founding_date"
            ),
            EnhancePropertyParam(
                entity_id=ENTITY_ID, 
                property_name="headcount"
            )
        ]
    ]

    # Create the plan
    plan_id = structify.plan.create(
        dataset="companies",
        plan=PlanParam(steps=steps)
    )

Managing Plans
-------------
List all your plans:

.. code-block:: python

    plans = structify.plan.list()
    for plan in plans:
        print(f"Plan {plan.id}: {plan.status}")

Pause all running plans for a dataset:

.. code-block:: python

    response = structify.plan.pause_all(
        dataset_name="companies"
    )
    print(f"Paused {response.paused_count} plans")

Resume all paused plans:

.. code-block:: python

    response = structify.plan.resume_all(
        dataset_name="companies"
    )
    print(f"Resumed {response.resumed_count} plans")

.. tip::
    Plans are a powerful way to orchestrate complex data enrichment workflows. You can:
    
    - Run steps sequentially or in parallel
    - Enhance both properties and relationships
    - Pause and resume execution as needed

.. note::
    When a plan is created, it begins executing immediately. Use pause_all() if you 
    need to temporarily stop execution.
