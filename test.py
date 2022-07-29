from docarray import DocumentArray, Document
from executor import UriDownloader

ex = UriDownloader()

docs = DocumentArray(
    [
        Document(uri="https://arxiv.org/pdf/1809.09600.pdf")
    ]
)

ex.download_uri(docs)

for doc in docs:
    print(doc.uri)
    print(doc.blob)
