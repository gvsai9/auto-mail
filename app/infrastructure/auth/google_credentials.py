from google.oauth2.credentials import Credentials


class GoogleCredentialStore:

    def __init__(self):
        self._credentials: dict[str, Credentials] = {}

    def save(
        self,
        user_id: str,
        credentials: Credentials,
    ):
        self._credentials[user_id] = credentials

    def get(
        self,
        user_id: str,
    ) -> Credentials | None:

        credentials = self._credentials.get(user_id)

        if credentials is None:
            return None

        return credentials