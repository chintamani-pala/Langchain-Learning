# type: ignore
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document

# 1. Load the free embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 2. Sample text data
documents = [
    Document(page_content="LangChain is used to build LLM-based applications."),
    Document(page_content="Langchain is used to create ai agents using python"),
    Document(page_content="Chroma is an open-source vector database."),
    Document(page_content="MiniLM is a small and fast embedding model."),
    Document(page_content="random text"),
]

# 3. Create the Chroma vector store
vectorstore = Chroma.from_documents(
    documents=documents, embedding=embedding_model, collection_name="my_collection"
)

# 4. Create retriever with similarity score filtering
retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.3, "k": 2},
)

# 5. Querying
query = "What is LangChain used for?"
results = retriever.invoke(query)

# 6. Output results
for idx, doc in enumerate(results):
    print(f"\nResult {idx + 1}:")
    print(doc.page_content)
