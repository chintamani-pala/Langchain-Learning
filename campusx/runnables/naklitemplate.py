# type: ignore
from runnable import Runnable


class NakliTemplate(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)


# template = NakliTemplate(
#     template="Write a {length} poem about {topic}", input_variables=["length", "topic"]
# )

# prompt = template.format({"length": "short", "topic": "india"})

# print(prompt)
