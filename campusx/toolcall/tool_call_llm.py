# type:ignore
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two number and returns the result"""
    return a * b


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# tool binding
llm_with_tools = llm.bind_tools([multiply])

query = "what is the result of multiply 3 and 5"

result = llm_with_tools.invoke(query)

# llm give the tool name and arguments
print(result.tool_calls[0])
