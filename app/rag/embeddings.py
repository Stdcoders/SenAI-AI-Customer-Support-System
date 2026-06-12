from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingService:
    """
    Generates dense vector embeddings for RAG.

    Model:
        sentence-transformers/all-MiniLM-L6-v2

    Output:
        384-dimensional normalized vectors
    """

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed(
        self,
        text: str,
    ) -> np.ndarray:

        embedding = self.model.encode(

            text,

            normalize_embeddings=True,

            convert_to_numpy=True,

        )

        return embedding

    def embed_many(
        self,
        texts: list[str],
    ) -> np.ndarray:

        embeddings = self.model.encode(

            texts,

            normalize_embeddings=True,

            convert_to_numpy=True,

        )

        return embeddings

    @property
    def dimension(self):

        return self.model.get_sentence_embedding_dimension()


embedding_service = EmbeddingService()