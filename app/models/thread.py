from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.base import TimestampMixin


class Thread(Base, TimestampMixin):

    __tablename__ = "threads"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    external_thread_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    subject: Mapped[str] = mapped_column(String(500))

    status: Mapped[str] = mapped_column(
        String(50),
        default="OPEN",
    )

    contact_id: Mapped[int] = mapped_column(
        ForeignKey("contacts.id"),
        nullable=False,
    )

    contact = relationship(
        "Contact",
        back_populates="threads",
    )

    emails = relationship(
        "Email",
        back_populates="thread",
        cascade="all, delete-orphan",
    )