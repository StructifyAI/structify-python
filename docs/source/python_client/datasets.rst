Creating Datasets
=================

Overview
--------
Structify's API, at its core, is designed to let developers collect datasets on demand. You can create a dataset in just a few lines of code. This guide will walk you through the first step in getting your first custom dataset: defining your schema.

.. _define-schema:

Defining Your Schema
---------------------
The basis of creating datasets is defining the schema, much like creating a blueprint for a database. The schema of a Structify dataset is comprised of entity tables, which are in turn made up of columns (which we call Properties), and the relationships between them. Check out the example code below for more clarity.

Before you can sping up AI agents to fill up your datasets, we need to define the schema of the dataset. Note that each entity table, column, and relationship in the dataset needs a name and description.

If you have a schema you want your dataset to follow, you can easily pre-define your schema using our Python objects.

.. code-block:: python
    
        from structify import Structify
        from structify.types import Table, Property, Relationship

        client = Structify(api_key=os.environ["STRUCTIFY_API_TOKEN"])

        tables = [
            Table(
                name="job",
                description="the job history of the employee",
                properties=[
                    Property(name="title", description="The title of the job"),
                    Property(name="company", description="The company the employee worked for")
                ]
            ),
            Table(
                name="university",
                description="an educational institution",
                properties=[
                    Property(name="name", description="The name of the school"),
                    Property(name="location", description="The location of the school")
                ]
            ),
            Table(
                name="employee",
                description="details about employees at a certain company.",
                properties=[
                    Property(name="name", description="the full name of the employee"),
                    Property(name="current_title", description="the current title of the employee")
                ]
            )
        ]

        relationships = [
            Relationship(
                name="worked",
                description="connects the employee to their job history",
                source_table="employee",
                target_table="job"
            ),
            Relationship(
                name="education",
                description="connects the employee to their education history",
                source_table="employee",
                target_table="education"
            )
        ]

        client.datasets.create(
            name="employees", 
            description="A dataset named 'employees' that tells me about their job and education history.", 
            tables=tables,
            relationships=relationships
            )

        client.datasets.get(name="employees")

And the output will echo back a representation of the schema you just created.

.. note::
   Coming soon: a ``client.datasets.llm_create`` method to create a dataset with a schema that is automatically generated from just a description.
   This will allow users to, instead of writing out an entire schema, simply input plain text to allow the LLM to create your schema.

.. tip::
    Currently, if you need to edit the schema, you will need to either delete the dataset and recreate it with the edited schema or create a dataset with a new name.
    
    We are working on ``client.datasets.modify`` to allow users to adjust the schema without deleting an existing dataset.


Adding Typing to Your Schema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We allow users to add typing to the properties in the schemas that they define. We currently support the following types:

- **Strings**
- **Integers**
- **Floats**
- **Booleans**
- **Enums**
- **URLs**
- **Date**
- **Money**
- **Image**

Every property in the schema has a default type as a String. 

For instance, a strongly typed schema for an employee table might look like this:

.. code-block:: python

    from structify.types.property_type import Enum
    Table(
        name="employee",
        description="details about employees at a certain company.",
        properties=[
            Property(name="name", description="the full name of the employee"),
            Property(name="age", description="the age of the employee", prop_type="Integer"),
            Property(name="linkedin", description="the LinkedIn URL of the employee", prop_type="URL"),
            Property(name="photo", description="the photo of the employee", prop_type="Image"),
            Property(
                name="department",
                description="the department of the employee",
                prop_type=Enum(
                    Enum=["Sales", "Marketing", "Engineering", "HR", "Finance", "Legal", "Other"]
                )
            )
        ]
    )

And note that you can also add properties to relationships as well.

.. code-block:: python

    from structify.types.dataset_descriptor import Relationship, RelationshipProperty

    Relationship(
        name="worked",
        description="connects the employee to their job history",
        properties=[
            Property(name="title", description="The title of the job"),
            Property(name="start_date", description="The start date of the job", prop_type="Date"),
            Property(name="end_date", description="The end date of the job", prop_type="Date"),
            Property(name="is_full_time", description="Whether the job was full-time or part-time", prop_type="Boolean"),
            Property(name="salary", description="The annual salary of the job", prop_type="Money"),
        ]
    ),


.. _merging:

Merging & Entity Resolution
--------------------------
Structify, for its premium users, comes with a robust entity resolution system. When you define your schema, you can specify the ``merge_strategy`` for each property. The default merge strategy is ``"No Signal"``, which means that our API will not merge and deduplicate entities.

There are three types of major merge strategies:

- **Unique**: All entities that have this property value will be merged into a single entity.
- **Probabilistic**: Using a probabilistic approach, we will merge entities based on the shared properties between them.
- **Relationship Merging**: We will merge entities based on the relationships between them.

