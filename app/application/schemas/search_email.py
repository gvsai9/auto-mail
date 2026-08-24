from pydantic import BaseModel, Field

#This is used for validation of the input for searching the email.
class SearchEmailInput(BaseModel):
    query: str = Field(
        description="Keywords or brief idea describing the email to search for."
    )

    sender: str | None = Field(
        default=None,
        description="Optional sender email address."
    )