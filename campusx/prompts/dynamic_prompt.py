# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
)
# template = PromptTemplate(
#     input_variables=["topic", "language"],
#     template="Explain {topic} in {language} in simple words.",
#     validate_template=True,
# )
# template.save("template.json")

template = load_prompt("template.json")
user_topic = input("Enter a topic: ")
prompt1 = template.invoke({"topic": user_topic, "language": "English"})
prompt2 = template.format(topic=user_topic, language="French")

result1 = model.invoke(prompt1)
result2 = model.invoke(prompt2)

print(result1.content)
print(result2.content)
