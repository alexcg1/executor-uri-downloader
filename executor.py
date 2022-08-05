from jina import Executor, DocumentArray, requests
import requests as rq


class UriDownloader(Executor):
    @requests
    def download_uri(self, docs: DocumentArray, **kwargs):
        for doc in docs:
            if doc.uri:
                if doc.uri.startswith("http"):
                    try:
                        r = rq.get(doc.uri, allow_redirects=True)
                        if r.status_code == 200:
                            doc.blob = r.content
                        else:
                            print(f"UriDownloader: Failed to download {doc.uri} - status code {r.status_code}")
                    except:
                        print(f"UriDownloader: Failed to download {doc.uri}")
