from app.infrastructure.email.gmail_reader import GmailEmailReader


def test_gmail_search():

    reader = GmailEmailReader()

    results = reader.search(
        query="Find emails about ML assignment"
    )

    print("\n===== GMAIL SEARCH RESULTS =====")

    for email in results:
        print("ID:", email.id)
        print("FROM:", email.sender)
        print("SUBJECT:", email.subject)
        print("PREVIEW:", email.body[:100])
        print("-----------------------------")

    assert isinstance(results, list)