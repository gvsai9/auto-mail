# app/domain/models/email.py

from datetime import datetime

from pydantic import BaseModel, Field


class Email(BaseModel):
    id: str
    sender: str
    recipients: list[str]
    subject: str
    body: str
    timestamp: datetime

    @property
    def preview(self) -> str:
        return self.body[:200]