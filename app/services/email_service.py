from datetime import datetime

from sqlalchemy.orm import Session

from app.models.email import Email
from app.repositories.email_repository import email_repository
from app.schemas.email import EmailIngestRequest

from app.services.contact_service import contact_service
from app.services.thread_service import thread_service
from app.services.heuristic_service import heuristic_service
from app.services.classification_service import classification_service
from app.services.sentiment_service import sentiment_trend_service


class EmailService:

    def ingest(
        self,
        db: Session,
        payload: EmailIngestRequest,
    ) -> Email:

        # --------------------------------------------------
        # Deduplication
        # --------------------------------------------------

        existing = email_repository.get_by_message_id(
            db,
            payload.message_id,
        )

        if existing:
            return existing

        # --------------------------------------------------
        # Contact Resolution
        # --------------------------------------------------

        contact = contact_service.get_or_create(
            db,
            email=payload.sender,
        )

        # --------------------------------------------------
        # Thread Resolution
        # --------------------------------------------------

        thread = thread_service.get_or_create(
            db,
            external_thread_id=payload.thread_id,
            subject=payload.subject,
            contact_id=contact.id,
        )

        # --------------------------------------------------
        # Heuristic Intelligence Layer
        # --------------------------------------------------

        heuristics = heuristic_service.analyze(
            payload
        )

        # --------------------------------------------------
        # LLM Classification Layer
        # --------------------------------------------------

        classification = classification_service.classify(
            payload
        )

        # --------------------------------------------------
        # Sentiment Trend Layer
        # --------------------------------------------------

        sentiment_trend = sentiment_trend_service.analyze(
            [
                classification
            ]
        )

        # --------------------------------------------------
        # Email Persistence
        # --------------------------------------------------

        email = email_repository.create(
            db,
            external_message_id=payload.message_id,
            sender=payload.sender,
            subject=payload.subject,
            body=payload.body,
            timestamp=payload.timestamp or datetime.utcnow(),
            thread_id=thread.id,
        )

        return email


email_service = EmailService()
