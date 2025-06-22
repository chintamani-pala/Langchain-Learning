# type: ignore
from naklillm import NakliLLM
from naklitemplate import NakliTemplate
from naklistroutputparser import NakliStrOutputParser
from runnableConnector import RunnableConnector

template1 = NakliTemplate(
    template="Write a joke about {topic}", input_variables=["topic"]
)
template2 = NakliTemplate(
    template="Explain the following joke {response}", input_variables=["response"]
)

llm = NakliLLM()

parser = NakliStrOutputParser()

chain1 = RunnableConnector([template1, llm])
chain2 = RunnableConnector([template2, llm, parser])


final_chain = RunnableConnector([chain1, chain2])
result = final_chain.invoke({"topic": "AI"})

print(result)
