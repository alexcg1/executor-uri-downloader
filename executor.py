from jina import Executor, DocumentArray, requests
import requests as rq


class UriDownloader(Executor):
    @requests
    def download_uri(self, docs: DocumentArray, **kwargs):
        for doc in docs:
            if doc.uri:
                if doc.uri.startswith("http"):
                    r = rq.get(doc.uri, allow_redirects=True)
                    doc.blob = r.content
