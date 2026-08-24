from app.agent.manual_agent import ManualAgent


def process_email_request(
    user_input: str,
    credentials,
):

    agent = ManualAgent(
        credentials
    )

    result = agent.invoke(
        user_input
    )

    email = result["email"]

    if email is None:
        return {
            "status": "failed",
            "message": "No email was generated.",
        }

    return {
        "status": "preview",
        "email": email,
    }


def confirm_and_send(
    email,
    confirmed: bool,
    credentials,
):

    if not confirmed:
        return {
            "status": "cancelled",
        }

    # Sending is now handled by GmailEmailSender
    # through the authenticated user's credentials.
    from app.infrastructure.email.gmail_sender import (
        GmailEmailSender,
    )

    sender = GmailEmailSender(
        credentials
    )

    response = sender.send(
        email
    )

    return {
        "status": "sent",
        "gmail_response": response,
    }