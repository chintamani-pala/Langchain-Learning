# type: ignore
from runnables.naklitemplate import NakliTemplate
from runnables.naklillm import NakliLLM


class NakliLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result["response"]


# template = NakliTemplate(
#     template="Write a {length} poem about {topic}", input_variables=["length", "topic"]
# )

# llm = NakliLLM()

# prompt = template.format()
# chain = NakliLLMChain(llm=llm, prompt=prompt)


# chain.run({"length": "short", "topic": "india"})
# print(prompt)
