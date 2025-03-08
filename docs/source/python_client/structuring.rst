Structuring Data
================
The main functionality of the Structify API lies in structuring information from a variety of sources on demand.
Our structuring endpoints allow you to direct our research agents to collect data from the web, PDFs, and more to either enhance existing entities in your dataset or populate your dataset from scratch with structured information.

.. _enhancing-datasets:

Enhancing Information
------------------------
Once you have blueprinted your dataset by creating a schema and added some initial entities to it manually, you can use Structify's AI agents to find the missing information in your dataset.

You can either enhance the entities you've added through ``client.structure.enhance_property`` or ``client.structure.enhance_relationship``.

- **entity_id:** *(required)* The ID of the entity you want to enhance
- **property_name:** *(required)* The name of the property you want to enhance (only used for ``enhance_property``)
- **relationship_name:** *(required)* The name of the relationship you want to enhance (only used for ``enhance_relationship``)
- **starting_websites:** *(optional)* The websites you want the agent to start navigating from, if you have any specific websites in mind
- **starting_searches:** *(optional)* The search queries you want the agent to start searching from, if you have any specific searches you want to start with
- **allow_extra_entities:** *(optional)* Whether you want the agent to add new entities to the dataset (in the case of ``enhance_relationship``, setting this to ``True`` will allow the agent to add new entities to the dataset that are outside the specified relationship)

Here's an example of how you'd enhance missing information for entities in your dataset:

.. code-block:: python

    for entity in client.datasets.view_table(dataset="employees", name="employee"):
        client.structure.enhance_property(
            entity_id=entity.id,
            property_name="job_title",
            starting_searches=[f"{entity.properties.get("name")} linkedin"]
        )
        client.structure.enhance_relationship(
            entity_id=entity.id,
            relationship_name="education",
        )

.. note::
    The output of ``client.structure.enhance_property`` and ``client.structure.enhance_relationship`` will be a job ID that you can use to access the job and view its status via ``client.structure.job_status``.

We also have a  ``client.structure.find_relationship`` endpoint that allows you to find if a relationship exists between two entities.
Instead of taking in a single entity id, it takes in two entity ids (``source_entity_id`` and ``target_entity_id``).

Here's an example of how you'd use ``client.structure.find_relationship`` to see if employees went to a certain set of universities:

.. code-block:: python

    for school in ["Yale", "Harvey-Mudd", "Princeton"]:
        client.entities.add(
            dataset="employees",
            entity_graph=KnowledgeGraphParam(
                entities=[
                    EntityParam(
                        id=0,
                        type="university",
                        properties={"name": school}
                    )
                ]
            )
        )

    for employee in client.datasets.view_table(dataset="employees", name="employee"):
        for university in client.datasets.view_table(dataset="employees", name="university"):
            client.structure.find_relationship(
                source_entity_id=employee.id,
                target_entity_id=university.id,
                relationship_name="education",
            )


.. _populating-datasets:

Populating Your Datasets
------------------------
To populate your dataset with more control, you can run our agents through ``client.structure.run_async`` to populate a dataset with an initial batch of data. 
The ``client.structure.run_async`` API call takes the following arguments:

- **name:** *(required)* The name of the dataset you want to populate
- **source:** *(required)* The source you want the agent to use to extract data from. More on this in :ref:`source-types`
- **save_requirement:** *(required)* The criteria you want the agent to use to extract data from the source. More on this in :ref:`save-requirement`

This API endpoint allows the user to have more finetune control over the agent, and allows them to specify the sources and criteria for the agent to extract data from the source.

.. code-block:: python

    from structify.types.save_requirement import RequiredEntity, RequiredProperty, RequiredRelationship
    from structify.types.structure_run_async_params import SourceWeb, SourceWebWeb

    job_id = client.structure.run_async(
        name="employees", 
        source=SourceWeb(
            SourceWebWeb(
                starting_urls=["linkedin.com"]
            )
        ),
        save_requirement=[RequiredEntity(seeded_entity_id=0)],
    )

    client.structure.job_status(job=[job_id])

.. note::
    The output of ``client.structure.run_async`` will be a Job ID that you can use to access the run and view its status via ``client.structure.job_status``.


.. _save-requirement:

Save Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Save Requirements are a way to specify what you want the agent to extract from the source. 
It provides our agents with guidance as to the specific entities, properties, or relationships that need to appear for it to extract data to populate your dataset.
If not specified, the default value will be an empty list, meaning the agent will extract any data from the provided source that is present in the schema.
There are three types of save requirements that you can specify:

**RequiredEntity**
In the case that you want to get data about a specific entity, you can specify the entity you want to extract.
This save requirement does necessitate that you input the entity into the run or run_async call as follows:

