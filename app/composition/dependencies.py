from app.application.use_cases.search_emails import SearchEmailsUseCase
from app.application.use_cases.send_email import SendEmailUseCase

from app.infrastructure.email.gmail_reader import GmailEmailReader
from app.infrastructure.email.mock_sender import MockEmailSender

from app.infrastructure.llm.nvidia_provider import NVIDIAProvider
from app.infrastructure.llm.email_content_generator import (
    LLMEmailContentGenerator,
)

from app.application.schemas.llm import LLMConfig

from app.agent.tools.registry import ToolRegistry
from app.agent.tools.search_email import create_search_email_tool
from app.agent.tools.read_email import create_read_email_tool
from app.agent.tools.send_email import create_send_email_tool


class ToolExecutor:

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, tool_call: dict):

        tool = self.registry.get(
            tool_call["name"]
        )

        return tool.invoke(
            tool_call["args"]
        )


def create_llm():

    config = LLMConfig(
        provider="nvidia",
        model_name="meta/llama-3.1-8b-instruct",
        temperature=0.0,
    )

    provider = NVIDIAProvider()

    return provider.create_model(config)


def create_email_content_generator():

    model = create_llm()

    return LLMEmailContentGenerator(
        model=model,
        sender_name="Venkata Sai",
    )


def create_search_email_use_case():

    reader = GmailEmailReader()

    return SearchEmailsUseCase(
        reader
    )


def create_send_email_use_case():

    sender = MockEmailSender()

    content_generator = create_email_content_generator()

    return SendEmailUseCase(
        sender=sender,
        content_generator=content_generator,
    )


def create_tool_registry():

    reader = GmailEmailReader()

    # Search
    search_use_case = create_search_email_use_case()

    search_tool = create_search_email_tool(
        search_use_case
    )

    # Read
    read_tool = create_read_email_tool(
        reader
    )

    # Send
    send_use_case = create_send_email_use_case()

    send_tool = create_send_email_tool(
        send_use_case
    )

    return ToolRegistry([
        search_tool,
        read_tool,
        send_tool,
    ])


def create_tool_executor():

    registry = create_tool_registry()

    return ToolExecutor(registry)