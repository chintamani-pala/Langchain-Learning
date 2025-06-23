# type: ignore
from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt = PromptTemplate(
    template="Write a summery for the following paragraphs - \n {text}",
    input_variables=["text"],
)

parser = StrOutputParser()

loader = TextLoader("text.txt", encoding="utf-8")


docs = loader.load()

# print(type(docs))  # <class 'list'>

# print(len(docs))  # 1

# print(type(docs[0]))  # <class 'langchain_core.documents.base.Document'>

# print(docs[0])

chain = prompt | model | parser


result = chain.invoke({"text": docs[0].page_content})

print(result)
