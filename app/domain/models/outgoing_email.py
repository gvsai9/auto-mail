from dataclasses import dataclass


@dataclass
class OutgoingEmail:
    recipient: str
    subject: str
    body: str