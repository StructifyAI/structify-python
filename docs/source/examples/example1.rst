Monitoring Changes in Datasets
==============================
Using the Structify API, you can easily track changes in datasets over time and keep a database up to date when changes occur. This is helpful to keep up to date on information that changes frequently in large scale, such as company board members, executive team, or other personnel changes.

Tracking Private Company Board Members
--------------------------------------

In this tutorial, imagine you are intested in keeping tabs on who is on the board of various private companies.
Let's say furthermore, you are only interested in companies that are in the technology sector.
You want to know who is on the board of any given company, and you want to know when that information changes.

This information is not readily available, but you can determine it by periodically checking company websites, press releases, and SEC filings.
The goal being to regularly check if there have been any changes. Of course, since all the websites "Team" or "About Us" pages are all formatted differently, this is a near impossible scraping task to execute with high accuracy.

Structify allows you to easily collect this information to track any changes.

Step 1: Upload Your Existing Board Members Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, we want to update the existing dataset that you may have. We start that process from the Structify document endpoint, using the upload call.

.. code-block:: python

    import os

    from structify import Structify
    from structify.sources import Web, Text
    from structify.types import Table, Property, Relationship
    from structify.extraction_criteria import RequiredRelationship

    client = Structify(api_key=os.environ["STRUCTIFY_API_TOKEN"])

    # Here, we suppose that you have a dataset of board members in a CSV file
    # We will use the Structify API to upload this dataset to the platform
    csv_path = "path/to/your/board_members.csv"
    with open(csv_path, 'rb') as f:
        client.documents.upload(content=f, path='/structify/board_members.csv', file_type='Text')

Step 2: Create a Structify Dataset for Board Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, we will need to create a dataset to store the board members information. We can do this by defining the schema in tables, properties, and relationships, making sure to include descriptions for each.

.. code-block:: python

    # We will define the schema we want to use for the dataset in creating the dataset
    board_members = client.datasets.create(
        name="private_tech_company_board_members",
        description="Dataset containing information about board members of private companies in the technology sector.",
        tables=[
            Table(
                name="board_member",
                description="information about board members of private companies in the technology sector",
                properties=[
                    Property(name="name", description="name of the board member"),
                    Property(name="title", description="title of the board member"),
                    Property(name="start_date", description="start date of the board member's tenure"),
                    Property(name="end_date", description="end date of the board member's tenure")
                ]
            ),
            Table(
                name="company",
                description="information about private companies in the technology sector",
                properties=[
                    Property(name="name", description="name of the company"),
                    Property(name="website", description="the url of the company's website")
                ]
            )
        ],
        relationships=[
            Relationship(
                name="sits_on_board",
                description="Company the board member is associated with",
                source_table="board_member",
                target_table="company"
            )
        ]
    )

    # Here, we're populating the dataset with the existing information
    client.structure.run_async(
        dataset="private_tech_company_board_members",
        source=Text(path="/structify/board_members.csv"),
        extraction_criteria=[RequiredRelationship(relationship_name="sits_on_board")]
    )


Step 3: Set Up Regular Refreshes of the Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have a dataset to store the board members information, we want to set up regular refreshes of the dataset to keep the information up to date.

.. code-block:: python

    # After getting the data from the uploaded CSV, we want to get the most recent information from the Internet sources.
    # Simultaneously, we will set up a refresh schedule to run every week at 9:30am

    every().day.at("09:30").do(
        structify.structure.run_async, 
        dataset="private_tech_company_board_members", 
        source=Web("https://www.prnewswire.com"),
        extraction_criteria=[RequiredRelationship(relationship_name="sits_on_board")]
    )

    while True:
        run_pending()
        time.sleep(1)


With this setup, you will be able to keep track of the board members of various private companies in the technology sector.
