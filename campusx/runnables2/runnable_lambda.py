# type: ignore
# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)

load_dotenv()


def word_counter(text):
    return len(text.split())


prompt = PromptTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)
parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "word_Count": RunnableLambda(word_counter),
    }
)


final_chain = RunnableSequence(joke_gen_chain, parallel_chain)
result = final_chain.invoke({"topic": "AI"})

print(result)
