from pathlib import Path
import pickle

import faiss
import numpy as np

from app.rag.chunk import Chunk
from app.rag.embeddings import embedding_service


class VectorStore:
    """
    FAISS vector store for knowledge retrieval.

    Responsibilities

    - build index
    - save index
    - load index
    - search
    """

    def __init__(self):

        self.dimension = embedding_service.dimension

        self.index = faiss.IndexFlatIP(
            self.dimension
        )

        self.metadata: list[Chunk] = []

    def build(
        self,
        chunks: list[Chunk],
    ):
        self.index = faiss.IndexFlatIP(
            self.dimension
        )

        self.metadata = chunks

        vectors = embedding_service.embed_many(

            [chunk.text for chunk in chunks]

        )

        vectors = np.asarray(
            vectors,
            dtype=np.float32,
        )

        self.index.add(vectors)

    def save(

        self,

        index_path: str = "storage/knowledge.index",

        metadata_path: str = "storage/knowledge_metadata.pkl",

    ):

        Path(index_path).parent.mkdir(

            parents=True,

            exist_ok=True,

        )

        faiss.write_index(

            self.index,

            index_path,

        )

        with open(

            metadata_path,

            "wb",

        ) as file:

            pickle.dump(

                self.metadata,

                file,

            )

    def load(

        self,

        index_path: str = "storage/knowledge.index",

        metadata_path: str = "storage/knowledge_metadata.pkl",

    ):

        self.index = faiss.read_index(

            index_path,

        )

        with open(

            metadata_path,

            "rb",

        ) as file:

            self.metadata = pickle.load(

                file,

            )

    def search(

        self,

        query: str,

        top_k: int = 3,

    ):

        query_embedding = embedding_service.embed(

            query,

        )

        query_embedding = np.asarray(

            [query_embedding],

            dtype=np.float32,

        )

        scores, indices = self.index.search(

            query_embedding,

            top_k,

        )

        results = []

        for score, index in zip(

            scores[0],

            indices[0],

        ):

            if index == -1:

                continue

            results.append(

                {

                    "score": float(score),

                    "chunk": self.metadata[index],

                }

            )

        return results

    def rebuild(

        self,

        chunks: list[Chunk],

    ):

        self.index = faiss.IndexFlatIP(

            self.dimension

        )

        self.build(

            chunks,

        )


vector_store = VectorStore()