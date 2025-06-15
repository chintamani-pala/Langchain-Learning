# type: ignore
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpfull customer support agent"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),
    ]
)
chat_history = []
with open("chat_history.txt", "r") as f:
    chat_history.append(f.readlines())

print(chat_history)
prompt = chat_template.invoke(
    {"chat_history": chat_history[0], "query": "Where is my refund"}
)

print(prompt)
