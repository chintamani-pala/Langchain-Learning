# type: ignore
import random
from runnable import Runnable


class NakliLLM(Runnable):
    def __init__(self):
        print("LLM created")

    def invoke(self, prompt):
        responseList = [
            "Delhi is the capital of india.",
            "IPL is a cricket league",
            "AI stands for artificial inteligence",
        ]
        return {"response": random.choice(responseList)}

    def predict(self, prompt):
        responseList = [
            "Delhi is the capital of india.",
            "IPL is a cricket league",
            "AI stands for artificial inteligence",
        ]
        return {"response": random.choice(responseList)}


# llm = NakliLLM()

# result = llm.predict("What is the capital of india")

# print(result)
