from pydantic import BaseModel


class EmailSearchResult(BaseModel):
    id: str
    sender: str
    subject: str
    preview: str