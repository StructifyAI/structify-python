.. _quickstart:

Quickstart Guide
================
Datasets on demand for you or your AI tool in three easy steps.

#. :ref:`Installation`
#. :ref:`Getting-An-API-Key`
#. :ref:`create-your-first-dataset`

Our documentation will guide you through the process of using the Structify API to access, create, and manipulate your data.
When you create a dataset, Structify spins up AI agents to populate your custom schema by indexing information from the sources you specify. Soon, you will see how much fun it is to "structify" your data. 
We have a python client library, and we are working on releasing a Rest API.

.. _Installation:

Installation
------------

Let's get started!

First, install the python client library using pip:

.. code-block:: bash

   pip install structifyai


Running ``pip list`` after it completes will show you the Python libraries you've got, which will let you know if the Structify Python library was successfully installed.

.. note::
   We constantly push new updates so make sure to check for the latest version of the Structify Python library by running ``pip install structifyai --upgrade``.


Anytime you want to use the Structify Python library, you'll need to import it:

.. code-block:: python

   from structify import Structify


.. _Getting-An-API-Key:

Getting an API Key
------------------
We are early, so it is important to us to develop a relationship with all our users. That said, the quickest way to secure an API key is to `email us <mailto:team@structify.ai>`_ with your name, email, and a brief description of your use case. We will send you back an API key and your account details.

Alternatively, you can book a time for a detailed guided tour of our API and get an API key at the end of the session. Please find a time to meet `here <https://calendly.com/ronakgandhi/structify-demo>`_.

Once you have your API key, you can use it to authenticate your requests to the Structify API. You can do this by setting the ``api_key`` attribute of the client object:

.. code-block:: python

   structify = Structify(api_key="your_api_key")

We recommend setting the ``api_key`` attribute of the client object as an environment variable:

.. code-block:: bash

   export STRUCTIFY_API_TOKEN="your_api_key"


.. _create-your-first-dataset:

Create Your First Dataset
-------------------------
You can create and fill a dataset with two quick successive API calls:

#. Define a schema using ``structify.datasets.create``.
#. Add some starting entities using ``structify.entities.add`` that we want to enrich.
#. Specify the source to populate the dataset from with ``structify.structure.enhance_property`` and ``structify.structure.enhance_relationship``.

Here's an example of how you would make an API call to create a dataset:

.. code-block:: python
   
   from structify import Structify
   from structify.types import KnowledgeGraphParam, EntityParam
   from structify.types.dataset_descriptor import Relationship
   from structify.types.table import Table, Property

   structify = Structify()

   # Define a schema using our Python Objects, make sure to include descriptions for each of your tables, properties, and relationships

   tables = [
      Table(
         name="author",
         description="an individual who wrote a book",
         properties=[
            Property(name="name", description="The name of the author"),
            Property(name="genre", description="The genre that the author typically writes in")
         ]
      ),
      Table(
         name="book",
         description="a book that has been written",
         properties=[
            Property(name="title", description="The title of the book"),
            Property(name="copies_sold", description="The number of copies sold of the book")
         ],
      )
   ]

   relationships = [
      Relationship(
         name= "authored_by",
         description="Connects the book to the list of authors who wrote it",
         source_table="book",
         target_table="author"
         )
   ]

   # Use the schema to create the dataset
   structify.datasets.create(
      name="books",
      description="Create a dataset named 'books' that tells me about the authors and publishers of books.",
      tables=tables,
      relationships=relationships
   )


   # Add some initial authors to the dataset
   for author in ["J.K. Rowling", "Stephen King", "Harper Lee"]:
      structify.entities.add(
         dataset="books",
         kg=KnowledgeGraphParam(
            entities=[EntityParam(id=0, type="author", properties={"name": author})]
         )
      )

   # Now, use the enhance_property and enhance_relationship methods to populate the dataset
   for author in structify.datasets.view_table(dataset="books", table="author"):
      structify.structure.enhance_property(
         entity_id=author.id,
         property_name="genre",
      )
      structify.structure.enhance_relationship(
         entity_id=author.id,
         relationship_name="authored_by",
      )


With that, you are on your way to structifying your data.
