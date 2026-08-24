from app.agent.manual_agent import ManualAgent
from app.infrastructure.email.gmail import push_mail


def process_email_request(user_input: str):

    agent = ManualAgent()

    result = agent.invoke(user_input)

    email = result["email"]

    if email is None:
        return {
            "status": "failed",
            "message": "No email was generated.",
        }

    # This object is what the UI will display
    return {
        "status": "preview",
        "email": email,
    }


def confirm_and_send(email, confirmed: bool):

    if not confirmed:
        return {
            "status": "cancelled",
        }

    response = push_mail(email)

    return {
        "status": "sent",
        "gmail_response": response,
    }