from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.email_repository import email_repository
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/stats",
    response_model=APIResponse,
)
def dashboard_stats(
    db: Session = Depends(get_db),
):

    stats = email_repository.get_dashboard_stats(
        db=db,
    )

    return APIResponse(

        success=True,

        message="Dashboard statistics fetched successfully",

        data=stats,

    )