import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = [
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.readonly",
]


def get_gmail_credentials():

    credentials = None

    if os.path.exists("token.json"):

        credentials = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES,
        )

    if credentials and credentials.valid:
        return credentials

    if credentials and credentials.expired and credentials.refresh_token:

        credentials.refresh(Request())

        with open("token.json", "w") as token:
            token.write(credentials.to_json())

        return credentials

    flow = InstalledAppFlow.from_client_secrets_file(
        "credentials.json",
        SCOPES,
    )

    credentials = flow.run_local_server(
        port=0
    )

    with open("token.json", "w") as token:
        token.write(credentials.to_json())

    return credentials