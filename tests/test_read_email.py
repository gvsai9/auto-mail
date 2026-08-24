from app.agent.tools.read_email import create_read_email_tool
from app.infrastructure.email.mock_reader import MockEmailReader
from app.agent.tools.registry import ToolRegistry
from app.composition.dependencies import create_tool_registry

def test_tool_registry_contains_email_tools():

    registry = create_tool_registry()

    assert registry.get("search_emails") is not None
    assert registry.get("read_email") is not None