# type: ignore
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},  # Use "cuda" for GPU
)
result = embedding.embed_query("What is the capital of India?")
print(str(result))
