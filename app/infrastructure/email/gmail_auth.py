from google.oauth2.credentials import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.readonly",
]


def validate_credentials(
    credentials: Credentials,
) -> Credentials:

    if credentials.expired and not credentials.refresh_token:
        raise ValueError(
            "Gmail credentials expired and cannot be refreshed."
        )

    return credentials