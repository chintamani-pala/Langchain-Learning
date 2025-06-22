# type: ignore

from runnable import Runnable
from naklitemplate import NakliTemplate
from naklillm import NakliLLM
from naklistroutputparser import NakliStrOutputParser


class RunnableConnector(Runnable):
    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data


# template = NakliTemplate(
#     template="Write a {length} poem about {topic}", input_variables=["length", "topic"]
# )

# llm = NakliLLM()

# parser = NakliStrOutputParser()

# chain = RunnableConnector([template, llm, parser])


# result = chain.invoke({"length": "short", "topic": "india"})

# print(result)
