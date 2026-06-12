from fastapi import APIRouter, Query
from app.schemas.response import APIResponse
from app.services.rag_service import rag_service

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)


@router.get(
    "/search",
    response_model=APIResponse,
)
def search(
    q: str = Query(...),
):

    result = rag_service.search(q)

    return APIResponse(

        success=True,

        message="Knowledge search completed",

        data=result,

    )