from abc import ABC, abstractmethod

from langchain_core.language_models.chat_models import BaseChatModel

from app.application.schemas.llm import LLMConfig


class LLMProvider(ABC):

    @abstractmethod
    def create_model(
        self,
        config: LLMConfig,
    ) -> BaseChatModel:
        pass