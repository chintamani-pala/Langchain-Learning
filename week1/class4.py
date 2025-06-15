# type: ignore
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1)

chat_history = []

system_message = SystemMessage("You are a helpful AI assistant.")

chat_history.append(system_message)

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting the chat.")
        break
    human_message = HumanMessage(query)
    chat_history.append(human_message)
    response = model.invoke(chat_history)
    ai_message = AIMessage(response.content)
    chat_history.append(ai_message)
    print(f"AI: {response.content}")

print("--------Message History--------")
print(chat_history)
