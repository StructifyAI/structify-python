Welcome to Structify!
=====================
We power you to collect, enrich, and update your own custom datasets using our AI agents, built and trained right here at Structify. 
Structify allows you transform any information from document to web page into structured data with as little as two API calls.

.. code-block:: python

   # First, define the schema of your dataset using our Python Objects
   tables = Table(
      name="person",
      description="an individual in my professional network",
      properties=[
         Property(name="name", description="The name of the person"),
         Property(name="job_title", description="The title the person holds")
      ]
   )

   # Next, create a dataset with that schema
   structify.datasets.create(
      name="my_network",
      description="A dataset of people in my professional network",
      tables=[tables],
      relationships = []
   )

   # Then, create an agent to index information from defined sources for your dataset
   structify.structure.run_async(
      name="my_network",
      source={"web_search": {"starting_urls": ["linkedin.com"]}},
   )



After reading our API documentation, you will be able to use our Python client to do things like:

* Create a personalized dataset representing the job history of everyone in your network
* Monitor changes in a continuously updating dataset of real estate listings
* Extract structured data about startup financing events from a collection of SEC filings and pitch decks
* Automate notifications when a new job listing is posted that matches your criteria

Keep reading to learn more about how to use Structify to supercharge your team or an AI tool.

Get Started with Structify
--------------------------
.. toctree::
   :caption: Get Started
   :maxdepth: 1

   Overview <get_started/overview>
   Intro <get_started/intro>
   Quickstart <get_started/quickstart>


Check Out Our Capabilities
--------------------------
.. toctree::
   :caption: Guide
   :maxdepth: 1

   Creating Datasets <python_client/datasets>
   Structuring Data <python_client/structuring>
   Planning Agent Jobs <python_client/planning>
   Viewing Datasets <python_client/viewing>
   Using Documents <python_client/documents>
   Getting Sources <python_client/backsourcing>


Learn from Examples
-------------------
.. toctree::
   :caption: Tutorials
   :maxdepth: 1

   Grabbing Press about Clients <examples/example0>
   Tracking Board Member Changes <examples/example1>
   Structifying Pitch Decks <examples/example2>
   Creating a Dataset for Your Network <examples/example3>


.. Indices and tables
.. -------------------
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

See What's Coming Soon
-------------------------
.. toctree::
   :caption: In Beta
   :maxdepth: 1

   Analytical Capabilities <coming_soon/analysis>
   Searching through Datasets <coming_soon/search>
   Sharing Datasets <coming_soon/sharing>

Read More
---------
.. toctree::
   :caption: More
   :maxdepth: 1

   FAQ <more/faq>
