from app.application.email_flow import (
    process_email_request,
    confirm_and_send,
)


def test_email_flow():

    preview = process_email_request(
        "Send an email to ravi@example.com saying I completed the ML assignment."
    )

    print("\n===== EMAIL PREVIEW =====")
    print(preview["email"])
    print("=========================\n")

    assert preview["status"] == "preview"
    assert preview["email"] is not None

    result = confirm_and_send(
        preview["email"],
        confirmed=True,
    )

    print("\n===== SEND RESULT =====")
    print(result)
    print("=======================\n")

    assert result["status"] == "sent"
    assert result["gmail_response"]["id"]