from langchain_core.language_models.chat_models import BaseChatModel

from app.agent.tools.registry import ToolRegistry


def create_agent_model(
    model: BaseChatModel,
    registry: ToolRegistry,
) -> BaseChatModel:

    return model.bind_tools(
        registry.all()
    )