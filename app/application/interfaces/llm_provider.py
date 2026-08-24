from abc import ABC, abstractmethod

from langchain_core.language_models.chat_models import BaseChatModel

from app.application.schemas.llm import LLMConfig

# This is an interface for LLMProvider, which helps to scale with different LLM providers
class LLMProvider(ABC):

    @abstractmethod
    def create_model(
        self,
        config: LLMConfig,
    ) -> BaseChatModel:
        pass