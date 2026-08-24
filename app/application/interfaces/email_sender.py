from abc import ABC, abstractmethod

from app.domain.models.outgoing_email import OutgoingEmail


class EmailSender(ABC):

    @abstractmethod
    def send(self, email: OutgoingEmail):
        pass