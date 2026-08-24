from pydantic import BaseModel, Field


class ReadEmailInput(BaseModel):

    id: str = Field(
        description=(
            "Exact email ID obtained from a previous search_email "
            "result in the conversation context."
        )
    )