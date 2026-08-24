import base64
from email.utils import parsedate_to_datetime

from googleapiclient.discovery import build

from app.application.interfaces.email_reader import EmailReader
from app.domain.models.email import Email


class GmailEmailReader(EmailReader):

    def __init__(self, credentials):

        self.service = build(
            "gmail",
            "v1",
            credentials=credentials,
        )

    def search(
        self,
        query: str,
        sender: str | None = None,
    ) -> list[Email]:

        gmail_query = query

        if sender:
            gmail_query += f" from:{sender}"

        response = (
            self.service.users()
            .messages()
            .list(
                userId="me",
                q=gmail_query,
                maxResults=10,
            )
            .execute()
        )

        messages = response.get(
            "messages",
            []
        )

        emails = []

        for message in messages:

            try:

                email = self.read(
                    message["id"]
                )

                if email:
                    emails.append(email)

            except Exception as exc:

                print(
                    f"Failed to read Gmail message "
                    f"{message['id']}: {exc}"
                )

        return emails

    def read(
        self,
        id: str,
    ) -> Email | None:

        response = (
            self.service.users()
            .messages()
            .get(
                userId="me",
                id=id,
                format="full",
            )
            .execute()
        )

        payload = response.get(
            "payload",
            {}
        )

        headers = payload.get(
            "headers",
            []
        )

        header_map = {
            header["name"].lower(): header["value"]
            for header in headers
        }

        sender = header_map.get(
            "from",
            ""
        )

        subject = header_map.get(
            "subject",
            ""
        )

        date_header = header_map.get(
            "date"
        )

        timestamp = (
            parsedate_to_datetime(
                date_header
            )
            if date_header
            else None
        )

        body = self._extract_body(
            payload
        )

        recipients = []

        to_header = header_map.get(
            "to"
        )

        if to_header:

            recipients = [
                recipient.strip()
                for recipient in to_header.split(",")
            ]

        return Email(
            id=id,
            sender=sender,
            recipients=recipients,
            subject=subject,
            body=body,
            timestamp=timestamp,
        )

    def _extract_body(
        self,
        payload,
    ) -> str:

        body = payload.get(
            "body",
            {}
        )

        data = body.get(
            "data"
        )

        if data:

            return self._decode_body(
                data
            )

        for part in payload.get(
            "parts",
            []
        ):

            if part.get(
                "mimeType"
            ) == "text/plain":

                data = part.get(
                    "body",
                    {}
                ).get(
                    "data"
                )

                if data:

                    return self._decode_body(
                        data
                    )

        return ""

    def _decode_body(
        self,
        data: str,
    ) -> str:

        decoded = base64.urlsafe_b64decode(
            data.encode("UTF-8")
        )

        return decoded.decode(
            "UTF-8",
            errors="replace",
        )