from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Nextjs_Syllabus.pdf")

docs = loader.load()

print(docs[0].page_content)
