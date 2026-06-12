from sqlalchemy import Boolean, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.base import TimestampMixin


class AIClassification(Base, TimestampMixin):

    __tablename__ = "ai_classifications"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    email_id: Mapped[int] = mapped_column(
        ForeignKey("emails.id"),
        unique=True,
        nullable=False,
    )

    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    urgency: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    sentiment: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    confidence: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    requires_human: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    reasoning: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    email = relationship(
        "Email",
        back_populates="classification",
    )