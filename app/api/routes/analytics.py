from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.repositories.email_repository import email_repository
from app.schemas.response import APIResponse
from app.services.sentiment_service import (
    sentiment_trend_service,
)
from datetime import datetime, timedelta

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/sentiment-trend",
    response_model=APIResponse,
)
def sentiment_trend(
    sender: str,
    days: int = 30,
    db: Session = Depends(get_db),
):

    emails = email_repository.get_by_sender(
        db=db,
        sender=sender,
    )
    cutoff = datetime.utcnow() - timedelta(days=days)
    emails = [email for email in emails if email.timestamp >= cutoff]

    classifications = [

        {
            "sentiment_score": email.sentiment_score,
        }

        for email in emails

    ]

    result = sentiment_trend_service.analyze(
        classifications,
    )

    return APIResponse(

        success=True,

        message="Sentiment trend fetched successfully",

        data=result,

    )


@router.get(
    "/category-breakdown",
    response_model=APIResponse,
)
def category_breakdown(
    db: Session = Depends(get_db),
):

    
    result = email_repository.category_breakdown(
        db=db,
    )

    return APIResponse(

        success=True,

        message="Category breakdown fetched successfully",

        data=result,

    )