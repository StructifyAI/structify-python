Structuring Data
================
The main functionality of the Structify API lies in structuring information from a variety of sources on demand.
Our structuring endpoints allow you to direct our research agents to collect data from the web, PDFs, and more to populate your datasets with structured information.

.. _populating-datasets:

Populating Your Datasets
------------------------
Once you have blueprinted your dataset by creating a schema, you can use Structify's AI agents to collect and structure data.

You can run our scraper agents either through ``structify.structure.run`` or ``structify.structure.run_async`` to populate a dataset with an initial batch of data. The structure API call takes the following arguments:

- **name:** *(required)* The name of the dataset you want to populate
- **source:** *(required)* The source you want the agent to use to extract data from. More on this in :ref:`source-types`
- **extraction_criteria:** *(optional)* The criteria you want the agent to use to extract data from the source. More on this in

Here's an example of an API call to populate that employees dataset with data from LinkedIn using ``structify.structure.run``:

.. code-block:: python

    from structify import Structify
    from structify.sources import Web

    structify.structure.run(
        dataset="employees", 
        source=Web(starting_website="linkedin.com")
    )
   
.. note::
    The output of ``structify.structure.run`` will be a view of the extracted entities in the dataset after the run completes.

If you want to run the populate request asynchronously, you can use ``structify.structure.run_async``:

.. code-block:: python

    job_id = structify.structure.run_async(
        dataset="employees", 
        source=Web(starting_website="linkedin.com")
    )

    structify.structure.job_status(job=[job_id])

.. note::
    The output of ``structify.structure.run_async`` will be a Job ID that you can use to access the run and view its status via ``structify.structure.job_status``.


Extraction Criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Extraction Criteria is a way to specify what you want the agent to extract from the source. 
It provides our agents with guidance as to the specific entities, properties, or relationships that need to appear for it to extract data to populate your dataset.
There are three types of extraction criteria that you can specify:

**Required Entity**
In the case that you want to get data about a specific entity, you can specify the entity you want to extract.
This extraction criteria does necessitate that you input the entity into the run or run_async call as follows:

.. code-block:: python

    from structify.extraction_criteria import RequiredEntity
    structify.structure.run(
        dataset="employees", 
        source=Web(starting_website="linkedin.com"),
        extraction_criteria=[RequiredEntity(id=0)],
        starting_entity={
            "id": 0,
            "type": "employee",
            "properties": {
                "name": "Jane Doe"
            }
        }
    )
    
.. note::
    The ID you specify in the extraction criteria must match the id of the starting_entity.

**Required Property**
In the case that you want to require that a certain property be present for a table before extracting data, you can use the required property extraction criteria.

.. code-block:: python

    from structify.extraction_criteria import RequiredProperty
    structify.structure.run(
        dataset="employees", 
        source=Web(starting_website="linkedin.com"),
        extraction_criteria=[RequiredProperty(
            table="job",
            properties=["title", "company"]
        )]
    )

.. note::
    The agent will extract data if at least one of the specified properties are present.

**Required Relationship**
In the case that you want to require that a certain relationship be present for a table before extracting data, you can use the required relationship extraction criteria.

.. code-block:: python

    from structify.extraction_criteria import RequiredRelationship
    structify.structure.run(
        dataset="employees", 
        source=Web(starting_website="linkedin.com"),
        extraction_criteria=[RequiredRelationship(
            relationship_name="worked"
        )]
    )

You can input multiple extraction criteria to ensure a set of conditions are met before saving data.

.. _source-types:

Sources
-----------------------
You can use a variety of sources to populate your datasets such as:

- **Web**: Our AI agents can navigate the Web and scrape data at scale. This is our bread and butter.
- **PDF**: We can also extract unstructured data from PDFs.
- **Text**: If you have plain text you want to structure, you can use this source.
- **SEC Filings**: We also have a direct integration to the SEC if you want to extract data from their filings.
- **DocumentImage**: We support any other document types through this endpoint. It does require users to convert their documents into images first.

