from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.base import TimestampMixin


class Email(Base, TimestampMixin):

    __tablename__ = "emails"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    external_message_id: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    sender: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    subject: Mapped[str] = mapped_column(String(500))

    body: Mapped[str] = mapped_column(Text)

    timestamp: Mapped[datetime] = mapped_column(DateTime)

    thread_id: Mapped[int] = mapped_column(
        ForeignKey("threads.id"),
        nullable=False,
    )

    thread = relationship(
        "Thread",
        back_populates="emails",
    )

    classification = relationship(
        "AIClassification",
        back_populates="email",
        uselist=False,
        cascade="all, delete-orphan",
    )

    actions = relationship(
        "Action",
        back_populates="email",
        cascade="all, delete-orphan",
    )