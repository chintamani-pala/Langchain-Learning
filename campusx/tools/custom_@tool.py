# type: ignore
from langchain_core.tools import tool

# step 1 => Create a function
# step 2 => Add type hints
# step 3 => Add @tool decorator
# step 4 => Add docstring in the function


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


result = multiply.invoke({"a": 3, "b": 5})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())
