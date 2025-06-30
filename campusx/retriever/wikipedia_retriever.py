# type: ignore
from langchain_community.retrievers import WikipediaRetriever


retriver = WikipediaRetriever(top_k_results=2, lang="en")

query = "What is AI"

docs = retriver.invoke(query)

for i, doc in enumerate(docs):
    print(f"\n ---Result {i + 1}---")
    print(f"Content: \n {doc.page_content}...")
