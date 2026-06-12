from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.response import APIResponse
from app.services.thread_service import thread_service

router = APIRouter(
    prefix="/threads",
    tags=["Threads"],
)


@router.get(
    "/{contact_email}",
    response_model=APIResponse,
)
def get_thread_history(
    contact_email: str,
    db: Session = Depends(get_db),
):

    result = thread_service.get_history(
        db=db,
        contact_email=contact_email,
    )

    return APIResponse(

        success=True,

        message="Thread history fetched successfully",

        data=result,

    )