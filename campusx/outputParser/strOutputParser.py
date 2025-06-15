# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 1st prompt
template1 = PromptTemplate(
    template="write a details report on {topic}",
    input_variables=["topic"],
    validate_template=False,
)

# 2nd prompt
template2 = PromptTemplate(
    template="Write a 5 lines summary on the following text /n {text}",
    input_variables=["text"],
    validate_template=False,
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "black hole"})
print(result)
