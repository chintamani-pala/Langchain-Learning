from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
LangChain helps developers build LLM-powered applications using composable components.
It handles prompt templates, chains, memory, retrieval, and agents with ease.
This makes it a go-to choice for production-ready AI apps.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,  # Maximum characters per chunk
    chunk_overlap=5,  # Overlap between chunks for context preservation
)

chunks = splitter.split_text(text)

print(chunks)
