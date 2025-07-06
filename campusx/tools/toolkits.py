# type: ignore
from langchain_core.tools import tool


@tool
def add(a: int, b: int) -> int:
    """Add two number"""
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """multiply two number"""
    return a * b


class MathToolKit:
    def get_tools(self):
        return [add, multiply]


toolkit = MathToolKit()

tools = toolkit.get_tools()

# for tool_item in tools:
#     print(f"{tool_item.name} => {tool_item.description}")

print(tools)
