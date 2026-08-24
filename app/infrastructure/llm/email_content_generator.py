from app.application.interfaces.email_content_generator import (
    EmailContentGenerator,
)
from app.application.schemas.generated_email import GeneratedEmail
from app.infrastructure.llm.prompts.email_generation import (
    EMAIL_GENERATION_PROMPT,
)


class LLMEmailContentGenerator(EmailContentGenerator):

    def __init__(self, model, sender_name: str):
        self.model = model
        self.sender_name = sender_name

        self.structured_model = model.with_structured_output(
            GeneratedEmail
        )

    def generate(
        self,
        recipient: str,
        query: str,
    ) -> tuple[str, str]:

        chain = EMAIL_GENERATION_PROMPT | self.structured_model

        result = chain.invoke(
            {
                "sender_name": self.sender_name,
                "recipient": recipient,
                "query": query,
            }
        )

        return result.subject, result.body