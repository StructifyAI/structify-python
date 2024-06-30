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

Currently we also have a dependency on Azure, so you will want to pip install azure-core:

.. code-block:: bash

   pip install azure-core


Anytime you want to use the Structify Python library, you'll need to import it:

.. code-block:: python

   from structify import Structify


.. _Getting-An-API-Key:

Getting an API Key
------------------
We are early, so it is important to us to develop a relationship with all our users. That said, the quickest way to secure an API key is to `email us <mailto:team@structify.ai>`_ with your name, email, and a brief description of your use case. We will send you back an API key and your account details.

Alternatively, you can book a time for a detailed guided tour of our API and get an API key at the end of the session. Please find a time to meet via `our Calendly <https://calendly.com/ronakgandhi/structify-demo>`_.

Once you have your API key, you can use it to authenticate your requests to the Structify API. You can do this by setting the ``apiKey`` attribute of the client object:

.. code-block:: python

   structify = Structify(headers = {"apiKey": "your-api-key-here"})"

Our API recognizes two types of users: business and personal. Both have organizations and users underneath, for the case that you are letting users of your program make API calls through us. Every one of the endpoints is done through an authenticated personel.

.. _create-your-first-dataset:

Create Your First Dataset
-------------------------
You can create and fill a dataset with two quick successive API calls:

#. Define a schema using ``structify.dataset.create``.
#. Specify the source to populate the dataset from with ``structify.structure.run`` (or ``structify.structure.run_async``).

Here's an example of how you would make an API call to create a dataset:

.. code-block:: python
   
   from structify import Structify, Source, Table, Property, Relationship

   structify = Structify(headers = {"apiKey": "your-api-key-here"})

   # Define a schema as a JSON object, make sure to include descriptions for each of your tables, properties, and relationships

   tables = [
      Table(
         name = "author",
         description = "an individual who wrote a book",
         properties = [
            Property(name = "name", description = "The name of the author"),
            Property(name = "genre", description = "The genre that the author typically writes in")
         ],
         relationships = []
      ),
      Table(
         name = "publisher",
         description = "a company that publishes books",
         properties = [
            Property(name = "name", description = "The name of the publisher"),
            Property(name = "location", description = "The location of the publisher")
         ],
         relationships = []
      ),
      Table(
         name = "book",
         description = "a book that has been written",
         properties = [
            Property(name = "title", description = "The title of the book"),
            Property(name = "copies_sold", description = "The number of copies sold of the book")
         ],
         relationships = [
            Relationship(name = "authored_by", description = "Connects the book to the list of authors who wrote it"),
            Relationship(name = "published_by", description = "Connects the book to the list of publishers of the book")
         ]
      )
   ]

   # Use the schema to create the dataset
   structify.dataset.create(
      name = "books",
      description = "Create a dataset named 'books' that tells me about the authors and publishers of books.",
      schema = entities
   )

   # Specify the source to populate the dataset from the Source object and then populate the dataset with structify.structure.run
   source = Source.Web(
      prompt = "What are details about the books appearing here?",
      websites = ["https://www.goodreads.com/"]
   )

   books_dataset = structify.structure.run(name = "books", source = source)


With that, you are on your way to structifying your data.

.. note::
   We also allow users to asynchronously run agents to populate datasets. This is useful for large datasets that may take a long time to populate. You can use the ``structify.structure.run_async`` method to run an agent asynchronously.
