from pydantic import BaseModel

from app.domain.models.outgoing_email import OutgoingEmail


class PrepareEmailRequest(BaseModel):

    query: str


class PrepareEmailResponse(BaseModel):

    status: str

    email: OutgoingEmail | None = None

    message: str | None = None


class SendEmailRequest(BaseModel):

    email: OutgoingEmail

    confirmed: bool


class SendEmailResponse(BaseModel):

    status: str
    message: str