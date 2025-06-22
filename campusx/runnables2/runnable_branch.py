# type: ignore
# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.schema.runnable import (
    RunnableSequence,
    RunnableBranch,
    RunnablePassthrough,
    RunnableLambda,
)

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)
prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}", input_variables=["text"]
)

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

parser = StrOutputParser()


def is_summarize_triggered(input):
    print("yes Summarize branch triggered")
    return input


def check_word(input):
    return len(input.split()) > 500


report_gen_chain = RunnableSequence(prompt1, model, parser)
branch_chain = RunnableBranch(
    (
        check_word,
        RunnableSequence(
            RunnableLambda(is_summarize_triggered), prompt2, model, parser
        ),
    ),
    RunnablePassthrough(),
)


final_chain = RunnableSequence(report_gen_chain, branch_chain)
result = final_chain.invoke({"topic": "Russia vs ukraine"})

print(result)
