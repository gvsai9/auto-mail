from fastapi import APIRouter

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


router = APIRouter(
    prefix="/email",
    tags=["Email"],
)


@router.post(
    "/prepare",
    response_model=PrepareEmailResponse,
)
def prepare_email(
    request: PrepareEmailRequest,
):

    result = process_email_request(
        request.query
    )

    return result


@router.post(
    "/send",
    response_model=SendEmailResponse,
)
def send_email(
    request: SendEmailRequest,
):

    result = confirm_and_send(
        request.email,
        confirmed=request.confirmed,
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