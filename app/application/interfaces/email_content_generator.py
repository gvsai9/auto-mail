from abc import ABC, abstractmethod


class EmailContentGenerator(ABC):

    @abstractmethod
    def generate(
        self,
        recipient: str,
        query: str,
    ) -> tuple[str, str]:
        """
        Generate an email subject and body
        using the recipient and user's request.
        """
        pass