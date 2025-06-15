# type: ignore
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    import getpass

    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")


llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
result = llm.invoke("what is the square root of 49?")
print(result.content)
