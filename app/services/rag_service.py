from app.rag.loader import knowledge_loader
from app.rag.chunk import semantic_chunker
from app.rag.retriever import retriever
from app.rag.vector_store import vector_store


class RAGService:
    """
    High-level interface for the RAG subsystem.

    Responsibilities
    ----------------
    - Build knowledge index
    - Load persisted index
    - Retrieve relevant knowledge
    - Format results for the autonomous agent
    """

    def build_index(self):

        documents = knowledge_loader.load_documents()

        chunks = []

        for document in documents:
            chunks.extend(
                semantic_chunker.chunk(
                    document
                )
            )

        vector_store.build(chunks)
        vector_store.save()

        return len(chunks)

    def load_index(self):

        vector_store.load()

    def search(
        self,
        query: str,
        top_k: int = 3,
    ):
        if isinstance(query, dict):
            query = (
                query.get("query")
                or query.get("text")
                or ""
            )
        query = str(query)
        if not isinstance(query, str,):
            query = str(query)

        results = retriever.retrieve(
            query=query,
            top_k=top_k,
        )

        formatted = []

        for result in results:

            chunk = result["chunk"]

            formatted.append(
                {
                    "score": round(result["score"], 4),
                    "source": chunk.source,
                    "section": chunk.section_title,
                    "policy_id": chunk.policy_id,
                    "content": chunk.text,
                }
            )

        confidence = 0.0

        if formatted:
            confidence = formatted[0]["score"]

        return {
            "tool": "rag_search",
            "query": query,
            "confidence": confidence,
            "documents": formatted,
            "context": "\n\n".join(
                [
                    item["content"]
                    for item in formatted
                ]
            ),
        }


rag_service = RAGService()