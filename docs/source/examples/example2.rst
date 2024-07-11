Structifying Documents
=======================
In this tutorial, we've cover how you can use the Structify API to structure information from documents into datasets.
In the end, we'll show you how to implement this into an alternative to using RAG to query documents.

.. _document-example:

Extracting Company Information from Pitch Decks
-----------------------------------------------
This example will walk through the process of uploading pitch decks and extracting the company name, industry, founders, investors, and funding amount from each deck.

Step 1: Upload the Relevant Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Structify allows you to upload PDF documents.
We associate the documents with your account (or your user account), such that multiple datasets can be created from the same document 
(or sets of documents involving some of the same documents and different ones).

.. code-block:: python

    from structify import Structify, Source, Table, Property, Relationship
    import os

    client = Structify(headers = {"apiKey": "your_api_key_here"})

    # You can upload multiple documents at once by specifying a folder than contains them
    folder_path = '/path/to/your/folder/of/pitchdecks'

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, "rb") as file:
                client.documents.upload(file, path = "path/to/your/structify/folder/" + filename, doctype = "Pdf")
        except FileNotFoundError:
            print("File not found at path:", file_path)
        except Exception as e:
            print("An error occurred:", e)


Step 2: Create a Relevant Dataset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, we have to blueprint the schema of the dataset that we are interested in creating from these documents.

.. code-block:: python

    # Create the dataset schema
    schema = [
        Table(
            name = "Company",
            properties = [
                Property(name = "name", description = "The name of the company"),
                Property(name = "industry", description = "The industry of the company"),
                Property(name = "founders", description = "The founders of the company"),
                Property(name = "investors", description = "The investors of the company"),
                Property(name = "funding_amount", description = "The funding amount of the company")
            ],
            relationships = [
                Relationship(name = "investors", description = "The investors of the company"),
            ]
        ),
        Table(
            name = "Investor",
            properties = [
                Property(name = "name", description = "The name of the investor"),
                Property(name = "description", description = "The description of the investor")
            ],
            relationships = []
        )
    ]
    
    
    client.dataset.create(
        name = "pitchdecks",
        description = "A dataset of company information extracted from pitch decks."
        schema = schema
    )

.. note::
    Remember you can always view the schema of any dataset later by using ``client.dataset.info(name = "dataset_name")``.

Step 3: Populate the Dataset using the Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now that we have the dataset schema, we can populate the dataset with the information from the pitch decks.

.. code-block:: python

    import glob

    # Get a list of all the file paths in the folder
    folder_path = '/path/to/your/structify/folder/'
    file_paths = glob.glob(folder_path + '*')

    # Iterate over the file paths and make the API call for each file
    for file_path in file_paths:
        agent = client.structure.run_async(
            name = pitchdecks.name, 
            sources = Source.Document(
                prompt = "Extract company information from the uploaded pitch decks.",
                path = file_path
            )
        )
        client.structure.wait(agent)


Step 4: Query the Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Let's assume you have a user that wants to search through the documents. 
Once you've used the populate method to create the dataset, you can use the query method to search through the documents.

.. code-block:: python

    def query_pitchdecks(query):
        response = client.analysis.query(dataset = "pitchdecks", query = query)
        print(response)

    query_pitchdecks("Who are the investors in ABC Corp?")
    query_pitchdecks("What is the industry of XYZ Inc?")


