# type: ignore
from langchain_core.messages import ToolMessage, AIMessage
from langchain_core.tools import tool
from langchain.globals import set_debug
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import requests
import os

# ✅ Enable debug logging
# set_debug(True)

# ✅ Load environment variables
load_dotenv()
EXCHANGE_RATE_API_KEY = os.getenv(
    "EXCHANGE_RATE_API_KEY"
)  # get api key from https://app.exchangerate-api.com/dashboard
print("Loaded API Key:", EXCHANGE_RATE_API_KEY)


@tool
def get_conversion_factor(base_currency: str, target_currency: str) -> float:
    """
    Fetch the real-time exchange rate from one currency to another using ExchangeRate-API.

    Args:
        base_currency (str): The base currency code (e.g., 'USD').
        target_currency (str): The target currency code (e.g., 'INR').

    Returns:
        float: The latest conversion rate between base and target currency.

    Example:
        get_conversion_factor("USD", "INR") → 83.21
    """
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "conversion_rate" not in data:
        raise ValueError(f"Failed to fetch conversion rate: {data}")

    return data["conversion_rate"]


@tool
def convert_currency(base_currency_value: float, conversion_rate: float) -> float:
    """
    Convert a currency amount using a provided conversion rate.

    Args:
        base_currency_value (float): The amount in the base currency.
        conversion_rate (float): The exchange rate from base to target currency.

    Returns:
        float: The converted amount in the target currency.

    Example:
        convert_currency(10, 83.5) → 835.0
    """
    return base_currency_value * conversion_rate


# ✅ Create LLM and bind tools
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
llm_with_tools = llm.bind_tools([get_conversion_factor, convert_currency])

# ✅ Input prompt with strong instruction
messages = [
    SystemMessage(
        content=(
            "You are a tool-using assistant. If the user asks to convert currency:\n"
            "1. First, call 'get_conversion_factor' to fetch the current exchange rate.\n"
            "2. Then, call 'convert_currency' with the amount and fetched rate.\n"
            "You must always use both tools when conversion is required. Never ask the user for the rate.\n"
            "Reason step-by-step and use tools in sequence when needed."
        )
    ),
    HumanMessage(
        content="What is the conversion factor between USD and INR, and based on that can you convert 10 usd to inr"
    ),
]

# ✅ Invoke the assistant
response = llm_with_tools.invoke(messages)

tool_calls = getattr(response, "tool_calls", [])
while True:
    tool_calls = getattr(response, "tool_calls", None)
    if not tool_calls:
        break  # ✅ No more tool calls, we're done!

    print("\n🛠️ Tool Calls:")
    tool_messages = []

    for call in tool_calls:
        tool_name = call["name"]
        args = call["args"]
        tool_call_id = call["id"]

        print(f"🔧 Calling tool: {tool_name} with args: {args}")

        # ✅ Dynamically dispatch the tool
        if tool_name == "get_conversion_factor":
            result = get_conversion_factor.invoke(args)
        elif tool_name == "convert_currency":
            result = convert_currency.invoke(args)
        else:
            raise ValueError(f"Unknown tool name: {tool_name}")

        # ✅ Append tool response as ToolMessage
        tool_messages.append(
            ToolMessage(tool_call_id=tool_call_id, content=str(result))
        )

    # ✅ Add previous AI response and tool outputs to the conversation
    messages.append(AIMessage(content=response.content, tool_calls=tool_calls))
    messages.extend(tool_messages)

    # ✅ Re-invoke with updated messages
    response = llm_with_tools.invoke(messages)

print(response.content)
