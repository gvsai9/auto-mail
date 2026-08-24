import base64
from email.mime.text import MIMEText

from googleapiclient.discovery import build

from app.domain.models.outgoing_email import OutgoingEmail


def push_mail(
    email: OutgoingEmail,
    credentials,
):

    service = build(
        "gmail",
        "v1",
        credentials=credentials,
    )

    message = MIMEText(
        email.body
    )

    message["to"] = email.recipient
    message["subject"] = email.subject

    encoded_message = (
        base64.urlsafe_b64encode(
            message.as_bytes()
        )
        .decode()
    )

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