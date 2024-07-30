Making the Internet Your Database
=================================

The central feature of Structify is structuring unstructured data on the web. It's a powerful tool that can transform the web into an always-up-to-date database.

Grabbing Relevant Press & News about Clients
--------------------------------------------

In this example, let's say we have an ever updating list of clients, but we want to keep track of the latest press and news about them. We can use Structify to grab the latest press and news about our clients and keep it up-to-date.

Step 1: Define a Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We can use the `job_status` endpoint to check if the jobs are still running. Then, we can use the `client.datasets.view` endpoint to view the dataset.

.. code-block:: python

    while any(status for status in client.structure.job_status(job=[james, musk, swift]) if status.job_status == "Running"):
        time.sleep(10)

    print(client.datasets.view(name="client_press"))


Finding contacts in your network
--------------------------------------------

In this tutorial, we will walk you through the steps of finding people in your network based on certain domain expertise.
For example, you might be curious to know who you know that has experience in the field of "AI Infrastructure" or "Beauty and Apparel".
Or you could want to know who in your network has experience in "Python" or "Sales".
With Structify, getting this information has never been easier.

Step 1: Create a Network Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
First, you are going to want to initialize a dataset to represent your network. You first do this by defining the schema for the dataset. 
The schema is a JSON object that defines the structure of the dataset. Remember that you are going to need to include a description for each entity, table, and column.

.. code-block:: python

    from structify import Structify, Source, Table, Property, relationship

    client = Structify(headers = {"apiKey": "your-api-key-here"})

    # Define the schema for the dataset using our Python Objects
    schema = [
        Table(
            name = "person",
            description = "A person in my network",
            properties = [
                Property(name = "name", description = "The name of the person"),
                Property(name = "photo", description = "A photo of the person"),
                Property(name = "linkedin_url", description = "The LinkedIn URL of the person")
            ],
            relationships = [
                Relationship(name = "worked_at", description = "The jobs the person has held"),
                Relationship(name = "educated_at", description = "The schools the person has attended")
            ]
        ),
        Table(
            name = "job",
            description = "A job a person has held",
            properties = [
                Property(name = "title", description = "The title of the job"),
                Property(name = "company", description = "The company the person worked for"),
                Property(name = "industry", description = "The industry the company is in")
            ],
            relationships = []
        ),
        Table(
            name = "school",
            description = "A school a person has attended",
            properties = [
                Property(name = "name", description = "The name of the school"),
                Property(name = "degree", description = "The degree the person received"),
                Property(name = "gradyear", description = "The year the person graduated")
            ],
            relationships = []
        )
    ]

    # Create a network dataset
    client.dataset.create(
        name = "my_network",
        description = "A dataset representing the job and educational experience of people in my network",
        schema = schema
    )

Step 2: Populate the Network Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, you are going to use the structure endpoint to add data to the dataset. Here, we're doing it synchronously to grab the data from the Web.
Since information about your network can easily be found via LinkedIn, we are going to limit the sources to LinkedIn.

.. code-block:: python

    # Populate the network dataset
    network = client.structure.run(
        name = "my_network",
        source = Source.Web(
            prompt = "use LinkedIn to get details about my first degree connections",
            websites = "linkedin.com")
    )

    print(network)
