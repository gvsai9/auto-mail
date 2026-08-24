from app.domain.models.outgoing_email import OutgoingEmail
from app.infrastructure.email.gmail import push_mail


class GmailEmailSender:

    def __init__(self, credentials):
        self.credentials = credentials

    def send(
        self,
        email: OutgoingEmail,
    ):
        return push_mail(
            email,
            self.credentials,
        ) 