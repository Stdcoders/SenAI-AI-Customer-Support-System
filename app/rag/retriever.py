from app.rag.vector_store import vector_store


class Retriever:
    """
    Retrieves the most relevant knowledge chunks.

    Responsibilities

    - execute vector search
    - remove duplicate chunks
    - diversify sources
    - return top_k results
    """

    def retrieve(
        self,
        query: str,
        top_k: int = 3,
    ):

        # retrieve more than required for reranking
        candidates = vector_store.search(
            query=query,
            top_k=max(top_k * 3, 10),
        )

        seen = set()

        results = []

        for candidate in candidates:

            chunk = candidate["chunk"]

            key = (
                chunk.source,
                chunk.policy_id,
                chunk.chunk_index,
            )

            if key in seen:
                continue

            seen.add(key)

            results.append(candidate)

            if len(results) >= top_k:
                break

        return results


retriever = Retriever()