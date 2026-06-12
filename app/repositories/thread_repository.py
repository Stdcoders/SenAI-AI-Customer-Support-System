from sqlalchemy.orm import Session

from app.models.thread import Thread
from app.models.email import Email
from app.models.contact import Contact

from app.repositories.base_repository import BaseRepository


class ThreadRepository(BaseRepository[Thread]):

    def __init__(self):

        super().__init__(Thread)

    def get_by_external_thread_id(
        self,
        db: Session,
        thread_id: str,
    ):

        return (

            db.query(Thread)

            .filter(

                Thread.external_thread_id == thread_id

            )

            .first()

        )

    def get_emails(
        self,
        db: Session,
        thread_id: int,
    ):

        return (

            db.query(Email)

            .filter(

                Email.thread_id == thread_id

            )

            .order_by(

                Email.timestamp.asc()

            )

            .all()

        )

    def get_by_contact_email(
        self,
    db: Session,
    contact_email: str,
):

        return (

        db.query(Thread)

        .join(Thread.contact)

        .filter(

            Thread.contact.has(

                email=contact_email

            )

        )

        .first()

    )


thread_repository = ThreadRepository()