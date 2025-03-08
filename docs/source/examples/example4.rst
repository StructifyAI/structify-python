Tracking Pricing for Semiconductor Parts
=========================================

In this example, we will walk you through the steps of tracking pricing for semiconductor parts.


Step 1: Create the Dataset
-------------------------

First, you are going to want to initialize a dataset to represent semiconductor parts and their pricing. You first do this by defining the schema for the dataset. 
Remember that you are going to need to include a description for each entity, table, and column. We recommend using global variables to store the names of the entities, tables, and columns, as it will make it easier to refer to them later.

.. code-block:: python

    from structify.types.dataset_descriptor import DatasetDescriptor, Relationship
    from structify.types.table import (
        Property,
        Table,
    )

    DATASET_NAME = "Product Parts"
    PRODUCT_PART_TABLE = "Part"
    PRICE_TABLE = "Unit_Price"
    MANUFACTURER_TABLE = "Manufacturer"
    SKU_NAME = "SKU"
    DESCRIPTION_NAME = "Description"
    SPECIFICATIONS_NAME = "Specifications"
    IMAGE_NAME = "Image"
    QUANTITY_NAME = "Quantity"
    UNIT_PRICE_NAME = "Unit_Price"
    TOTAL_PRICE_NAME = "Total_Price"
    PRICING_RELATIONSHIP_NAME = "Pricing"
    MANUFACTURER_RELATIONSHIP_NAME = "Manufacturer"
    MANUFACTURER_NAME = "Name"
    MANUFACTURER_URL_NAME = "URL"
    MANUFACTURER_PHONE_NAME = "Phone"

    def schema():
        return DatasetDescriptor(
            name=DATASET_NAME,
            description="Detailed information about product parts, including pricing details",
            tables=[
                Table(
                    name=PRODUCT_PART_TABLE,
                    description="Information about individual product parts including specifications",
                    properties=[
                        Property(
                            name=SKU_NAME,
                            description="The Stock Keeping Unit identifier for the part",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=DESCRIPTION_NAME,
                            description="A detailed description of the what the part is used for, what it is used in, and any other relevant details",
                        ),
                        Property(
                            name=SPECIFICATIONS_NAME,
                            description="The specifications of the part, including any quantitative metrics such as dimensions, weight, and other relevant details",
                        ),
                        Property(
                            name=IMAGE_NAME,
                            description="An image of the part",
                            prop_type="Image",
                        ),
                    ],
                ),
                Table(
                    name=PRICE_TABLE,
                    description="The pricing structure for the part at a certain scale",
                    properties=[
                        Property(
                            name=QUANTITY_NAME,
                            description="The minimum quantity of the part that can be purchased for a given price",
                            prop_type="Integer",
                        ),
                        Property(
                            name=UNIT_PRICE_NAME,
                            description="The price per unit of the part",
                            prop_type="Money",
                        ),
                        Property(
                            name=TOTAL_PRICE_NAME,
                            description="The total price for the quantity of the part, if explicitly stated",
                            prop_type="Money",
                        ),
                    ],
                ),
                Table(
                    name=MANUFACTURER_TABLE,
                    description="The manufacturer of the part",
                    properties=[
                        Property(name=MANUFACTURER_NAME, description="The name of the manufacturer"),
                        Property(
                            name=MANUFACTURER_URL_NAME,
                            description="The URL of the manufacturer's website",
                            prop_type="URL",
                            merge_strategy="Unique",
                        ),
                        Property(
                            name=MANUFACTURER_PHONE_NAME,
                            description="The phone number of the manufacturer",
                            prop_type="Integer", merge_strategy="Unique"),
                        Property(name=DESCRIPTION_NAME, description="A detailed description of the manufacturer, including any other relevant details"),
                    ],
                ),
            ],
            relationships=[
                Relationship(
                    name=PRICING_RELATIONSHIP_NAME,
                    description="The relationship between a product part and its pricing structure",
                    source_table=PRODUCT_PART_TABLE,
                    target_table=PRICE_TABLE,
                ),
                Relationship(
                    name=MANUFACTURER_RELATIONSHIP_NAME,
                    description="The relationship between a product part and its manufacturer",
                    source_table=PRODUCT_PART_TABLE,
                    target_table=MANUFACTURER_TABLE,
                ),
            ],
        )

Step 2: Make Helper Functions to Run Plans
----------------------------------------

Now, let's make helper functions to run plans and wait for them to complete.

