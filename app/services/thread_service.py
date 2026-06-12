from sqlalchemy.orm import Session

from app.models.thread import Thread
from app.repositories.thread_repository import thread_repository


class ThreadService:

    def get_or_create(
        self,
        db: Session,
        external_thread_id: str,
        subject: str,
        contact_id: int,
    ) -> Thread:

        thread = thread_repository.get_by_external_thread_id(
            db,
            external_thread_id,
        )

        if thread:
            return thread

        return thread_repository.create(
            db,
            external_thread_id=external_thread_id,
            subject=subject,
            contact_id=contact_id,
        )

    def get_history(
        self,
        db: Session,
        contact_email: str,
    ):

        thread = thread_repository.get_by_contact_email(
            db=db,
            contact_email=contact_email,
        )

        if thread is None:

            return {

                "tool": "thread_history",

                "email_count": 0,

                "history": [],

                "context": "",

            }

        emails = thread_repository.get_emails(
            db=db,
            thread_id=thread.id,
        )

        history = []

        for email in emails:

            history.append(

                {

                    "sender": email.sender,

                    "subject": email.subject,

                    "body": email.body,

                    "timestamp": str(email.timestamp),

                }

            )

        return {

            "tool": "thread_history",

            "thread_id": thread.id,

            "email_count": len(history),

            "history": history,

            "context": "\n\n".join(

                [

                    f"{item['timestamp']} | {item['sender']}: {item['body']}"

                    for item in history

                ]

            ),

        }


thread_service = ThreadService()