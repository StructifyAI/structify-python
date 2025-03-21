Semiconductor Pricing Schema
------------------------------
A schema to help structure the pricing of semiconductor parts
.. code-block:: python

    DatasetDescriptor(
        name=DATASET_NAME,
        description="Detailed information about product parts, including pricing details",
        tables=[
            Table(
                name=PRODUCT_PART_TABLE,
                description="Information about individual product parts including manufacturer and specifications",
                expected_cardinality=100_000,
                properties=[
                    Property(
                        name=MANUFACTURER_NAME,
                        description="The name of the company that manufactures the part",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=10_000, match_transfer_probability=0.4)
                        ),
                    ),
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
                        name=SOURCE_URL_NAME,
                        description="The URL where the part can be purchased",
                        prop_type="URL",
                        merge_strategy="Unique",
                    ),
                    Property(
                        name=LABEL_UNIT_PRICE_NAME,
                        description="The listed price per unit of the part",
                        prop_type="Money",
                    ),
                    Property(
                        name=TOTAL_PRICE_NAME,
                        description="The total price for the quantity of the part, if explicitly stated",
                        prop_type="Money",
                    ),
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
        ],
    )