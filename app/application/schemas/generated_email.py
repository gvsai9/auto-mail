from pydantic import BaseModel, Field


class GeneratedEmail(BaseModel):

    subject: str = Field(
        description="A concise and appropriate email subject."
    )

    body: str = Field(
        description="The complete email body."
    )