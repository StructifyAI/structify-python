Using Documents in Structify
============================
In many cases, a wealth of unstructured data lies within documents without set formats. Structify allows you to upload these documents and extract the data you need from them.

Uploading Documents
---------------------
You can upload documents to Structify using ``structify.documents.upload`` by passing the file in binary mode. You will also need to specify the path you want to store the document on your Structify account, along with the type of document. 

.. code-block:: python

    from structify import Structify
    structify = Structify(headers = {"apiKey": "your-api-key-here"})

    with open('/path/to/your/local/file.pdf', 'rb') as f:
        structify.documents.upload(f, path = '/path/on/your/Structify/remote.pdf', doctype = 'Pdf')

Currently, we support the following document formats:

- PDFs
- Text files (TXT, CSV, etc.)

We are working to support more formats in the future, such as:

- Images (JPG, PNG, etc.)
- Word documents (DOCX)
- Excel spreadsheets (XLSX)
- PowerPoint presentations (PPTX)

In the meantime, we recommend converting all your documents to either PDFs or text files before uploading them to Structify.

Once you've uploaded them, you can use our other document endpoints to list, download, and delete the documents.

Here are examples of how you would use those endpoints:

.. code-block:: python

    # Listing all documents will return a JSON object of all your uploaded documents
    structify.documents.list()

    # Download and view a document. Note that you will need to convert the download from vectors of bytes to text.
    import io
    print(io.BytesIO(bytes(client.documents.download(path = '/path/on/your/Structify/remote.pdf'))).read().decode())

    # Delete a document by specifying the name of the document. This will remove the document from your Structify account.
    structify.documents.delete(path = '/path/on/your/Structify/remote.pdf')


.. _Structuring Documents:

Extracting Data from Documents
-------------------------------
Creating datasets from documents is quite simple. You just use the ``structify.structure.run`` or ``structify.structure.run_async`` method and specify the document file path or paths you want to include in the dataset through the Source python object.

.. code-block:: python

    from structify import Structify, Source
    structify = Structify(headers = {"apiKey": "your-api-key-here"})

    structify.structure.run(
        name = "startups", 
        source = Source.Document(
            prompt = "structure data from this startup's pitch deck",
            path = "/pitchdecks/structify_deck.pdf"
            )
    )

And just like that you've created a dataset from your documents. 