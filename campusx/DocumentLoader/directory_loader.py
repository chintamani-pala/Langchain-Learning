# type: ignore
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(path="syllabus", glob="*.pdf", loader_cls=PyPDFLoader)

docs = loader.load()

print(docs[4])
