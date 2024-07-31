Using Documents in Structify
============================
In many cases, a wealth of unstructured data lies within documents without set formats. Structify allows you to upload these documents and extract the data you need from them.

Uploading Documents
---------------------
You can upload documents to Structify using ``structify.documents.upload`` by passing the file in binary mode. You will also need to specify the path you want to store the document on your Structify account, along with the type of document. 

.. code-block:: python

    from structify import Structify
    structify = Structify(api_key="your-api-key-here")

    file = "/path/to/your/document.pdf"

    client.documents.upload(
        content=open(file, "rb").read(),
        path=b"/path/on/your/Structify/remote.pdf",
        file_type="PDF"
    )

Currently, we support the following document formats:

- PDFs
- Text files (TXT, CSV, etc.)
- Images (JPG, PNG, etc.)

We are working to support more formats in the future, such as:

- Word documents (DOCX)
- Excel spreadsheets (XLSX)
- PowerPoint presentations (PPTX)

In the meantime, we recommend converting all your documents to either PDFs or images before uploading them to Structify.
With the DocumentImage structuring endpoint (read more about it in the :doc:`structuring` section), you can extract data from any document type after converting it to an image.

Once you've uploaded them, you can use our other document endpoints to list, download, and delete the documents.

Here are examples of how you would use those endpoints:

.. code-block:: python

    # Listing all documents will return a JSON object of all your uploaded documents
    structify.documents.list()

    # Download a document by specifying the name of the document. This will return the document in binary mode, which we can save to your local machine.
    document = structify.documents.download(path='/path/on/your/Structify/remote.pdf')
    open("downloaded_document.pdf", "wb").write(document.read())

    # Delete a document by specifying the name of the document. This will remove the document from your Structify account.
    structify.documents.delete(path='/path/on/your/Structify/remote.pdf')


.. _Structuring Documents:

Extracting Data from Documents
-------------------------------
Creating datasets from documents is quite simple. You just use the ``structify.structure.run`` or ``structify.structure.run_async`` method and specify the document file path or paths you want to include in the dataset through the relevant Python object.

.. code-block:: python

    from structify.sources import DocumentImage

    structify.structure.run_async(
        dataset="startups", 
        source=DocumentImage(path = "/pitchdecks/structify_deck.pdf")
    )

And just like that you've created a dataset from your documents. 