When entities are merged, their entity id will be updated to the entity id of the less recently created entity. You can always find the entity id to reference by setting the ``resolve_id`` parameter to ``True`` in the ``client.entities.get`` function.


Unique Merge Strategy
~~~~~~~~~~~~~~~~~~~~
This is the most straightforward merge strategy. If you set the merge strategy to ``"Unique"``, then all entities that have the same property value will be merged together. It effectively removes all duplicates from your dataset.
You set this as part of the ``merge_strategy`` parameter in the ``Property`` object.

.. code-block:: python

    Property(
        name="linkedin",
        description="the LinkedIn URL of the employee",
        prop_type="URL",
        merge_strategy="Unique" # Since LinkedIn URLs have a 1:1 correspondence with people, we can use the Unique merge strategy
    )


Probabilistic Merge Strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This one is a more complex merge strategy that uses a probabilistic approach to merge entities. It is useful when you have a property that is not unique, but still can help inform if an entity from one source is the same as an entity from another source.
Probabilistic merging depends on the concept of "cardinality", which is the number of expected entities that have a certain property value. When thinking of setting a probabilistic merging strategy for a table, you will have to think about the following and set the following parameters:

#. The ``expected_cardinality`` parameter in the ``Table`` object, which refers to the number of expected entities of that type that exist in the world.
#. The ``baseline_cardinality`` parameter for the ``Property`` object, which refers to the number of expected entities that have the same property value.
#. The ``match_transfer_probability`` parameter for the ``Property`` object, which refers to the probability that an entity from one source is the same as an entity from another source given that they have the same property value.

For example, if you are setting a person table of all the people in the US, you would set the ``expected_cardinality`` to the total population of the US. And for the ``baseline_cardinality`` parameter in the birthday property, you would set it to the number of people you expect to have the same birthday. And for the ``match_transfer_probability`` parameter, you would set it to the probability that two people have the same birthday.

.. code-block:: python

    from structify.types.strategy import Probabilistic, MergeConfig

    Table(
        name="person",
        description="a person living in the United States",
        expected_cardinality=330_000_000,
        properties=[
            Property(
                name="name",
                description="the first name of the person",
                merge_strategy=Probabilistic(Probabilistic=MergeConfig(
                    baseline_cardinality=25_000,
                    match_transfer_probability=0.001,
                ))
            ),
            Property(
                name="last_name",
                description="the last name of the person",
                merge_strategy=Probabilistic(Probabilistic=MergeConfig(
                    baseline_cardinality=10_000,
                    match_transfer_probability=0.01,
                ))
            ),
            Property(
                name="email",
                description="the email of the person",
                prop_type="String",
                merge_strategy="Unique"
            ),
            Property(
                name="birthday",
                description="the birthday of the person",
                prop_type="Date",
                merge_strategy=Probabilistic(Probabilistic=MergeConfig(
                    baseline_cardinality=365,
                    match_transfer_probability=0.00001,
                ))
            )
        ]
    )


Relationship Merging
~~~~~~~~~~~~~~~~~~~~~
When you specify a relationship between two tables, you can specify the ``merge_strategy`` for the relationship which defines how we will consider sharing endpoints to a common entity via a relationship in the merging process.

For this you need to specify the following parameters:

#. The ``source_cardinality_given_target_match`` parameter, which refers to the number of expected entities of unique endpoints of any given target table.
#. The ``target_cardinality_given_target_mismatch`` parameter, which refers to the reverse (i.e. the number of expected entities of unique endpoints of any given source table).

Here is an example of how you can specify a relationship merging strategy:

.. code-block:: python

    from structify.types.strategy import RelationshipMergeStrategy

    Relationship(
        name="worked",
        description="connects the employee to their job history",
        source_table="employee",
        target_table="job",
        merge_strategy=RelationshipMergeStrategy(
            source_cardinality_given_target_match=100, # We expect around 100 employees per company
            target_cardinality_given_source_match=5, # We expect around 5 jobs worked over a career
        ),
    )


Manually Merging Entities
~~~~~~~~~~~~~~~~~~~~~~~~~

If you ever need to manually merge entities, you can use the ``client.entities.merge`` function. This will allow you to merge two entities by their index.

.. code-block:: python

    client.entities.merge(
        entity_1_id="123",
        entity_2_id="456",
    )

.. note::
    Please note that this endpoint will automatically resolve the entity IDs to the correct entity reference.

Helpful Dataset Functionality
------------------------------
We also have a few other helpful functions to help you manage your datasets: ``client.datasets.list`` to list all your datasets, and ``client.datasets.get`` to get the schema for a certain dataset.

Here are some examples of how you can use these functions:

.. code-block:: python

    # Requires no parameters and will return a list of all your datasets
    client.datasets.list()

    # Requires the name of the dataset and will return the schema
    client.datasets.get(name="employees")
