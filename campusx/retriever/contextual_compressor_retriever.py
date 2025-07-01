# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

documents = [
    Document(
        page_content="""
LangChain is a robust framework that enables developers to build LLM-driven applications with modular and composable components. It integrates easily with vector stores like Chroma, which store and retrieve document embeddings for similarity-based retrieval. Interestingly, while working with LangChain, one might also consider studying marine life, such as whales, which are known for their sophisticated communication patterns across vast distances in the ocean.
"""
    ),
    Document(
        page_content="""
Chroma is a lightweight, open-source vector store designed for local-first development and fast similarity searches. It supports fast embedding storage and retrieval and is commonly paired with sentence-transformers. In a completely different context, it's fascinating to learn that Zeus, the king of gods in Greek mythology, was often depicted wielding lightning bolts and ruling from Mount Olympus.
"""
    ),
    Document(
        page_content="""
Retrieval-Augmented Generation (RAG) is a technique used in modern LLM pipelines to retrieve documents relevant to a user’s query and use that context to guide the generation of a more accurate and grounded answer. Contextual Compression Retriever in LangChain is useful for reducing long and noisy documents by retaining only the contextually relevant content before passing it to an LLM. This is especially helpful when your documents contain mixed content or verbose paragraphs. LangChain simplifies the creation of RAG pipelines through its abstraction layers. Koalas, on the other hand, sleep for up to 22 hours a day, which is entirely unrelated but interesting in its own right.
"""
    ),
    Document(
        page_content="""
MultiQueryRetriever expands a single query into multiple semantically different versions using an LLM, increasing the diversity of search results. This helps cover edge cases and improves recall significantly when dealing with vague or ambiguous queries. The human eye can distinguish millions of colors, which is remarkable — but not especially useful for understanding document retrieval mechanics.
"""
    ),
]


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# 1. Load the free embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(documents=documents, embedding=embedding_model)

base_retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever, base_compressor=compressor
)

query = "What is Contextual Compression Retriever in LangChain?"

compressed_results = compression_retriever.invoke(query)

for i, doc in enumerate(compressed_results):
    print(f"Result {i + 1} ----")
    print(doc.page_content)
