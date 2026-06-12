from sqlalchemy.orm import Session

from app.models import contact
from app.models.contact import Contact
from app.repositories.contact_repository import contact_repository


class ContactService:

    def get_or_create(
        self,
        db: Session,
        email: str,
        name: str | None = None,
        company: str | None = None,
    ) -> Contact:

        contact = contact_repository.get_by_email(db, email)

        if contact:
            return contact

        return contact_repository.create(
            db,
            email=email,
            name=name,
            company=company,
        )

    def get_profile(
        self,
        db: Session,
        email: str,
):

        contact = contact_repository.get_by_email(
        db,
        email,
    )

        if not contact:

            return {

            "tool": "contact_profile",

            "exists": False,

        }

        thread_count = contact_repository.get_thread_count(

        db,

        contact.id,

    )

        email_count = contact_repository.get_email_count(

        db,

        contact.id,

    )

        return {

        "tool": "contact_profile",

        "exists": True,

        "contact_id": contact.id,

        "email": contact.email,

        "name": contact.name,

        "company": contact.company,

        "total_threads": thread_count,

        "total_emails": email_count,

        "is_repeat_customer": email_count > 1,

        "is_vip": email_count >= 10,

        "context": (

            f"{email_count} previous emails "

            f"across {thread_count} thread(s)."

        ),

    }

contact_service = ContactService()