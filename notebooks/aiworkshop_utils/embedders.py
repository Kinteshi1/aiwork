import requests

class OllamaEmbedder:
    def __init__(self, url, model_name):
        self.url = url
        self.model_name = model_name

    def _post_request(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        
        response = requests.post(
            self.url,
            json={
                "model": self.model_name,
                "input": texts
            }
        )
        return response.json()

    def get_embeddings(self, texts):
        response = self._post_request(texts)
        embeddings = response["embeddings"]
        if isinstance(texts, str) or len(embeddings) == 1:
            return embeddings[0]
        return embeddings

    def get_full_response(self, texts):
        return self._post_request(texts)


class OpenaisdkEmbedder:
    def __init__(self, client, model_name):
        self.client = client
        self.model_name = model_name

    def _post_request(self, texts):
        if isinstance(texts, str):
            texts = [texts]
        
        response = self.client.embeddings.create(
            model=self.model_name,
            input=texts,
            encoding_format="float"
        )
        return response

    def get_embeddings(self, texts):
        response = self._post_request(texts)
        embeddings = [data_item.embedding for data_item in response.data]
        if isinstance(texts, str) or len(embeddings) == 1:
            return embeddings[0]
        return embeddings

    def get_full_response(self, texts):
        return self._post_request(texts)