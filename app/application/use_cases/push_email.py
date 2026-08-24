from app.application.interfaces.email_sender import EmailSender
from app.domain.models.outgoing_email import OutgoingEmail


class PushMailUseCase:

    def __init__(self, sender: EmailSender):
        self.sender = sender

    def execute(self, email: OutgoingEmail) -> None:
        self.sender.send(email)