.. code-block:: python

    from structify.types import KnowledgeGraphParam, EntityParam

    client.structure.run_async(
        name="employees", 
        source=SourceWeb(
            SourceWebWeb(
                starting_urls=["linkedin.com"]
            )
        ),
        save_requirement=[RequiredEntity(seeded_entity_id=0)],
        seeded_entity=KnowledgeGraphParam(
            entities=[EntityParam(
                id=0,
                type="employee",
                properties={"name": "Jane Doe"}
            )],
            relationships=[]
        )
    )
    
.. note::
    The ID you specify in the save requirement must match the id of the starting_entity.

.. tip::
    If the entity already exists in your dataset, you could set the save requirement to ``[RequiredEntity(entity_id=entity.id)]`` to ensure that the agent adds info to the existing entity.

**RequiredProperty**
In the case that you want to require that a certain property be present for a table before extracting data, you can use the ``RequiredProperty`` save requirement.

.. code-block:: python

    client.structure.run_async(
        name="employees", 
        source=SourceWeb(
            SourceWebWeb(
                starting_urls=["linkedin.com"]
            )
        ),
        save_requirement=[RequiredProperty(table_name="job", property_names=["title", "company"])]
    )

.. note::
    The agent will extract data if at least one of the specified properties are present.

**RequiredRelationship**
In the case that you want to require that a certain relationship be present for a table before extracting data, you can use the ``RequiredRelationship`` save requirement.

.. code-block:: python

    client.structure.run_async(
        name="employees",
        source=SourceWeb(
            SourceWebWeb(
                starting_urls=["linkedin.com"]
            )
        ),
        save_requirement=[RequiredRelationship(relationship_name="worked_at")]
    )

You can input multiple save requirement to ensure a set of conditions are met before saving data.

.. _source-types:

Sources
-----------------------
You can use a variety of sources to populate your datasets such as:

- **Web**: Our AI agents can navigate the Web and structure data at scale. This is our bread and butter.
- **PDF**: We can also extract unstructured data from PDFs.
- **DocumentImage**: We support any other document types through this endpoint (which is used via the same API calls as PDFs). It does require users to convert their documents into images first.

Below are some examples of how you can start structuring runs on each source:

Web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    client.structure.run_async(
        name="employees", 
        source=SourceWeb(
            SourceWebWeb(
                starting_urls=["linkedin.com"]
            )
        ),
        save_requirement=[RequiredEntity(seeded_entity_id=0)],
        seeded_entity=KnowledgeGraphParam(
            entities=[EntityParam(
                id=0,
                type="employee",
                properties={"name": "Jane Doe"}
            )],
            relationships=[]
        )
    )
PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from structify.types.structure_run_async_params import SourcePdf, SourcePdfPdf

    client.structure.run_async(
        name="employees",
        source=SourcePdf(pdf=SourcePdfPdf(path="path/to/pdf")),
        save_requirement=[RequiredRelationship(relationship_name="education")],
    )

.. note::
    The path to the PDF will be the remote path of the document uploaded to Structify. For more information on how to upload documents, see the :doc:`documents` section. Or you can check out the tutorials at :ref:`document-example`.

.. _tracking-jobs:

Tracking Jobs
-----------------------
When you run our agent using ``enhance_property``, ``enhance_relationship``, or ``run_async``, it creates jobs that you can track using the jobs endpoints.
These endpoints allow you to monitor the progress of your structuring tasks and manage them as needed.

Listing Jobs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You can list all jobs using ``client.jobs.list()``. This endpoint supports several optional filtering arguments:

- **dataset_name:** Filter jobs by dataset
- **status:** Filter by job status ("Queued", "Running", "Completed", "Failed")
- **since:** List jobs since a specific timestamp
- **limit:** Maximum number of jobs to return
- **offset:** Number of jobs to skip for pagination

.. code-block:: python

    # List all running jobs for a specific dataset
    jobs = client.jobs.list(
        dataset_name="employees",
        status="Running"
    )

    # List recently completed jobs
    from datetime import datetime, timedelta

    yesterday = datetime.now() - timedelta(days=1)
    recent_jobs = client.jobs.list(
        since=yesterday,
        status="Completed"
    )

Getting Job Details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To get detailed information about a specific job, use ``client.jobs.get()``:

.. code-block:: python

    # Get details for a specific job
    job_details = client.jobs.get(job_id="Job-12345678-abcd-efgh-ijkl-987654321")

The response will be a Job object that contains the following information:

- **id:** The ID of the job
- **status:** The status of the job ("Queued", "Running", "Completed", "Failed")
- **created_at:** The timestamp when the job was created
- **run_started_time:** The timestamp when the job began running
- **message:** A debugging log of the job
