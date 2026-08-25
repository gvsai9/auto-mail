from google.oauth2.credentials import Credentials
from uuid import uuid4


_sessions: dict[str, Credentials] = {}


def create_session(
    credentials: Credentials,
) -> str:

    session_id = str(uuid4())

    _sessions[session_id] = credentials

    print("========== CREATE SESSION ==========")
    print("Session ID:", session_id)
    print("Store size:", len(_sessions))
    print("====================================")

    return session_id


def get_credentials(
    session_id: str,
) -> Credentials | None:

    print("========== GET SESSION ==========")
    print("Received session ID:", session_id)
    print("Session exists:", session_id in _sessions)
    print("Store size:", len(_sessions))
    print("=================================")

    return _sessions.get(session_id)


def delete_session(
    session_id: str,
) -> None:

    _sessions.pop(session_id, None)