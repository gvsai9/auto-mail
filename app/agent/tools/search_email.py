from langchain_core.tools import StructuredTool

from app.application.schemas.search_email import SearchEmailInput
from app.application.use_cases.search_emails import SearchEmailsUseCase


def create_search_email_tool(use_case):

    def search_emails(query: str, sender: str | None = None):

        print("\n===== SEARCH TOOL INPUT =====")
        print("query:", repr(query))
        print("sender:", repr(sender))
        print("=============================\n")
        if sender == "null":
            sender = None

        search_input = SearchEmailInput(
            query=query,
            sender=sender,
        )

        return use_case.execute(search_input)

    return StructuredTool.from_function(
        func=search_emails,
        name="search_emails",
description=(
    "Search the user's emails using keywords, subject, content, "
    "sender, or a brief description of the email. "
    "Use this tool FIRST when the user asks to read, inspect, "
    "summarize, or find an email but does not provide an exact email ID. "
    "The search results contain the exact unique email IDs. "
    "After finding the relevant email, use that exact ID with "
    "the read_email tool to retrieve the full email. "
    "Do not use read_email with a description or guessed ID."
),
        args_schema=SearchEmailInput,
    )