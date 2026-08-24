from app.application.schemas.send_email import SendEmailInput
from app.application.use_cases.send_email import SendEmailUseCase
from app.infrastructure.email.mock_sender import MockEmailSender
from app.infrastructure.llm.mock_email_generator import (
    MockEmailContentGenerator,
)


def test_send_email_use_case():

    sender = MockEmailSender()
    generator = MockEmailContentGenerator()

    use_case = SendEmailUseCase(
        sender=sender,
        content_generator=generator,
    )

    input_data = SendEmailInput(
        recipient="ravi@example.com",
        query="Tell Ravi that I completed the ML assignment.",
    )

    result = use_case.execute(input_data)

    assert result is not None