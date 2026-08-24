from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    nvidia_api_key: str
    google_redirect_uri: str
    frontend_url: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()