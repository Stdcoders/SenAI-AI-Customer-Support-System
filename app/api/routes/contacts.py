from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.contact_repository import contact_repository
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/contacts",
    tags=["Contacts"],
)


@router.get(
    "/{email}",
    response_model=APIResponse,
)
def get_contact(
    email: str,
    db: Session = Depends(get_db),
):

    contact = contact_repository.get_by_email(
        db=db,
        email=email,
    )

    if contact is None:

        raise HTTPException(
            status_code=404,
            detail="Contact not found",
        )

    total_threads = contact_repository.get_thread_count(
        db=db,
        contact_id=contact.id,
    )

    total_emails = contact_repository.get_email_count(
        db=db,
        contact_id=contact.id,
    )

    return APIResponse(

        success=True,

        message="Contact fetched successfully",

        data={

            "id": contact.id,

            "email": contact.email,

            "name": contact.name,

            "company": contact.company,

            "total_threads": total_threads,

            "total_emails": total_emails,

        },

    )


@router.patch(
    "/{email}/status",
    response_model=APIResponse,
)
def update_status(
    email: str,
    status: str,
    db: Session = Depends(get_db),
):

    contact = contact_repository.get_by_email(
        db=db,
        email=email,
    )

    if contact is None:

        raise HTTPException(
            status_code=404,
            detail="Contact not found",
        )

    VALID_STATUS = {

        "VIP",

        "Blocked",

        "Active",

        "Churned",

    }

    if status not in VALID_STATUS:

        raise HTTPException(

            status_code=400,

            detail="Invalid contact status",

        )

    return APIResponse(

        success=True,

        message="Contact status updated",

        data={

            "id": contact.id,

            "email": contact.email,

            "name": contact.name,

            "company": contact.company,

            "status": status,

        },

    )