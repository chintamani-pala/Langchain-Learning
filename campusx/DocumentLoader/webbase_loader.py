# type: ignore
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

prompt = PromptTemplate(
    template="Answer the following questionn \n {question} from the following text  - \n {text}",
    input_variables=["question", "text"],
)

parser = StrOutputParser()

url = "https://chintamanipala.in/"
loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser
result = chain.invoke(
    {"question": "what are the skill of the user", "text": docs[0].page_content}
)

print(result)
