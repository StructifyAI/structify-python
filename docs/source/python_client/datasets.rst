Creating Datasets
=================

Overview
--------
Structify's API, at its core, is designed to let developers collect datasets on demand. You can create a dataset in just a few lines of code. This guide will walk you through the three main steps in getting your first custom dataset:

#. :ref:`define-schema`
#. :ref:`Populating-Datasets`
#. :ref:`view-dataset`
#. :ref:`Refreshing-Dataset`

.. _define-schema:

Defining Your Schema
---------------------
The basis of creating datasets is defining the schema, much like creating a blueprint for a database. The schema of a Structify dataset is comprised of entity tables, which are in turn made up of columns (which we call Properties), and the relationships between them. Check out the example code below for more clarity.

Before you can create researchers to automatically fill up your datasets, we need to define the schema of the dataset. Note that each entity table, column, and relationship in the dataset needs a name and description.

If you have a schmea you want your dataset to follow, you can easily pre-define your schema using our Python objects.

.. code-block:: python
    
        from structify import Structify, Table, Property, Relationship
        from pydantic import BaseModel
        from typing import List

        structify = Structify(headers = {"apiKey": {"your-api-key-here"})

        entities = [
            Table(
                name = "jobs",
                description = "the job history of the employee",
                properties = [
                    Property(name = "title", description = "The title of the job"),
                    Property(name = "company", description = "The company the employee worked for")
                ],
                relationships = []
            ),
            Table(
                name = "education",
                description = "the educational history of an employee",
                properties = [
                    Property(name = "school_name", description = "The name of the school"),
                    Property(name = "school_gradyear", description = "The year the employee graduated")
                ],
                relationships = []
            ),
            Table(
                name = "employees",
                description = "details about employees at a certain company.",
                properties = [
                    Property(name = "name", description = "the full name of the employee")
                ],
                relationships = [
                    Relationship(name = "job", description = "connects the employee to their job history"),
                    Relationship(name = "education", description = "connects the employee to their education history")
                ]
            )
        ]

        structify.dataset.create(
            name="employees", 
            description="A dataset named 'employees' that tells me about their job and education history.", 
            schema = entities
            )

        structify.dataset.info(name = "employees")

And the output will echo back a JSON representation of the schema you just created.

.. note::
   Coming soon: a ``structify.dataset.llm_create`` method to create a dataset with a schema that is automatically generated from just a description.
   This will allow users to, instead of writing out an entire schema, simply input plain text to allow the LLM to create your schema.

.. tip::
    Currently, if you need to edit the schema, you will need to either delete the dataset and recreate it with the edited schema or create a dataset with a new name.
    
    We are working on ``structify.dataset.modify`` to allow users to adjust the schema without deleting an existing dataset.

.. warning::
    As of now, the every property in the schema has a default type as a String. We're working quickly to allow users to specify types for each property such an integers or lists.

.. _populating-datasets:

Populating Your Datasets
------------------------
Once you have blueprinted your dataset by creating a schema, you can now use Structify's research agents to collect data to fill your dataset.

You can run our scraper agents either through ``structify.structure.run`` or ``structify.structure.run_async`` to populate a dataset with an initial batch of data. The structure API call requires the following:

- **name:** The name of the dataset you want to populate
- **source:** The sources or types of sources you want the agent to use (e.g. “LinkedIn” or “news articles”). These will be a Python enum of the sources available to the agent. Make sure to import Source. If not specified, the API call will error out.

Here's an example of an API call to populate that employees dataset with data from LinkedIn using ``structify.structure.run``:

.. code-block:: python

    from structify import Structify, Source

    structify.structure.run(
        name = "employees", 
        sources = Source.Web(prompt = "find me details about the employees of ACME", websites = ["linkedin.com"])
    )
   


.. note::
    The output of ``structify.structure.run`` will be a JSON representation of the dataset.

If you want to run the populate request asynchronously, you can use ``structify.structure.run_async``:

.. code-block:: python
    
        from structify import Structify, Source
    
        dataset = structify.structure.run_async(
            name = "employees", 
            sources = Source.Web(prompt = "find me details about the employees of ACME", websites = ["linkedin.com"])
        )

        structify.structure.wait([dataset])

.. note::
    The output of ``structify.structure.run_async`` will be a key that you can use to access the run via ``structify.structure.wait``. We are working on adding an endpoint that will allow you to check the status on an asynchronous run.



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



