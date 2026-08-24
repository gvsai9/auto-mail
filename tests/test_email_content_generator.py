from app.infrastructure.llm.email_content_generator import (
    LLMEmailContentGenerator,
)
from app.application.schemas.generated_email import GeneratedEmail
from app.composition.dependencies import create_llm


from app.infrastructure.llm.email_content_generator import (
    LLMEmailContentGenerator,
)
from app.composition.dependencies import create_llm


def test_generate_email_content():

    model = create_llm()

    generator = LLMEmailContentGenerator(
        model=model,
        sender_name="Venkata Sai",
    )

    subject, body = generator.generate(
        recipient="ravi@example.com",
        query="I completed the ML assignment.",
    )

    print("\n===== GENERATED SUBJECT =====")
    print(subject)

    print("\n===== GENERATED BODY =====")
    print(body)

    assert subject
    assert body

    assert "Venkata Sai" in body