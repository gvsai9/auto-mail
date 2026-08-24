from app.domain.models.outgoing_email import OutgoingEmail
from app.infrastructure.email.gmail import push_mail


def test_push_mail():

    email = OutgoingEmail(
        recipient="gummadellivenkatsai@gmail.com",
        subject="Email Agent Test",
        body="""Hi,

This is a test email from my email agent.

Best regards,
Venkata Sai
""",
    )

    response = push_mail(email)

    print("\n===== GMAIL RESPONSE =====")
    print(response)
    print("==========================")

    assert response["id"]