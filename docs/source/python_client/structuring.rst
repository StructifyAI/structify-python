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
- **extraction_criteria:** *(optional)* The criteria you want the agent to use to extract data from the source. More on this in :ref:`extraction-criteria`

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

.. _extraction-criteria:

Extraction Criteria
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Extraction Criteria is a way to specify what you want the agent to extract from the source. 
It provides our agents with guidance as to the specific entities, properties, or relationships that need to appear for it to extract data to populate your dataset.
If not specified, the default value will be an empty list, meaning the agent will extract any data from the provided source that is present in the schema.
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
        dataset="employees", 
        source=Web(starting_website="linkedin.com")
    )

PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from structify.sources import PDF

    structify.structure.run_async(
        name="employees",
        source=PDF(path="path/to/pdf")
    )

.. note::
    The path to the PDF will be the remote path of the document uploaded to Structify. For more information on how to upload documents, see the :doc:`documents` section. Or you can check out the tutorials at :ref:`document-example`.




Text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For text, you can either input the text directly or use a path to a text file uploaded to Structify.

.. code-block:: python
    
    from structify.sources import Text

    structify.structure.run_async(
        dataset="employees", 
        source=Text(content="Jane Doe is the CEO of ACME. Previously she was the Senior VP at EMCA.")
    )

.. code-block:: python

    structify.structure.run_async(
        dataset="employees", 
        source=Text(path="path/to/text")
    )


SEC Filings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from structify.sources import SECFiling
        
    structify.structure.run_async(
        dataset="employees", 
        source=SECFiling(
            year=2021, # Optional
            quarter=3, # Optional
            accession_number="0000320193-21-000056" # Optional
        )
    )


DocumentImage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from structify.sources import DocumentImage

    structify.structure.run_async(
        dataset="employees", 
        source=DocumentImage(path="path/to/image")
    )


.. _view-dataset:

Viewing Your Datasets
---------------------------------------
Through this endpoint, we allow users to view either all entities or all the relationships in their dataset.

.. code-block:: python
    
    entities = structify.dataset.view(
        name="employees",
        requested_type="Entities" # The default value is "Entities", but we show it here for clarity
    )

    relationships = structify.dataset.view(
        name="employees",
        requested_type="Relationships"
    )

The output for each is an iterator which we can use to view the dataset as follows:

.. code-block:: python

    for entity in entities:
        print(entity)

    for relationship in relationships:
        print(relationship)

.. tip::
    
    To view a particular type of entity or relationship, you can add the ``table_name`` or ``relationship_name`` parameter to the respective view call.

.. note::
    Keep your eye out for the ``structify.datasets.refresh`` API call to update the data in your dataset.
