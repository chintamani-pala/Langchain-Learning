# type:ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate

load_dotenv()

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpfull {domain} expert"),
        ("human", "Explain in simple term what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "web development", "topic": "fastapi"})


# Print the generated prompt
print(prompt)


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

result = model.invoke(prompt)

print(result.content)
