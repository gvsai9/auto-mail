from langchain_core.tools import StructuredTool

from app.application.schemas.send_email import SendEmailInput


def create_send_email_tool(use_case):

    def send_email(
        recipient: str,
        query: str,
    ):
        email_input = SendEmailInput(
            recipient=recipient,
            query=query,
        )

        return use_case.execute(email_input)

    return StructuredTool.from_function(
        func=send_email,
        name="send_email",
        description=(
            "Send an email to a recipient based on a natural-language "
            "request. The recipient is the destination email address. "
            "The query describes what the email should communicate. "
            "Generate an appropriate subject and body from the request."
        ),
        args_schema=SendEmailInput,
    )