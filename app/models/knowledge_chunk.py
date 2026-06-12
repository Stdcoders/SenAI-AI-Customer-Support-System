from sqlalchemy import JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base
from app.models.base import TimestampMixin


class KnowledgeChunk(Base, TimestampMixin):

    __tablename__ = "knowledge_chunks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    document_name: Mapped[str] = mapped_column(
        String(255),
    )

    chunk_text: Mapped[str] = mapped_column(
        Text,
    )

    chunk_metadata: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )