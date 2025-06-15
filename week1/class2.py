# type: ignore
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


messages = [
    SystemMessage("You are an export in social media content strategy"),
    HumanMessage("Give a short tip to create engaging port on instagram"),
]

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
result = llm.invoke(messages)
print(result.content)
