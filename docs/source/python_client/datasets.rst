Creating Datasets
=================

Overview
--------
Structify's API, at its core, is designed to let developers collect datasets on demand. You can create a dataset in just a few lines of code. This guide will walk you through the first step in getting your first custom dataset: defining your schema.

.. _define-schema:

Defining Your Schema
---------------------
The basis of creating datasets is defining the schema, much like creating a blueprint for a database. The schema of a Structify dataset is comprised of entity tables, which are in turn made up of columns (which we call Properties), and the relationships between them. Check out the example code below for more clarity.

Before you can spin up AI agents to fill up your datasets, we need to define the schema of the dataset. Note that each entity table, column, and relationship in the dataset needs a name and description.

If you have a schema you want your dataset to follow, you can easily pre-define your schema using our Python objects.

.. code-block:: python
    
    from structify import Structify
    from structify.types.dataset_descriptor import DatasetDescriptor, Relationship
    from structify.types.table import Property, Table

    client = Structify()

    tables = [
        Table(
            name="founder",
            description="the founder of a company",
            properties=[
                Property(name="name", description="The name of the founder"),
                Property(name="bio", description="The bio of the founder"),
                Property(name="title", description="The title of the founder"),
            ]
        ),
        Table(
            name="company",
            description="a private company that is interested in raising capital",
            properties=[
                Property(name="name", description="The name of the company"),
                Property(name="business_description", description="The description of the company"),
                Property(name="location", description="The location of the company"),
            ]
        ),
        Table(
            name="investor",
            description="an investor (usually a venture capital firm) that is interested in investing in a company",
            properties=[
                Property(name="name", description="The name of the investor"),
                Property(name="description", description="The description of the investor"),
                Property(name="location", description="The location of the investor"),
            ]
        )
    ]

    relationships = [
        Relationship(
            name="invested",
            description="connects the company to the investor",
            source_table="company",
            target_table="investor"
        ),
        Relationship(
            name="founded",
            description="connects the company to the founder",
            source_table="company",
            target_table="founder"
        )
    ]

    client.datasets.create(
        name="startups", 
        description="A dataset named 'startups' that tells me about their job and education history.", 
        tables=tables,
        relationships=relationships
    )

    client.datasets.get(name="startups")


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

For instance, a strongly typed schema for the founder table might look like this:

.. code-block:: python

    from structify.types.property_type import Enum

    founder_table = Table(
        name="founder",
        description="the founder of a company",
        properties=[
            Property(name="name", description="The name of the founder"),
            Property(name="age", description="the age of the founder", prop_type="Integer"),
            Property(name="linkedin", description="the LinkedIn URL of the founder", prop_type="URL"),
            Property(name="photo", description="the photo of the founder", prop_type="Image"),
            Property(
                name="background",
                description="the professional specialization of the founder",
                prop_type=Enum(
                    Enum=["Sales", "Marketing", "Engineering", "HR", "Finance", "Legal", "Other"]
                )
            )
        ]
    )

And note that you can also add properties to relationships as well.

.. code-block:: python

    from structify.types.dataset_descriptor import Relationship, RelationshipProperty

    invested_relationship = Relationship(
        name="invested",
        description="connects the company to the investor",
        properties=[
            Property(name="amount", description="The amount of money invested", prop_type="Money"),
            Property(name="date_invested", description="The date of the investment", prop_type="Date"),
            Property(name="valuation", description="The valuation of the company at the time of the investment", prop_type="Money"),
            Property(name="round", description="The round of the investment", prop_type=Enum(Enum=["Seed", "Series A", "Series B", "Series C", "Series D", "Series E", "Series F", "Series G", "Series H or later"])),
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
        description="the LinkedIn URL of the founder",
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
        name="founded",
        description="connects the company to the founder",
        source_table="company",
        target_table="founder",
        merge_strategy=RelationshipMergeStrategy(
            source_cardinality_given_target_match=3, # We expect around a founder to start roughly 3 companies in their lifetime
            target_cardinality_given_source_match=2, # And we assume median 2 founders per company
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
    client.datasets.get(name="startups")
