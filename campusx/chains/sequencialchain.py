# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt1 = PromptTemplate(
    template="Generate a detailed report on {topic}",
    input_variables=["topic"],
    validate_template=True,
)
prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text \n {text}",
    input_variables=["text"],
    validate_template=True,
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)

chain.get_graph().print_ascii()
