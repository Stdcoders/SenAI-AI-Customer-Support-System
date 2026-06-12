from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.email_repository import email_repository
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/respond",
    tags=["Respond"],
)


@router.post(
    "/{email_id}",
    response_model=APIResponse,
)
def respond(
    email_id: int,
    db: Session = Depends(get_db),
):

    email = email_repository.get_by_id(
        db=db,
        object_id=email_id,
    )

    if email is None:

        raise HTTPException(
            status_code=404,
            detail="Email not found",
        )

    if hasattr(email, "status"):

        email.status = "Replied"

        db.add(email)

        db.commit()

        db.refresh(email)

    return APIResponse(

        success=True,

        message="Response approved and marked as replied",

        data={

            "email_id": email.id,

            "status": getattr(email, "status", "Replied"),

        },

    )