# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()


prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Generate a Linkedin post about {topic}", input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model, parser),
        "linkedin": RunnableSequence(prompt2, model, parser),
    }
)


result = parallel_chain.invoke({"topic": "AI"})

print("tweet", result["tweet"])
print("linkedin", result["linkedin"])


parallel_chain.get_graph().print_ascii()
