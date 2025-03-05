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

        structify = Structify(api_key=os.environ["STRUCTIFY_API_TOKEN"])

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
                name="education",
                description="the educational history of an employee",
                properties=[
                    Property(name="school_name", description="The name of the school"),
                    Property(name="school_gradyear", description="The year the employee graduated")
                ]
            ),
            Table(
                name="employee",
                description="details about employees at a certain company.",
                properties=[
                    Property(name="name", description="the full name of the employee")
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

        structify.datasets.create(
            name="employees", 
            description="A dataset named 'employees' that tells me about their job and education history.", 
            tables=tables,
            relationships=relationships
            )

        structify.datasets.get(name="employees")

And the output will echo back a representation of the schema you just created.

.. note::
   Coming soon: a ``structify.datasets.llm_create`` method to create a dataset with a schema that is automatically generated from just a description.
   This will allow users to, instead of writing out an entire schema, simply input plain text to allow the LLM to create your schema.

.. tip::
    Currently, if you need to edit the schema, you will need to either delete the dataset and recreate it with the edited schema or create a dataset with a new name.
    
    We are working on ``structify.datasets.modify`` to allow users to adjust the schema without deleting an existing dataset.

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


Helpful Dataset Functionality
------------------------------
We also have a few other helpful functions to help you manage your datasets: ``structify.datasets.list`` to list all your datasets, and ``structify.datasets.get`` to get the schema for a certain dataset.

Here are some examples of how you can use these functions:

.. code-block:: python

    # Requires no parameters and will return a list of all your datasets
    structify.datasets.list()

    # Requires the name of the dataset and will return the schema
    structify.datasets.get(name="employees")
