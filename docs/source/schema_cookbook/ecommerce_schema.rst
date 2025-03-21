E-Commerce
---------------------
.. code-block:: python

    DatasetDescriptor(
        name=DATASET_NAME,
        description=(
            "Dataset tracking e-commerce products and merchants, like Louis Vitton or Craftsman, "
            "including product details, merchant information, and relationships. We specifically "
            "want these, not aggregators like Amazon or Shopify."
        ),
        tables=[
            Table(
                name=PRODUCT_TABLE,
                description="Information about e-commerce products, including pricing, images, and descriptions.",
                expected_cardinality=10_000_000,
                properties=[
                    Property(
                        name=PRODUCT_NAME_PROPERTY,
                        description="The name of the product being sold.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=1_000_000, match_transfer_probability=0.9)
                        ),
                    ),
                    Property(
                        name=PRODUCT_IMAGE_PROPERTY,
                        description="The image of the product.",
                        prop_type="Image",
                    ),
                    Property(
                        name=PRODUCT_PRICE_PROPERTY,
                        description="The price of the product",
                        prop_type="Money",
                    ),
                    Property(
                        name=PRODUCT_DESCRIPTION_PROPERTY,
                        description="A detailed description of the product, including specifications and features.",
                    ),
                    Property(
                        name=PRODUCT_AMAZON_PAGE_PROPERTY,
                        description="The URL to the product's page on Amazon or "
                        "another e-commerce platform., if available",
                        prop_type="URL",
                        merge_strategy="Unique",
                    ),
                    Property(
                        name=QUANTITY_PROPERTY, description="The quantity of the product in stock", prop_type="Integer"
                    ),
                ],
            ),
            Table(
                name=COMPANY_TABLE,
                description="Details about merchants selling products online.",
                expected_cardinality=500_000,
                properties=[
                    Property(
                        name=NAME_PROPERTY,
                        description="The name of the merchant or store.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=100_000, match_transfer_probability=0.9)
                        ),
                    ),
                    Property(
                        name=WEBSITE_PROPERTY,
                        description="The official website of the merchant.",
                        prop_type="URL",
                        merge_strategy="Unique",
                    ),
                    Property(
                        name=BUSINESS_DESCRIPTION_PROPERTY,
                        description="A brief but detailed description of the merchant,"
                        " including the types of products they sell.",
                    ),
                ],
            ),
        ],
        relationships=[
            Relationship(
                name=SELLS_RELATIONSHIP,
                description="Links merchants to the products they sell.",
                source_table=COMPANY_TABLE,
                target_table=PRODUCT_TABLE,
            ),
        ],
    )
