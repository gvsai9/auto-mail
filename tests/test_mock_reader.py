import pytest

from app.infrastructure.email.mock_reader import MockEmailReader


def test_search_emails():
    reader = MockEmailReader()

    results = reader.search("ML assignment")

    assert len(results) == 2


def test_search_by_sender():
    reader = MockEmailReader()

    results = reader.search(
        "assignment",
        sender="anita@example.com"
    )

    assert len(results) == 1
    assert results[0].sender == "anita@example.com"


def test_search_no_results():
    reader = MockEmailReader()

    results = reader.search("football")

    assert results == []


def test_read_email():
    reader = MockEmailReader()

    email = reader.read("email_001")

    assert email.subject == "ML Assignment Deadline"


def test_read_unknown_email():
    reader = MockEmailReader()

    email = reader.read("does_not_exist")

    assert email is None

def test_read_email_by_id():

    reader = MockEmailReader()

    result = reader.read("email_001")

    assert result is not None
    assert result.id == "email_001"