from app.agent.tools.registry import ToolRegistry


class ToolExecutor:

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def execute(self, tool_call: dict):

        tool = self.registry.get(tool_call["name"])

        return tool.invoke(tool_call["args"])