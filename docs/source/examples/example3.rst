Finding Menu Items from Restaurants across NYC
===============================================
In some instances, you may want to structure information from PDFs found on the Web. A great example of this is when you want to find menu items from restaurants across NYC.
If you're interested in this feature, the ``pdf_parsing`` feature must be active for your account. As it is only available for premium users at this time, please reach out to us at team@structify.ai if you are interested in activating it.

In this tutorial, we will walk you through the steps of finding menu items from restaurants across NYC.

Step 1: Create the Menu Dataset
------------------------------
First, you are going to want to initialize a dataset to represent restaurants and their menu items. You first do this by defining the schema for the dataset. 
Remember that you are going to need to include a description for each entity, table, and column. A recommended way to do so is to create a schema function that returns a DatasetDescriptor object.

.. code-block:: python

    from structify.types.dataset_descriptor import DatasetDescriptor, Relationship
    from structify.types.table import Property, Table

    DATASET_NAME = "restaurants_and_menus"
    MENU_TABLE = "dish"
    RESTAURANT_TABLE = "restaurant"
    INGREDIENT_TABLE = "ingredient"
    NAME_PROPERTY = "name"
    DESCRIPTION_PROPERTY = "description"
    PRICE_PROPERTY = "price"
    CUISINE_PROPERTY = "cuisine"
    IMAGE_PROPERTY = "image"
    WEBSITE_PROPERTY = "website"
    LOGO_PROPERTY = "logo"
    LOCATION_PROPERTY = "location"
    SERVES_RELATIONSHIP = "serves"


    def schema():
        return DatasetDescriptor(
            name=DATASET_NAME,
            description="A dataset containing information about restaurants and their menus",
            tables=[
                Table(
                    name=RESTAURANT_TABLE,
                    description="The specific location of a restaurant, which is an establishment that serves food",
                    properties=[
                        Property(name=NAME_PROPERTY, description="The name of the restaurant"),
                        Property(name=DESCRIPTION_PROPERTY, description="A description of the restaurant"),
                        Property(name=LOCATION_PROPERTY, description="The location of the restaurant"),
                        Property(
                            name=CUISINE_PROPERTY, description="The cuisine of the restaurant, such as Italian, Thai, etc."
                        ),
                        Property(
                            name=WEBSITE_PROPERTY,
                            description="The website of the restaurant (the specific restaurant's website, not the restaurant group's website)",
                            merge_strategy="Unique",
                            prop_type="URL",
                        ),
                        Property(name=LOGO_PROPERTY, description="The logo of the restaurant", prop_type="Image"),
                    ],
                ),
                Table(
                    name=MENU_TABLE,
                    description="A food item on a menu that the restaurant serves, including sides, salads, appetizers, entrees, and desserts (not drinks)",
                    properties=[
                        Property(name=NAME_PROPERTY, description="The name of the menu item"),
                        Property(name=PRICE_PROPERTY, description="The price of the menu item", prop_type="Float"),
                        Property(name=IMAGE_PROPERTY, description="An image of the menu item", prop_type="Image"),
                        Property(
                            name=DESCRIPTION_PROPERTY,
                            description="A description of the menu item, including all the listed ingredients",
                        ),
                    ],
                ),
            ],
            relationships=[
                Relationship(
                    name=SERVES_RELATIONSHIP,
                    description="The dishes served by a restaurant on a menu",
                    source_table=RESTAURANT_TABLE,
                    target_table=MENU_TABLE,
                ),
            ],
        )

And then it becomes easy to create the dataset and refer to the schema later.

.. code-block:: python

    from structify import Structify

    client = Structify()

    client.datasets.create(**schema().to_dict())


Step 2: Pull Restaurants from an Aggregator
------------------------------------
Next, you are going to use the ``run_async`` endpoint to pull restaurants from an aggregator.
To limit the scope of the data, we will only pull restaurants in NYC.

.. code-block:: python

    # Note how we manually specify the seeded entity. This is because we want to ensure that the restaurant entity is indeed based in NYC
    job = client.structure.run_async(
        dataset="restaurants_and_menus",
        structure_input={
            "web_search": {
                "starting_urls": [
                    "https://www.timeout.com/newyork/restaurants",
                    "https://www.tripadvisor.com/Restaurants-g60763-New_York_City_New_York.html",
                    "https://www.yelp.com/search?find_desc=Restaurants&find_loc=New+York%2C+NY&start=0",
                    "https://www.google.com/search?q=restaurants+in+nyc",
                ],
            },
        },
        extraction_criteria=[
            {"GenericProperty": {"property_names": ["name"], "table_name": "restaurant"}},
            {"EntityExtraction": {"seeded_kg_id": 0}}
        ],
        seeded_entity={
            "entities": [
                {
                    "id": 0,
                    "type": "restaurant",
                    "properties": {
                        "location": "New York City, NY",
                    },
                }
            ],
            "relationships": []
        },
    )

    # Wait for the job to finish
    while client.jobs.get(job_id=job).status != "Completed":
        time.sleep(5)

Step 3: Find the Menus for Each Restaurant
--------------------------------
Now that you have some restaurants, you can use ``structure.enhance_relationship`` to find the menu items for each restaurant.

.. code-block:: python

    for restaurant in client.datasets.view_table(dataset="restaurants_and_menus", name="restaurant"):
        jobs = client.structure.enhance_relationship(
            dataset="restaurants_and_menus",
            relationship=SERVES_RELATIONSHIP,
            entity_id=restaurant.id,
        )
    
    # Wait for the jobs to finish
    for job in jobs:
        while client.jobs.get(job_id=job).status != "Completed":
            time.sleep(5)

Step 4: View & Print the Menus
---------------------
Now that you have some menus, you can view them by using the ``client.datasets.view_tables_with_relationships`` endpoint.

.. code-block:: python

    from collections import defaultdict

    restaurants = client.datasets.view_tables_with_relationships(dataset="restaurants_and_menus", name=RESTAURANT_TABLE)

    menu_dict = {menu.id: menu for menu in restaurants.connected_entities}
    relationship_dict = defaultdict(list)
    for relationship in restaurants.connected_relationships:
        relationship_dict[relationship.source_id].append(relationship)

    for restaurant in restaurants.entities:
        print(f"Restaurant: {restaurant.properties[NAME_PROPERTY]}")
        print("Menu Items:")
        for relationship in relationship_dict[restaurant.id]:
            print(f"Menu: {menu_dict[relationship.target_id].properties[NAME_PROPERTY]}")
            print(f"Price: {menu_dict[relationship.target_id].properties[PRICE_PROPERTY]}")
            print(f"Description: {menu_dict[relationship.target_id].properties[DESCRIPTION_PROPERTY]}")
            print("\n")
        print("-"*100)
