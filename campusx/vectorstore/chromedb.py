# type: ignore
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

# Documents
docs = [
    Document(
        page_content="LangChain helps build LLM-powered apps.",
        metadata={"topic": "LangChain"},
    ),
    Document(
        page_content="React is a frontend library for UI components.",
        metadata={"topic": "React"},
    ),
]


# Chroma vector store
vector_store = Chroma(
    embedding_function=OpenAIEmbeddings(),
    persist_directory="chroma_db",
    collection_name="sample",
)

# Add docs
vector_store.add_documents(docs)

# view Documents
all_data = vector_store.get(include=["embeddings", "documents", "metadata"])
print(all_data)


# Search documents
search_result = vector_store.similarity_search(query="What is React", k=1)
print(search_result)


# update document
updated_doc1 = Document(
    page_content="""
React is a popular JavaScript library for building user interfaces.
It uses a component-based architecture where UI pieces are encapsulated in reusable functions or classes.
""",
    metadata={"topic": "React"},
)
vector_store.update_document(document_id="Some document id", document=updated_doc1)


# Delete document
vector_store.delete(ids=["Some document id"])
vector_store.persist()

print("✅ Vector store initialized and documents embedded.")
