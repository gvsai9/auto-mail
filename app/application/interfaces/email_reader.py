from abc import ABC, abstractmethod

from app.domain.models.email import Email

# This as an interface for Email , which helps to scale with different email providers 
class EmailReader(ABC):

    @abstractmethod
    def search(
        self,
        query: str,
        sender: str | None = None,
    ) -> list[Email]:
        ...

    @abstractmethod
    def read(self, id: str) -> Email:
        ...
