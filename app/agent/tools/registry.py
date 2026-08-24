from langchain_core.tools import BaseTool


class ToolRegistry:

    def __init__(self, tools: list[BaseTool]):
        self._tools = {
            tool.name: tool
            for tool in tools
        }

    def get(self, name: str) -> BaseTool:

        tool = self._tools.get(name)

        if tool is None:
            raise ValueError(f"Unknown tool: {name}")

        return tool

    def get_all(self) -> list[BaseTool]:
        return list(self._tools.values())