# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"],
    validate_template=True,
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)

chain.get_graph().print_ascii()
