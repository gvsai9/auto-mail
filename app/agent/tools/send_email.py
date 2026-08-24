from langchain_core.tools import StructuredTool

from app.application.schemas.send_email import (
    SendEmailInput,
)

from app.domain.models.outgoing_email import (
    OutgoingEmail,
)


def create_send_email_tool(use_case):

    def send_email(
        recipient: str,
        query: str,
    ):

        email_input = SendEmailInput(
            recipient=recipient,
            query=query,
        )

        # Generate the email.
        # Do NOT send it here.
        generated = (
            use_case.content_generator.generate(
                recipient=recipient,
                query=query,
            )
        )

        subject, body = generated

        email = OutgoingEmail(
            recipient=recipient,
            subject=subject,
            body=body,
        )

        return {
            "status": "confirmation_required",
            "email": email,
        }

    return StructuredTool.from_function(
        func=send_email,
        name="send_email",
        description=(
            "Prepare an email for sending. "
            "Generate the subject and body, but DO NOT actually send "
            "the email. The result is a preview that requires explicit "
            "user confirmation before sending. "
            "The recipient is the destination email address. "
            "The query describes what the email should communicate."
        ),
        args_schema=SendEmailInput,
    )