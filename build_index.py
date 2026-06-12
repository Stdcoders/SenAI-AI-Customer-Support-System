from app.services.rag_service import rag_service

count = rag_service.build_index()

print(f"Indexed {count} chunks")