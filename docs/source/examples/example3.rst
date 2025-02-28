Creating a Dataset for Your Network
================================

In this tutorial, we will walk you through the steps of finding people in your network based on certain domain expertise.
For example, you might be curious to know who you know that has experience in the field of "AI Infrastructure" or "Beauty and Apparel".
Or you could want to know who in your network has experience in "Python" or "Sales".
With Structify, getting this information has never been easier.

Step 1: Create a Network Dataset
--------------------------------
First, you are going to want to initialize a dataset to represent your network. You first do this by defining the schema for the dataset. 
The schema is a JSON object that defines the structure of the dataset. Remember that you are going to need to include a description for each entity, table, and column.

.. code-block:: python

    import os
    import time

    from structify import Structify
    from structify.sources import Web
    from structify.types import Table, Property, Relationship

    client = Structify(api_key=os.environ["STRUCTIFY_API_TOKEN"])

    # Define the schema for the dataset using our Python Objects when using the datasets.create endpoint
    client.datasets.create(
        name="my_network",
        description="A dataset representing the job and educational experience of people in my network",
        tables=[
            Table(
                name="person",
                description="A person in my network",
                properties=[
                    Property(name="name", description="The name of the person"),
                    Property(name="linkedin_url", description="The LinkedIn URL of the person")
                ]
            ),
            Table(
                name="job",
                description="A job a person has held",
                properties=[
                    Property(name="title", description="The title of the job"),
                    Property(name="company", description="The company the person worked for"),
                    Property(name="industry", description="The industry the company is in")
                ]
            ),
            Table(
                name="school",
                description="A school a person has attended",
                properties=[
                    Property(name="name", description="The name of the school"),
                    Property(name="degree", description="The degree the person received"),
                    Property(name="gradyear", description="The year the person graduated")
                ]
            )
        ],
        relationships=[
            Relationship(
                name="worked_at", 
                description="The jobs the person has held"
                source_table="person",
                target_table="job"
            ),
            Relationship(
                name="educated_at",
                description="The schools the person has attended"
                source_table="person",
                target_table="school"
            )
        ]
    )

Step 2: Populate the Network Dataset
------------------------------------
Next, you are going to use the structure endpoint to add data to the dataset. Here, we're doing it synchronously to grab the data from the Web.
Since information about your network can easily be found via LinkedIn, we are going to limit the sources to LinkedIn.

.. code-block:: python

    # Populate the network dataset
    network = client.structure.run_async(
        dataset="my_network",
        source=Web(starting_website="linkedin.com"),
        extraction_criteria=[RequiredProperty(table_name="person", properties=["name"])]
    )

    # Wait for the job to finish
    while client.structure.job_status(job=[network]) != "Completed":
        time.sleep(5)

Step 3: View the Network Dataset
--------------------------------
Now that you have populated the dataset, you can view the schema of the dataset by using the `client.datasets.view` endpoint.

.. code-block:: python

    entities = client.datasets.view(name="my_network")
    relationships = client.datasets.view(name="my_network", requested_type="Relationships")

    for entity in entities:
        print(entity)
    
    for relationship in relationships:
        print(relationship)
