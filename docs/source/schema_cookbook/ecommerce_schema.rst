E-Commerce Schema
==================

Introduction
-------------
The schema below is designed to structure data about e-commerce. In particular, we extract information from various specific merchants (such as Louis Vitton or Samsung). We get their price, description, and a link to purchase on a retail aggregator (such as Amazon), among other things.

Design Decisions
-----------------
This schema is fairly simple but very powerful! Sometimes, a simple schema gets the job done better than anything fancy.

Detailed Descriptions
----------------------
Take a look at each of the description and business description properties. 

These are fairly generically named, so it's helpful to provide context for what you want to find and save. For instance, for products, we don't care about price in the description, but we do care about specifications of the item (color, dimensions, number of pieces, etc.)

Similarly, for the business description property, we specifically mention that we're interested in what kinds of products the company sells, as opposed to say what markets they target or something of that nature. Simple things like this go a long way! 

.. code-block:: python

    DATASET_NAME = "ecommerce_tracking"
    COMPANY_TABLE = "company"
    MERCHANT_TABLE = "merchant"
    # Product Table Properties
    IMAGE_PROPERTY = "product_image"
    PRICE_PROPERTY = "product_price"
    DESCRIPTION_PROPERTY = "description"
    RETAIL_AGGREGATOR_PROPERTY = "retail_aggregator_url"
    PRODUCT_TABLE = "products"
    QUANTITY_PROPERTY = "quantity"
    NAME_PROPERTY = "name"

    # Merchant Table Properties
    WEBSITE_PROPERTY = "website"
    BUSINESS_DESCRIPTION_PROPERTY = "business_description"

    # Relationship
    SELLS_RELATIONSHIP = "sell"
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
                        name=NAME_PROPERTY,
                        description="The name of the product being sold.",
                        merge_strategy=Probabilistic(
                            Probabilistic=MergeConfig(baseline_cardinality=1_000_000, match_transfer_probability=0.9)
                        ),
                    ),
                    Property(
                        name=IMAGE_PROPERTY,
                        description="The image of the product.",
                        prop_type="Image",
                    ),
                    Property(
                        name=PRICE_PROPERTY,
                        description="The price of the product",
                        prop_type="Money",
                    ),
                    Property(
                        name=DESCRIPTION_PROPERTY,
                        description="A detailed description of the product, including specifications and features.",
                    ),
                    Property(
                        name=RETAIL_AGGREGATOR_PROPERTY,
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
