from fastapi import (
    APIRouter,
    Cookie,
    HTTPException,
)

from app.application.email_flow import (
    process_email_request,
    confirm_and_send,
)

from app.api.schemas.email import (
    PrepareEmailRequest,
    PrepareEmailResponse,
    SendEmailRequest,
    SendEmailResponse,
)

from app.infrastructure.auth.session_store import (
    get_credentials,
)


router = APIRouter(
    prefix="/email",
    tags=["Email"],
)


def get_user_credentials(
    session_id: str | None,
):

    if session_id is None:
        raise HTTPException(
            status_code=401,
            detail="Please sign in with Google first.",
        )

    credentials = get_credentials(
        session_id
    )

    if credentials is None:
        raise HTTPException(
            status_code=401,
            detail="Google session expired. Please sign in again.",
        )

    return credentials


@router.post(
    "/prepare",
    response_model=PrepareEmailResponse,
)
def prepare_email(
    request: PrepareEmailRequest,
    session_id: str | None = Cookie(
        default=None
    ),
):

    credentials = get_user_credentials(
        session_id
    )

    result = process_email_request(
        request.query,
        credentials,
    )

    return result


@router.post(
    "/send",
    response_model=SendEmailResponse,
)
def send_email(
    request: SendEmailRequest,
    session_id: str | None = Cookie(
        default=None
    ),
):

    credentials = get_user_credentials(
        session_id
    )

    result = confirm_and_send(
        request.email,
        confirmed=request.confirmed,
        credentials=credentials,
    )

    if result["status"] == "cancelled":

        return {
            "status": "cancelled",
            "message": "Email sending cancelled.",
        }

    return {
        "status": result["status"],
        "message": "Email sent successfully.",
    }