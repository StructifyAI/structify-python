Grabbing Press about Clients
=============================

In this example, let's say we have an ever updating list of clients, but we want to keep track of the latest press and news about them. We can use Structify to grab the latest press and news about our clients and keep it up-to-date.

Step 1: Define a Dataset
------------------------
First things first. We need a Structify dataset to store all this information. We create one by defining the schema.

.. code-block:: python

    import os

    from structify import Structify
    from structify.types import Table, Property, Relationship
    from structify.sources import Web
    from structify.extraction_criteria import RequiredEntity

    client = Structify(api_key=os.environ["STRUCTIFY_API_TOKEN"])

    # Create the schema for the dataset using our Python Objects
    client.datasets.create(
        name="client_press", 
        description="a dataset that stores all the information about press and social media noise relevant to them.",
        tables=[
            Table(
                name="client",
                description="a list of clients who we cover",
                properties=[
                    Property(name="name", description="The name of the client"),
                    Property(name="bio", description="A one phrase description of the client")
                ]
            )
            Table(
                name="press",
                description="news articles covering our clients",
                properties=[
                    Property(name="title", description="The title of the article"),
                    Property(name="outlet", description="The outlet that published the article")
                ]
            ),
            Table(
                name="social_media_noise",
                description="social media posts about our clients",
                properties=[
                    Property(name="app", description="The social media app"),
                    Property(name="handle", description="The handle of the post"),
                    Property(name="content", description="The content of the post")
                ]
            )
        ],
        relationships=[
            Relationship(
                name="covers",
                description="The client covered in the article",
                source_table="press",
                target_table="client"
            ),
            Relationship(
                name="mentions",
                description="The client mentioned in the social media post",
                source_table="social_media_noise",
                target_table="client"
            )
        ]
    )

Step 2: Grab Current Press & News
----------------------------------
Now, we are going to use the Structify API to grab the latest press and news about our clients. We will use the `client.structure.run_async` endpoint to do this along with the ``RequiredEntity`` extraction criteria.

.. code-block:: python

    # In creating agents to populate the dataset, we have to specify the dataset name and the source
    james = client.structure.run_async(
        dataset="client_press",
        source=Web(starting_website="https://www.espn.com"),
        extraction_criteria=[RequiredEntity(id=0)],
        starting_entity={
            "id": 0,
            "type": "client",
            "properties": {
                "name": "LeBron James"
            }
        }
    )

    musk = client.structure.run_async(
        dataset="client_press",
        source=Web(starting_website="https://www.newyorktimes.com"),
        extraction_criteria=[RequiredEntity(id=0)],
        starting_entity={
            "id": 0,
            "type": "client",
            "properties": {
                "name": "Elon Musk"
            }
        }
    )

    swift = client.structure.run_async(
        dataset="client_press",
        source=Web(starting_website="https://www.variety.com"),
        extraction_criteria=[RequiredEntity(id=0)],
        starting_entity={
            "id": 0,
            "type": "client",
            "properties": {
                "name": "Taylor Swift"
            }
        }
    )

Step 3: Wait for the Jobs to Finish Running
-------------------------------------------
We can use the `job_status` endpoint to check if the jobs are still running. Then, we can use the `client.datasets.view` endpoint to view the dataset.

.. code-block:: python

    while any(status for status in client.structure.job_status(job=[james, musk, swift]) if status.job_status == "Running"):
        time.sleep(10)

    print(client.datasets.view(name="client_press"))
