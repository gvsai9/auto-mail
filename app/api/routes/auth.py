from fastapi import APIRouter, Cookie, HTTPException
from fastapi.responses import RedirectResponse

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

from app.config.settings import settings
from app.infrastructure.auth.google_credentials import GoogleCredentialStore


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]


CLIENT_SECRETS_FILE = "google_client_secret.json"

credential_store = GoogleCredentialStore()


@router.get("/google")
def google_login():

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
    )

    flow.redirect_uri = settings.google_redirect_uri

    authorization_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="false",
        prompt="consent",
    )

    response = RedirectResponse(authorization_url)

    response.set_cookie(
        key="oauth_state",
        value=state,
        httponly=True,
        secure=False,
        samesite="lax",
    )

    response.set_cookie(
        key="code_verifier",
        value=flow.code_verifier,
        httponly=True,
        secure=False,
        samesite="lax",
    )

    return response


@router.get("/google/callback")
def google_callback(
    code: str,
    state: str,
    oauth_state: str | None = Cookie(default=None),
    code_verifier: str | None = Cookie(default=None),
):

    # -----------------------------
    # Validate OAuth state
    # -----------------------------

    if oauth_state is None:
        raise HTTPException(
            status_code=400,
            detail="Missing OAuth state.",
        )

    if state != oauth_state:
        raise HTTPException(
            status_code=400,
            detail="Invalid OAuth state.",
        )

    # -----------------------------
    # Validate PKCE verifier
    # -----------------------------

    if code_verifier is None:
        raise HTTPException(
            status_code=400,
            detail="Missing PKCE code verifier.",
        )

    # -----------------------------
    # Recreate OAuth flow
    # -----------------------------

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state,
    )

    flow.redirect_uri = settings.google_redirect_uri

    # Important:
    # The verifier generated during /google
    # must be reused during the callback.
    flow.code_verifier = code_verifier

    # -----------------------------
    # Exchange authorization code
    # for Google credentials
    # -----------------------------

    flow.fetch_token(
        code=code,
    )

    credentials = flow.credentials

    # -----------------------------
    # Identify the Gmail account
    # -----------------------------

    gmail = build(
        "gmail",
        "v1",
        credentials=credentials,
    )

    profile = (
        gmail.users()
        .getProfile(userId="me")
        .execute()
    )

    user_email = profile["emailAddress"]

    # -----------------------------
    # Store credentials
    # -----------------------------

    credential_store.save(
        user_email,
        credentials,
    )

    # -----------------------------
    # Return success
    # -----------------------------

    return {
        "message": "Google Gmail authorization successful",
        "email": user_email,
        "token_type": "Bearer",
        "refresh_token": bool(credentials.refresh_token),
        "scopes": credentials.scopes,
    }