from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.email import Email
from app.repositories.base_repository import BaseRepository
from app.models.ai_classification import AIClassification
from sqlalchemy import func

class EmailRepository(BaseRepository[Email]):

    def __init__(self):

        super().__init__(Email)

    def get_by_message_id(
        self,
        db: Session,
        message_id: str,
    ):

        return (

            db.query(Email)

            .filter(
                Email.external_message_id == message_id
            )

            .first()

        )
    def get_by_sender(self, db, sender: str):
        return (
            db.query(self.model)
            .filter(self.model.sender == sender)
            .order_by(self.model.timestamp.asc())
            .all()
        )

    def category_breakdown(self, db, ):
        rows = ( db.query(

            AIClassification.category,

            func.count(AIClassification.id),

        )

        .group_by(

            AIClassification.category,

        ))
        return [

        {

            "category": category,

            "count": count,

        }

        for category, count in rows

    ]
    
    from sqlalchemy import func


    def get_dashboard_stats(
        self,
    db,
):

        pending = db.query(func.count(self.model.id)).scalar()

        replied = 0

        escalated = 0

        critical = (

        db.query(func.count(AIClassification.id))

        .filter(

            AIClassification.urgency == "Critical"

        )

        .scalar()

    )

        spam = (

        db.query(func.count(AIClassification.id))

        .filter(

            AIClassification.category == "Spam"

        )

        .scalar()

    )

        return {

        "pending": pending,

        "replied": replied,

        "escalated": escalated,

        "critical": critical,

        "spam": spam,

    }
email_repository = EmailRepository()