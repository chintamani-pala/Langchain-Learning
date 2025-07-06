# type: ignore
from langchain.tools import StructuredTool
from pydantic import BaseModel, Field


class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")


def multiply_func(a: int, b: int) -> int:
    return a * b


multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Multiply two number",
    args_schema=MultiplyInput,
)

result = multiply_tool.invoke({"a": 3, "b": 5})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)
print(multiply_tool.args_schema.model_json_schema())
