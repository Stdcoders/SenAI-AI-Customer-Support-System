from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.models.base import TimestampMixin


class Contact(Base, TimestampMixin):

    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )

    name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    company: Mapped[str | None] = mapped_column(String(255), nullable=True)

    threads = relationship(
        "Thread",
        back_populates="contact",
        cascade="all, delete-orphan",
    )