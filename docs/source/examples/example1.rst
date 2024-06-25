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

Structify disrupts the manual processes in the status quo and allows you to easily collect this information to track any changes.

Step 1: Upload Your Existing Board Members Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, we want to update the existing dataset that you may have. We start that process from the Structify document endpoint, using the upload call.

.. code-block:: python

    from structify import Structify, Source, Table, Property, Relationship
    client = Structify("your_api_key_here")

    # Here, we suppose that you have a dataset of board members in a CSV file
    # We will use the Structify API to upload this dataset to the platform
    csv_path = "path/to/your/board_members.csv"
    with open(csv_path, 'rb') as f:
        client.documents.upload(f, path = '/structify/board_members.csv', doctype = 'Text')

Step 2: Create a Structify Dataset for Board Members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, we will need to create a dataset to store the board members information. We can do this by defining the schema in tables, properties, and relationships, making sure to include descriptions for each.

.. code-block:: python

    # We will define the schema we want to use for the dataset
    schema = [
        Table(
            name = "board_member",
            description = "information about board members of private companies in the technology sector",
            properties = [
                Property(name = "name", description = "name of the board member"),
                Property(name = "title", description = "title of the board member"),
                Property(name = "start_date", description = "start date of the board member's tenure"),
                Property(name = "end_date", description = "end date of the board member's tenure")
            ]
            relationships = [
                Relationship(name = "company", description = "Company the board member is associated with")
            ]

        ),
        Table(
            name = "company",
            description = "information about private companies in the technology sector",
            properties = [
                Property(name = "name", description = "name of the company"),
                Property(name = "website", description = "the url of the company's website")
            ]
        )
    ]


    # Now, we will create a dataset with the schema
    board_members = client.datasets.create(
        name = "private_tech_company_board_members",
        description = "Dataset containing information about board members of private companies in the technology sector.",
        schema = schema
    )

    # Here, we're populating the dataset with the existing information
    client.structure.run_async(
        name = "private_tech_company_board_members",
        source = Source.Document(
            prompt = "Please structure the CSV containing board member data according to the new schema."
            path = "/structify/board_members.csv")
    )


Step 3: Set Up Regular Refreshes of the Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have a dataset to store the board members information, we want to set up regular refreshes of the dataset to keep the information up to date.

.. code-block:: python

    # After getting the data from the uploaded CSV, we want to get the most recent information from the Internet sources.
    # Simultaneously, we will set up a refresh schedule to run every week at 9:30am

    every().day.at("09:30").do(
        structify.structure.run_async, 
        name = "private_tech_company_board_members", 
        sources = Source.Web(
            prompt = "find me details about the board members and the companies they are associated with in the technology sector.", 
            websites = ["linkedin.com", "techcrunch.com", "prnewswire.com"]
        )
    )

    while True:
        run_pending()
        time.sleep(1)


With this setup, you will be able to keep track of the board members of various private companies in the technology sector.
