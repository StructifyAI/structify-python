Welcome to Structify!
=====================
We power you to collect, enrich, and update your own custom datasets using our AI agents, built and trained right here at Structify. 
Structify allows you transform any information from document to web page into structured data with as little as two API calls.

.. code-block:: python

   # First, define the schema of your dataset using our Python Objects
   table = Table(
      name="company",
      description="a private company that is interested in raising capital",
      properties=[
         Property(name="name", description="The name of the company"),
         Property(name="business_description", description="The description of the company"),
         Property(name="location", description="The location of the company"),
         Property(name="website", description="The website of the company", prop_type="URL"),
      ]
   )

   # Next, create a dataset with that schema
   structify.datasets.create(
      name="startups",
      description="A dataset of private companies that are interested in raising capital",
      tables=[table],
      relationships = []
   )

   # Then, create an agent to index information from defined sources for your dataset
   structify.structure.run_async(
      dataset="startups",
      source=SourceWeb(web=SourceWebWeb(starting_urls=["https://www.techcrunch.com/"])),
      save_requirement=[RequiredProperty(table_name="company", property_name="name")]
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
   Helpful Dataset Functionality <python_client/analysis>


Learn from Examples
-------------------
.. toctree::
   :caption: Tutorials
   :maxdepth: 1

   Grabbing Press about Clients <examples/example0>
   Tracking Board Member Changes <examples/example1>
   Structifying Pitch Decks <examples/example2>
   Making a Restaurant Menu Dataset <examples/example3>
   Tracking Pricing for Semiconductor Parts <examples/example4>


Schema Cookbook
-------------------
.. toctree::
   :caption: Schema Cookbook
   :maxdepth: 1

   Schema Guidance <schema_cookbook/schema_guidance>
   Financial Schema <schema_cookbook/financials_schema>
   E-Commerce <schema_cookbook/ecommerce_schema>
   Semiconductor Schema <schema_cookbook/semiconductor_schema>
   Clinical Trials Schema <schema_cookbook/clinical_trials_schema>


.. Indices and tables
.. -------------------
.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

Read More
---------
.. toctree::
   :caption: More
   :maxdepth: 1

   FAQ <more/faq>
