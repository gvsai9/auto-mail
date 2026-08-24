from google.oauth2.credentials import Credentials
from uuid import uuid4


_sessions: dict[str, Credentials] = {}


def create_session(
    credentials: Credentials,
) -> str:

    session_id = str(uuid4())

    _sessions[session_id] = credentials

    return session_id


def get_credentials(
    session_id: str,
) -> Credentials | None:

    return _sessions.get(session_id)


def delete_session(
    session_id: str,
) -> None:

    _sessions.pop(session_id, None)