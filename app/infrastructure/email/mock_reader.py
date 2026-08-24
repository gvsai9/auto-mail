from app.domain.models.email import Email
from app.application.interfaces.email_reader import EmailReader

class MockEmailReader(EmailReader):

    def __init__(self):
        self._emails = [
            Email(
                id="email_001",
                sender="ravi@example.com",
                recipients=["student@example.com"],
                subject="ML Assignment Deadline",
                body=(
                    "The ML assignment deadline has been extended to "
                    "August 25. Please submit your CNN classification project."
                ),
                timestamp="2026-08-20T10:30:00",
            ),
            Email(
                id="email_002",
                sender="ravi@example.com",
                recipients=["student@example.com"],
                subject="ML Assignment Instructions",
                body=(
                    "Please include the dataset description, preprocessing "
                    "steps, model architecture, and evaluation metrics."
                ),
                timestamp="2026-08-18T15:20:00",
            ),
            Email(
                id="email_003",
                sender="anita@example.com",
                recipients=["student@example.com"],
                subject="Database Assignment",
                body=(
                    "The database assignment should be submitted through "
                    "the college portal."
                ),
                timestamp="2026-08-19T09:15:00",
            ),
        ]

    def search(
        self,
        query: str,
        sender: str | None = None,
    ) -> list[Email]:

        query = query.lower()

        results = []

        for email in self._emails:

            if sender and email.sender.lower() != sender.lower():
                continue

            searchable_text = (
                f"{email.subject} {email.body}"
            ).lower()

            if query in searchable_text:
                results.append(email)

        return results

    def read(self, id: str):

        for email in self._emails:

            if email.id == id:
                return email

        return None