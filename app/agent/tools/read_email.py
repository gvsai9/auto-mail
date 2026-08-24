from langchain_core.tools import StructuredTool

from app.application.interfaces.email_reader import EmailReader
from app.application.schemas.read_email import ReadEmailInput


def create_read_email_tool(reader: EmailReader):

    def read_email(id: str):

        return reader.read(id)

    return StructuredTool.from_function(
        func=read_email,
        name="read_email",
        description=(
            "Read one specific email using its exact unique ID. "
            "Before calling this tool, look at the previous messages "
            "and tool results in the conversation context. "
            "If a search_email tool was previously called, use the exact "
            "email ID returned by that search result. "
            "Do not invent an ID, use a description as an ID, "
            "or use the tool name as an ID. "
            "This tool does not search for emails; it only reads an "
            "email when given its exact ID."
        ),
        args_schema=ReadEmailInput,
    )