from app.agent.tools.search_email import create_search_email_tool
from app.infrastructure.email.mock_reader import MockEmailReader
from app.application.use_cases.search_emails import SearchEmailsUseCase


def test_search_email_tool():

    reader = MockEmailReader()
    use_case = SearchEmailsUseCase(reader)

    tool = create_search_email_tool(use_case)

    result = tool.invoke({
        "query": "ML assignment"
    })

    assert result