from app.application.interfaces.email_sender import EmailSender
from app.domain.models.outgoing_email import OutgoingEmail


class MockEmailSender(EmailSender):

    def __init__(self):
        self.sent_emails: list[OutgoingEmail] = []

    def send(self, email: OutgoingEmail):

        self.sent_emails.append(email)

        return email