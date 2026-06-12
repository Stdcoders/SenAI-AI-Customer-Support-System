from datetime import datetime

from pydantic import BaseModel, ConfigDict


class EmailIngestRequest(BaseModel):

    message_id: str

    sender: str

    subject: str

    body: str

    timestamp: datetime

    thread_id: str


class EmailResponse(BaseModel):

    id: int

    external_message_id: str

    sender: str

    subject: str

    body: str

    timestamp: datetime

    thread_id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)