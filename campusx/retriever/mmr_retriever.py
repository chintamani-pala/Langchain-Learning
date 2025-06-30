# type: ignore
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

# 1. Load the free embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Sample text data
documents = [
    Document(page_content="LangChain is used to build LLM-based applications."),
    Document(page_content="Langchain is used to create AI agents using Python."),
    Document(page_content="LangChain enables prompt management and chaining for LLMs."),
    Document(page_content="Chroma is an open-source vector database."),
    Document(page_content="MiniLM is a small and fast embedding model."),
    Document(page_content="Vector stores help in storing and retrieving embeddings."),
    Document(page_content="You can build chatbots using LangChain and OpenAI."),
    Document(page_content="Chroma stores document embeddings for semantic search."),
    Document(
        page_content="random text that is not related to LangChain or embeddings."
    ),
]

# 3. Create the Chroma vector store
vectorstore = FAISS.from_documents(documents=documents, embedding=embedding_model)

# 4. Create retriever with similarity score filtering
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"lambda_mult": 0.5, "k": 2},
)

# 5. Querying
query = "What is LangChain"
results = retriever.invoke(query)

# 6. Output results
for idx, doc in enumerate(results):
    print(f"\nResult {idx + 1}:")
    print(doc.page_content)