.. code-block:: python

    from structify import Structify
    from structify.types import KnowledgeGraphParam, EntityParam
    from structify.types.enhance_property_param import EnhancePropertyParam
    from structify.types.enhance_relationship_param import EnhanceRelationshipParam
    from structify.types.plan_param import PlanParam

    def create_plan_for_part(client: Structify, manufacturer_name: str, dataset_name: str):
        # Manually add the manufacturer entity to the dataset
        entity_id = client.entities.add(
            dataset=dataset_name,
            entity_graph=KnowledgeGraphParam(
                entities=[
                    EntityParam(
                        id=0,
                        type=MANUFACTURER_TABLE,
                        properties=[
                            {
                                MANUFACTURER_NAME: manufacturer_name,
                            }
                        ]
                    )
                ],
                relationships=[]
            )
        )

        # Create a plan to populate the info about the manufacturer and then find the relationships between the part and the manufacturer
        plan = PlanParam(
            steps=[
                EnhancePropertyParam(
                    entity_id=entity_id,
                    property_name=MANUFACTURER_URL_NAME
                ),
                EnhancePropertyParam(
                    entity_id=entity_id,
                    property_name=DESCRIPTION_NAME
                ),
                EnhanceRelationshipParam(
                    entity_id=entity_id,
                    relationship_name=MANUFACTURER_RELATIONSHIP_NAME,
                    allow_extra_entities=True # So we can find the pricing information for the part
                ),
                # Since phone number is unessential to finding the relationship, we can check it at the end (in case we grabbed it in an earlier step)
                EnhancePropertyParam(
                    entity_id=entity_id,
                    property_name=MANUFACTURER_PHONE_NAME,
                )
            ]
        )
        client.plan.create(dataset_name=dataset_name, plan=plan)


Step 3: Run the Plans and Wait for Them to Complete
--------------------------------------------------

Now, let's run the plans and wait for them to complete.

.. code-block:: python

    import time

    # Assume you have a text file with a list of manufacturers
    with open("manufacturers.txt", "r") as f:
        manufacturers = f.readlines()

    for manufacturer in manufacturers:
        create_plan_for_part(client, manufacturer, DATASET_NAME)

    # Wait for all the plans to complete
    while True:
        plans = client.plan.list(dataset_name=DATASET_NAME)
        if not any(plan.status == "Running" for plan in plans):
            break
        time.sleep(1)


Step 4: Enhance all Missing Properties
------------------------------------

Now, let's enhance all the missing properties for the parts.

.. code-block:: python

    from tqdm import tqdm

    def enhance_missing_properties_for_table(
        client: Structify, schema: DatasetDescriptor, table_name: str
    ):
        """Helper function to run enhance on all missing properties of all entities in a table"""
        job_ids = []
        properties = [p.name for p in next(t for t in schema.tables if t.name == table_name).properties]
        entities = list(client.datasets.view_table(dataset=schema.name, name=table_name))
        for entity in tqdm(entities, desc=f"Enhancing properties for {table_name}", unit="entity"):
            for prop in properties:
                if prop not in entity.properties:
                    try:
                        job_ids.append(
                            client.structure.enhance_property(
                                entity_id=entity.id,
                                property_name=prop,
                            )
                        )
                    except Exception as e:
                        tqdm.write(f"Error enhancing property: {e}")
        return job_ids

    def enhance_missing_properties(client: Structify, dataset_name: str):
        """Helper function to run enhance on all missing properties of all dataset entities"""
        job_ids = []
        dataset = client.datasets.get(name=dataset_name)
        for table in dataset.tables:
            job_ids.extend(
                enhance_missing_properties_for_table(client, dataset, table.name)
            )

    enhance_missing_properties(client, DATASET_NAME)


Step 5: View the Dataset
----------------------

Now, let's view the dataset to see what parts we sourced from each manufacturer.

.. code-block:: python

    from collections import defaultdict

    semiconductor_parts = client.datasets.view_tables_with_relationships(dataset=DATASET_NAME, name=PRODUCT_PART_TABLE)

    parts_dict = {entity.id: entity for entity in semiconductor_parts.entities}
    relationship_dict = defaultdict(list)
    for relationship in semiconductor_parts.relationships:
        relationship_dict[relationship.from_id].append(relationship)

    for manufacturer in semiconductor_parts.connected_entities:
        if manufacturer.type == MANUFACTURER_TABLE:
            print(f"Manufacturer: {manufacturer.properties[MANUFACTURER_NAME]}")

            for relationship in relationship_dict[manufacturer.id]:
                part = parts_dict[relationship.from_id]
                print(f"{part.properties[SKU_NAME]}: {part.properties[DESCRIPTION_NAME]}")
