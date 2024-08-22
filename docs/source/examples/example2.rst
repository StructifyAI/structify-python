Structifying Pitch Decks
=======================
In this tutorial, we've cover how you can use the Structify API to structure information from documents into datasets.
In the end, we'll show you how to implement this into an alternative to using RAG to query documents.

This example will walk through the process of uploading pitch decks and extracting the company name, industry, founders, investors, and funding amount from each deck.

.. _document-example:

Step 1: Upload the Relevant Documents
-------------------------------------
Structify allows you to upload PDF documents.
We associate the documents with your account (or your user account), such that multiple datasets can be created from the same document 
(or sets of documents involving some of the same documents and different ones).

.. code-block:: python

    import os

    from structify import Structify
    from structify.sources import PDF
    from structify.types import Table, Property, Relationship

    client = Structify(api_key=os.environ["STRUCTIFY_API_TOKEN"])

    # You can upload multiple documents at once by specifying a folder than contains them
    folder_path = '/path/to/your/folder/of/pitchdecks'

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            with open(file_path, "rb") as file:
                client.documents.upload(content=file, path="path/to/your/structify/folder/" + filename, file_type="PDF")


Step 2: Create a Relevant Dataset
-----------------------------------
Next, we have to blueprint the schema of the dataset that we are interested in creating from these documents.

.. code-block:: python

    # Create the dataset schema along with the dataset itself
    client.datasets.create(
        name="pitchdecks",
        description="A dataset of company information extracted from pitch decks."
        tables=[
            Table(
                name="Company",
                properties=[
                    Property(name="name", description="The name of the company"),
                    Property(name="industry", description="The industry of the company"),
                    Property(name="founders", description="The founders of the company"),
                    Property(name="investors", description="The investors of the company"),
                    Property(name="funding_amount", description="The funding amount of the company")
                ],
                relationships = [
                ]
            ),
            Table(
                name="Investor",
                properties = [
                    Property(name="name", description="The name of the investor"),
                    Property(name="description", description="The description of the investor")
                ]
            )
        ],
        relationships=[
            Relationship(
                name="invested_in",
                description="Designates the portfolio companies of a given investor",
                source_table="Investor",
                target_table="Company"
            )
        ]
    )

.. note::
    Remember you can always view the schema of any dataset later by using ``client.datasets.get(name="dataset_name")``.

Step 3: Populate the Dataset using the Documents
-------------------------------------------------
Now that we have the dataset schema, we can populate the dataset with the information from the pitch decks.

.. code-block:: python

    import glob

    # Get a list of all the file paths in the folder
    folder_path = '/path/to/your/structify/folder/'
    file_paths = glob.glob(folder_path + '*')

    # Iterate over the file paths and make the API call for each file
    jobs = []
    for file_path in file_paths:
        job = client.structure.run_async(
            dataset="pitchdecks", 
            source=PDF(path=file_path),
            extraction_criteria=[RequiredProperty(table_name="Company", properties=["name"])]
        )
        jobs.append(job)

    while any([job.job_status != "Completed" for job in jobs]):
        time.sleep(5)

    entities = client.datasets.view(name="pitchdecks")

    for entity in entities:
        print(entity)
