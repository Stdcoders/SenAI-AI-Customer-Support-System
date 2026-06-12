from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.email_repository import email_repository
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/api/status",
    tags=["Status"],
)


@router.get(
    "/{job_id}",
    response_model=APIResponse,
)
def get_status(
    job_id: int,
    db: Session = Depends(get_db),
):

    email = email_repository.get_by_id(
        db=db,
        object_id=job_id,
    )

    if email is None:

        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    return APIResponse(

        success=True,

        message="Job status fetched successfully",

        data={

            "job_id": email.id,

            "status": getattr(email, "status", "Processed"),

            "category": getattr(email, "category", None),

            "priority": getattr(email, "priority", None),

            "urgency": getattr(email, "urgency", None),

        },

    )