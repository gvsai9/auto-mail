import base64
from email.mime.text import MIMEText

from googleapiclient.discovery import build

from app.domain.models.outgoing_email import OutgoingEmail
from app.infrastructure.email.gmail_auth import get_gmail_credentials


def push_mail(email: OutgoingEmail):

    credentials = get_gmail_credentials()

    service = build(
        "gmail",
        "v1",
        credentials=credentials,
    )

    message = MIMEText(email.body)

    message["to"] = email.recipient
    message["subject"] = email.subject

    encoded_message = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    response = (
        service.users()
        .messages()
        .send(
            userId="me",
            body={
                "raw": encoded_message,
            },
        )
        .execute()
    )

    return response