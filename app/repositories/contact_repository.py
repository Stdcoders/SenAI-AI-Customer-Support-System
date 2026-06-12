from sqlalchemy.orm import Session

from app.models.contact import Contact
from app.repositories.base_repository import BaseRepository
from app.models.thread import Thread
from app.models.email import Email

class ContactRepository(BaseRepository[Contact]):

    def __init__(self):

        super().__init__(Contact)

    def get_by_email(
        self,
        db: Session,
        email: str,
    ):

        return (

            db.query(Contact)

            .filter(self.model.email == email, )

            .first()

        )
    def get_thread_count(
        self,
        db: Session,
        contact_id: int,
):

        return (

        db.query(Thread)

        .filter(

            Thread.contact_id == contact_id

        )

        .count()

    )


    def get_email_count(
        self,
        db: Session,
        contact_id: int,
):

        return (

        db.query(Email)

        .join(

            Thread,

            Email.thread_id == Thread.id,

        )

        .filter(

            Thread.contact_id == contact_id,

        )

        .count()

    )


contact_repository = ContactRepository()