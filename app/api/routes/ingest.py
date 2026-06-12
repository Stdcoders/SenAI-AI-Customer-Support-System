from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.email import EmailIngestRequest, EmailResponse
from app.schemas.response import APIResponse
from app.services.email_service import email_service

router = APIRouter(
    prefix="/api/ingest",
    tags=["Email Ingestion"],
)
@router.post(
    "/",
    response_model=APIResponse,
    status_code=202,
)
def ingest_email(
    payload: EmailIngestRequest,
    db: Session = Depends(get_db),
):

    email = email_service.ingest(
        db=db,
        payload=payload,
    )

    return APIResponse(
        success=True,
        message="Email ingested successfully",
        data=EmailResponse.model_validate(email),
    )