# type: ignore
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
# 1. Load the free embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


documents = [
    Document(
        page_content="A balanced diet that includes proteins, healthy fats, and complex carbs improves overall energy levels."
    ),
    Document(
        page_content="Sleep is essential for restoring the body's energy and supporting mental health."
    ),
    Document(
        page_content="Daily exercise boosts mood, improves stamina, and increases long-term energy."
    ),
    Document(
        page_content="Chronic stress can lead to fatigue and negatively impact your immune system."
    ),
    Document(
        page_content="Staying hydrated is critical for maintaining focus, energy, and metabolic function."
    ),
    Document(
        page_content="Iron deficiency is one of the most common causes of low energy in adults."
    ),
    Document(
        page_content="Yoga and meditation not only calm the mind but also help in managing stress-induced fatigue."
    ),
    Document(
        page_content="Eating too much sugar can cause temporary energy spikes followed by crashes."
    ),
    Document(
        page_content="People with sleep apnea often experience constant tiredness despite spending long hours in bed."
    ),
    Document(
        page_content="Vitamin B12 helps convert food into energy and supports nerve function."
    ),
    # 🔀 Ambiguous or indirect documents
    Document(
        page_content="Some people just don't feel like themselves lately, and it's hard to pinpoint why."
    ),
    Document(
        page_content="Working from home has changed sleep habits and reduced overall movement."
    ),
    Document(
        page_content="Feeling low can sometimes stem from deeper issues that aren't immediately obvious."
    ),
    Document(
        page_content="It’s common to feel worn out after staring at screens all day, but is that the only reason?"
    ),
    Document(
        page_content="Changes in weather or seasons can impact mood and energy in subtle ways."
    ),
]


vectorstore = FAISS.from_documents(documents=documents, embedding=embedding_model)

multiquery_retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}), llm=llm
)

print(multiquery_retriever)
query = "I don't feel like myself — what's wrong? with mood"

simple_retriever = vectorstore.similarity_search(query)
multiquery_results = multiquery_retriever.invoke(query)
print("Simple similarity search")
for i, doc in enumerate(simple_retriever):
    print(f"Result {i + 1}---")
    print(doc.page_content)

print("#" * 150)
print("Multiquery similarity search")
for i, doc in enumerate(multiquery_results):
    print(f"Result {i + 1}---")
    print(doc.page_content)
