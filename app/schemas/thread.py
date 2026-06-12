from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ThreadBase(BaseModel):

    external_thread_id: str

    subject: str


class ThreadResponse(ThreadBase):

    id: int

    status: str

    contact_id: int

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)