Below are some examples of how you can start structuring runs on each source:

Web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from structify.sources import Web

    structify.structure.run_async(
        name = "employees", 
        sources = Web(starting_website = "linkedin.com")
    )

PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from structify.sources import PDF

    structify.structure.run_async(
        name = "employees", 
        sources = PDF()
    )

Populating Datasets from Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sometimes, you will want to collect data from documents, such as PDFs or PNGs. You can use the ``structify.structure.run`` and ``structify.structure.run_async`` endpoint off of documents as well. 

We'll walk you through the process to uploading documents and such in the :doc:`documents` section. Or you can check out the tutorials at :ref:`document-example`.


Additional Source Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We allow for two other sources besides the Web and Documents: SEC filings or plain text.

If you'd like to use Structify to just structure plain text, you can simply pass the text to the API call as such:

.. code-block:: python
    
    structify.structure.run(
        name = "employees", 
        sources = Source.Text(text = "John Doe is the CEO of ACME. Previously he was the Senior VP at EMCA.")
    )


If you'd like to use Structify to get datasets from SEC filings, you can use the following:

.. code-block:: python
        
    structify.structure.run(
        name = "employees", 
        sources = Source.SECFiling(
            year = 2021, # Optional
            quarter = 3, # Optional
            accession_number = "0000320193-21-000056" # Optional
        )
    )

.. _view-dataset:

Viewing Your Datasets
---------------------------------------
Through this endpoint, we allow users to view specific parts of the dataset that they are interested in. For example, if want to allow users to see the names of the schools that each person attended and their graduation date in their employees dataset, we could create the following view:

.. code-block:: python

    from pprint import pprint
    
    pprint(client.dataset.view(name = dataset_name, table = "education"))

The output will be a JSON object containing the properties and relationships of the entities in the education table (along with their ids).

.. note::
    
    We are in the process of adding the ability to view multiple tables at once, or limited the view of a dataset to a certain set of columns. In addition, we are working on methods to export your datasets.

Helpful Dataset functionality
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We also have a few other helpful functions to help you manage your datasets: ``structify.dataset.delete`` to delete a dataset, ``structify.dataset.list`` to list all your datasets, and ``structify.dataset.info`` to get info on a certain dataset, including the name.

Here are some examples of how you can use these functions:

.. code-block:: python

    # Requires no parameters and will return a list of all your datasets in a JSON object
    structify.dataset.list()

    # Requires the name of the dataset and will return the schema as a JSON object
    structify.dataset.info(name = "employees")

    # Requires the name of the dataset and will delete the dataset
    strucctify.dataset.delete(name = "employees")

 
.. _Refreshing-Dataset:

Refreshing Your Dataset
-----------------------
Of course, the data in your dataset will become outdated over time. Currently, to refresh your dataset, you will want to set a recurring schedule or refresh the dataset continuously. We are developing an endpoint that will streamline this functionality, but in the meantime, we recommend you use the following:

.. code-block:: python

    while True:
        run = structify.structure.run_async(
            name = "employees", 
            sources = Source.Web(prompt = "find me details about the employees of ACME", websites = ["linkedin.com"])
        )
        structify.structure.wait(run)

If you have a regular schedule you want to run the refresh, you can use the ``schedule`` library to run the refresh on a schedule. Here's an example of how you can run the refresh every day at 3:00 PM:

.. code-block:: python

    from schedule import every, run_pending
    import time

    every().day.at("15:00").do(
        structify.structure.run_async, 
        name = "employees", 
        sources = Source.Web(
            prompt = "find me details about the employees of ACME", 
            websites = ["linkedin.com"]
        )
    )

    while True:
        run_pending()
        time.sleep(1)



.. note::
    Keep your eye out for the ``structify.dataset.refresh`` API call to update the data in your dataset.

For one-time refreshes, we recommend just running ``structify.structure.run`` again to update the dataset.



