# type: ignore
from langchain.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


# arg schema using pydantic
class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")


class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two number"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b


multiply_tool = MultiplyTool()
result = multiply_tool.invoke({"a": 3, "b": 5})
print(result)
