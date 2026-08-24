from pydantic import BaseModel, Field


class SendEmailInput(BaseModel):
    recipient: str = Field(
        description="Email address of the recipient."
    )

    query: str = Field(
        description=(
            "Natural-language description of what the email "
            "should communicate."
        )
    )