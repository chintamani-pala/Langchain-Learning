# type: ignore
from runnable import Runnable


class NakliStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data["response"]
