from app.config.settings import settings


def test_nvidia_api_key_loaded():
    assert settings.nvidia_api_key