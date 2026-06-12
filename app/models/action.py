from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.base import TimestampMixin


class Action(Base, TimestampMixin):

    __tablename__ = "actions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    email_id: Mapped[int] = mapped_column(
        ForeignKey("emails.id"),
        nullable=False,
    )

    tool_name: Mapped[str] = mapped_column(
        String(100),
    )

    action_type: Mapped[str] = mapped_column(
        String(100),
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="PENDING",
    )

    output: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    email = relationship(
        "Email",
        back_populates="actions",
    )