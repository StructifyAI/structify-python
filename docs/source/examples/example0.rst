Grabbing Press about Clients
=============================

In this example, let's say we have an ever updating list of clients, but we want to keep track of the latest press and news about them. We can use Structify to grab the latest press and news about our clients and keep it up-to-date.

Step 1: Define a Dataset
------------------------
First things first. We need a Structify dataset to store all this information. We create one by defining the schema.

.. code-block:: python

    from structify import Structify
    from structify.types import Table, Property
    from structify.types.dataset_descriptor import Relationship, RelationshipProperty

    client = Structify()

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
                    Property(name="bio", description="A one phrase description of the client"),
                    Property(name="twitter_handle", description="The Twitter url of the client", prop_type="Url"),
                    Property(name="age", description="The age of the client", prop_type="Integer"),
                    Property(name="location", description="The location of where the client is based"),
                ]
            )
            Table(
                name="press",
                description="news articles covering our clients",
                properties=[
                    Property(name="title", description="The title of the article"),
                    Property(name="outlet", description="The outlet that published the article"),
                    Property(name="topic", description="The topic of the article", prop_type=Enum(Enum=["Sports", "Entertainment", "Politics", "Business", "Science", "Technology", "Other"])),
                    Property(name="content_overview", description="A short overview of the content of the article")
                ]
            ),
            Table(
                name="social_media_noise",
                description="social media posts about our clients",
                properties=[
                    Property(name="app", description="The social media app", prop_type=Enum(Enum=["Twitter", "YouTube", "LinkedIn", "Reddit", "Other"])),
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
                target_table="client",
                properties=[
                    RelationshipProperty(name="date", description="The date the article was published", prop_type="Date")
                ]
            ),
            Relationship(
                name="mentions",
                description="The client mentioned in the social media post",
                source_table="social_media_noise",
                target_table="client",
                properties=[
                    RelationshipProperty(name="date", description="The date the post was published", prop_type="Date")
                ]
            )
        ]
    )

Step 2: Add Entities to the Dataset
-----------------------------------
Now, we are going to add some entities to the dataset. We will start with the clients.

.. code-block:: python

    for celeb in ["LeBron James", "Taylor Swift", "Elon Musk"]:
        client.entities.add(
            dataset="client_press",
            entity_graph={
                "id": 0,
                "type": "client",
                "properties": {"name": celeb}
            }
        )

Step 3: Grab Current Press & News
----------------------------------
Now, we are going to use the Structify Plans API to populate the dataset. Our strategy will be to:
#. Find the twitter handle of the client
#. Find the latest social media posts from the client
#. Find the latest articles about the client


.. code-block:: python
    from structify.types.enhance_property_param import EnhancePropertyParam
    from structify.types.enhance_relationship_param import EnhanceRelationshipParam
    from structify.types.plan_param import PlanParam

    celebs = client.datasets.view_table(name="client", dataset="client_press")
    for celeb in celebs:
        steps = [
            # First find the twitter handle
            EnhancePropertyParam(
                entity_id=celeb.id,
                property_name="twitter_handle"
            ),
            # Find relationships in parallel
            [
                EnhanceRelationshipParam(
                    entity_id=celeb.id,
                    relationship_name="mentions",
                    allow_extra_entities=True
                ),
                EnhanceRelationshipParam(
                    entity_id=celeb.id,
                    relationship_name="covers",
                    allow_extra_entities=True
                )
            ]
        ]
        client.plans.create(dataset="client_press", plan=PlanParam(steps=steps))


Step 3: Wait for the Plans to Finish Running
-------------------------------------------
We can use the `plan.list` endpoint to check if the plans are still running. Then, we can use the `client.entities.view` endpoint to view the dataset.

.. code-block:: python

    while True:
        time.sleep(60)
        plans = client.plan.list()
        print(f"Checking if all of {len(plans)} plans are done")
        if not any(plan.status == "Running" for plan in plans):
            break

    for celeb in celebs:
        print(client.entities.view(entity_id=celeb.id, dataset="client_press"))
