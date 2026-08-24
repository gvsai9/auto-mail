from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

from app.config.settings import settings
from app.infrastructure.auth.session_store import create_session


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]


CLIENT_SECRETS_FILE = "google_client_secret.json"


# --------------------------------------------------
# Temporary OAuth state store
# --------------------------------------------------

_oauth_store: dict[str, str] = {}


# --------------------------------------------------
# Google Login
# --------------------------------------------------

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

    # Store the PKCE verifier against this OAuth state.
    _oauth_store[state] = flow.code_verifier

    print("========== GOOGLE LOGIN ==========")
    print("Generated state:", state)
    print(
        "Generated verifier exists:",
        flow.code_verifier is not None,
    )
    print("OAuth store size:", len(_oauth_store))
    print("===================================")

    return RedirectResponse(
        url=authorization_url
    )


# --------------------------------------------------
# Google OAuth Callback
# --------------------------------------------------

@router.get("/google/callback")
def google_callback(
    code: str,
    state: str,
):

    print("========== GOOGLE CALLBACK ==========")
    print("Google state:", state)
    print(
        "State exists in OAuth store:",
        state in _oauth_store,
    )
    print("OAuth store size:", len(_oauth_store))
    print("=====================================")

    # --------------------------------------------------
    # Validate OAuth state
    # --------------------------------------------------

    if state not in _oauth_store:

        raise HTTPException(
            status_code=400,
            detail=(
                "Invalid or expired OAuth state. "
                "Please start Google login again."
            ),
        )

    # --------------------------------------------------
    # Retrieve PKCE verifier
    # --------------------------------------------------

    code_verifier = _oauth_store.pop(state)

    print(
        "Code verifier exists:",
        code_verifier is not None,
    )

    # --------------------------------------------------
    # Recreate OAuth flow
    # --------------------------------------------------

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state,
    )

    flow.redirect_uri = settings.google_redirect_uri

    # Reuse the verifier generated during login.
    flow.code_verifier = code_verifier

    # --------------------------------------------------
    # Exchange authorization code
    # --------------------------------------------------

    flow.fetch_token(
        code=code,
    )

    credentials = flow.credentials

    # --------------------------------------------------
    # Identify Gmail account
    # --------------------------------------------------

    gmail = build(
        "gmail",
        "v1",
        credentials=credentials,
    )

    profile = (
        gmail.users()
        .getProfile(
            userId="me"
        )
        .execute()
    )

    user_email = profile["emailAddress"]

    print("Authenticated Gmail:", user_email)

    # --------------------------------------------------
    # Create application session
    # --------------------------------------------------

    session_id = create_session(
        credentials
    )

    # --------------------------------------------------
    # Redirect after successful login
    # --------------------------------------------------

    response = RedirectResponse(
        url=settings.frontend_url
    )

    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        secure=False,
        samesite="lax",
        path="/",
    )

    return response