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
    from structify.types.prop_type import Enum

    client = Structify()

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
                description="A private company that is interested in raising capital",
                properties=[
                    Property(name="name", description="The name of the company"),
                    Property(name="industry", description="The industry of the company", prop_type=Enum(Enum=["Technology", "Finance", "Healthcare", "Manufacturing", "Retail", "Other"])),
                    Property(name="description", description="The description of the company"),
                    Property(name="location", description="The location of the company"),
                    Property(name="website", description="The website of the company", prop_type="URL"),
                ],
            ),
            Table(
                name="Investor",
                description="An investor (usually a venture capital firm) that is interested in investing in a company",
                properties = [
                    Property(name="name", description="The name of the investor"),
                    Property(name="description", description="The description of the investor"),
                    Property(name="location", description="The location of the investor"),
                    Property(name="website", description="The website of the investor", prop_type="URL")
                ]
            ),
            Table(
                name="FundingRound",
                description="A funding round for a company",
                properties = [
                    Property(name="amount", description="The amount of the funding round", prop_type="Money"),
                    Property(name="date_announced", description="The date the funding round was announced", prop_type="Date"),
                    Property(
                        name="round_type",
                        description="The type of funding round",
                        prop_type=Enum(
                            Enum=["Seed", "Series A", "Series B", "Series C", "Series D", "Series E", "Series F", "Series G", "Series H"]
                        )
                    )
                ]
            ),
            Table(
                name="Founder",
                description="A founder of a company",
                properties = [
                    Property(name="name", description="The name of the founder"),
                    Property(name="location", description="The location of the founder"),
                    Property(name="linkedin_url", description="The LinkedIn URL of the founder", prop_type="URL"),
                    Property(name="twitter_url", description="The Twitter URL of the founder", prop_type="URL"),
                ]
            )
        ],
        relationships=[
            Relationship(
                name="invested_in",
                description="Designates the portfolio companies of a given investor",
                source_table="Investor",
                target_table="Company"
            ),
            Relationship(
                name="funding_round",
                description="Designates the funding round for a given company",
                source_table="Company",
                target_table="FundingRound"
            ),
            Relationship(
                name="founded",
                description="Designates the founder of a given company",
                source_table="Company",
                target_table="Founder"
            )
        ]
    )

.. note::
    Remember you can always view the schema of any dataset later by using ``client.datasets.get(dataset="dataset_name")``.

Step 3: Create Agent Jobs to Populate the Dataset
-------------------------------------------------
Now that we have the dataset schema, we can populate the dataset with the information from the pitch decks.

.. code-block:: python

    import glob

    from structify.types.save_requirement import RequiredProperty

    # Get a list of all the file paths in the folder
    folder_path = '/path/to/your/structify/folder/'
    file_paths = glob.glob(folder_path + '*')

    # Iterate over the file paths and make the API call for each file
    jobs = []
    for file_path in file_paths:
        job = client.structure.run_async(
            dataset="pitchdecks", 
            source=PDF(path=file_path),
            save_requirement=[RequiredProperty(table_name="Company", property_names=["name"])]
        )
        jobs.append(job)

Step 4: Monitor the Jobs
-----------------------
You can monitor the jobs by using the ``client.jobs.get()`` method.
Below, you'll find a helpful helper function that will wait for all the jobs to complete.

.. code-block:: python

    import time
    from typing import List
    from tqdm import tqdm

    MAX_WAIT_TIME_SECONDS = 60 * 30


    def wait_for_jobs(client: Structify, jobs: List[str], max_wait_time: int = MAX_WAIT_TIME_SECONDS):
        start_time = time.monotonic()

        with tqdm(total=len(jobs), desc="Waiting on Jobs", unit="job") as pbar:
            while True:
                try:
                    statuses = client.structure.job_status(job=jobs)
                    unfinished = sum([status == "Queued" or status == "Running" for status in statuses])

                    pbar.n = len(jobs) - unfinished
                    pbar.refresh()

                    if unfinished == 0 or time.monotonic() - start_time > max_wait_time:
                        break
                except Exception as e:
                    tqdm.write(f"Error waiting for jobs: {e}")

                time.sleep(5)

    wait_for_jobs(client, jobs)

Step 5: View the Dataset
----------------------
You can view the dataset by using the ``client.datasets.view_table()`` method.

.. code-block:: python

    entities = client.datasets.view_table(dataset="pitchdecks", name="Company")

    for entity in entities:
        print(entity)
