from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base
from app.models.base import TimestampMixin


class AuditLog(Base, TimestampMixin):

    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    entity: Mapped[str] = mapped_column(
        String(100),
    )

    entity_id: Mapped[int] = mapped_column()

    event: Mapped[str] = mapped_column(
        String(255),
    )

    details: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )