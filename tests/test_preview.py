from app.application.use_cases.search_emails import SearchEmailsUseCase
from app.infrastructure.email.mock_reader import MockEmailReader
from app.application.schemas.search_email import SearchEmailInput
from app.application.schemas.email_search_result import EmailSearchResult

def test_search_returns_preview():

    reader = MockEmailReader()

    use_case = SearchEmailsUseCase(reader)

    result = use_case.execute(
        SearchEmailInput(
            query="ML assignment"
        )
    )

    assert result
    assert isinstance(result[0], EmailSearchResult)

    assert result[0].id == "email_001"
    assert result[0].subject == "ML Assignment Deadline"
    assert result[0].preview
    print("Preview:", result[0].preview)