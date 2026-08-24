from app.application.interfaces.email_reader import EmailReader
from app.application.schemas.search_email import SearchEmailInput
from app.application.schemas.email_search_result import EmailSearchResult


class SearchEmailsUseCase:

    def __init__(self, reader: EmailReader):
        self.reader = reader

    def execute(self, input: SearchEmailInput):

        emails = self.reader.search(
            query=input.query,
            sender=input.sender,
        )

        return [
            EmailSearchResult(
                id=email.id,
                sender=email.sender,
                subject=email.subject,
                preview=email.body[:100],
            )
            for email in emails
        ]