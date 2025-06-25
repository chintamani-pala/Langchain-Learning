from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=100,
    chunk_overlap=10,
)

code = """
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

def main():
    calc = Calculator()
    print(calc.add(2, 3))
    print(calc.multiply(4, 5))

main()
"""

chunks = splitter.split_text(code)

for i, chunk in enumerate(chunks):
    print(f"🔹 Chunk {i + 1}:\n{chunk}\n")
