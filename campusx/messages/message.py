# type: ignore
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", model_kwargs={"max_output_token": 15}
)

messages = [
    SystemMessage(content="You are a helpfull assistant"),
    HumanMessage(content="Tell me about langchain?"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))


print(messages)
