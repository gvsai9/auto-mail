from app.application.interfaces.email_content_generator import (
    EmailContentGenerator,
)


class MockEmailContentGenerator(EmailContentGenerator):

    def generate(self, query: str) -> tuple[str, str]:

        subject = "Email regarding your request"

        body = query

        return subject, body