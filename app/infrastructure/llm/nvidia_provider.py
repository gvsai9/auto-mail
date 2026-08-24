from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI

from app.application.interfaces.llm_provider import LLMProvider
from app.application.schemas.llm import LLMConfig
from app.config.settings import settings


class NVIDIAProvider(LLMProvider):

    def create_model(
        self,
        config: LLMConfig,
    ) -> BaseChatModel:

        return ChatOpenAI(
            model=config.model_name,
            temperature=config.temperature,
            api_key=settings.nvidia_api_key,
            base_url="https://integrate.api.nvidia.com/v1",
        )