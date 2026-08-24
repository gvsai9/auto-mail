from app.application.interfaces.email_content_generator import (
    EmailContentGenerator,
)
from app.application.interfaces.email_sender import EmailSender
from app.application.schemas.send_email import SendEmailInput
from app.domain.models.outgoing_email import OutgoingEmail


class SendEmailUseCase:

    def __init__(
        self,
        sender: EmailSender,
        content_generator: EmailContentGenerator,
    ):
        self.sender = sender
        self.content_generator = content_generator

    def execute(self, input: SendEmailInput):

        subject, body = self.content_generator.generate(
            recipient=input.recipient,
            query=input.query,
        )
        email = OutgoingEmail(
            recipient=input.recipient,
            subject=subject,
            body=body,
        )

        return self.sender.send(email)