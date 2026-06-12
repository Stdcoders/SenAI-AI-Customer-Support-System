from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.email_repository import email_repository
from app.agents.agent_service import agent_service
from app.schemas.response import APIResponse

router = APIRouter(
    prefix="/agent",
    tags=["Agent"],
)

@router.post(
    "/dry-run/{email_id}",
    response_model=APIResponse,
)
def dry_run(
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

    result = agent_service.invoke(

        query=email.body,

        dry_run=True,

    )

    return APIResponse(

        success=True,

        message="Dry run completed successfully",

        data=result,

    )