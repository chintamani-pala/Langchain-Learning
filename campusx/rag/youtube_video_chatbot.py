# type: ignore
import sys
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser


# === 1. Fetch transcript once ===
def get_youtube_transcript(video_id):
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.list(video_id)
    is_transcript_available = transcript_list.find_generated_transcript(["en"])
    if not is_transcript_available:
        print("This video does not have the english subtitles.")
        sys.exit()
    transcript = ytt_api.fetch(video_id, languages=["en"])

    final_transcript_text = []
    for transctipt_item in transcript:
        final_transcript_text.append(transctipt_item.text)

    final_transcript_text = "".join(final_transcript_text)
    return final_transcript_text


# === 2. Split transcript into chunks ===
def split_text_to_chunks_and_make_documents(transcript_text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.create_documents([transcript_text])


# === 3. Setup FAISS vectorstore ===
def setup_vectorstore(documents):
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.from_documents(documents, embedding=embedding_model)


# === 4. Define Prompt ===
prompt = PromptTemplate(
    template="""
You are a helpful assistant.
Answer only from the provided transcript context.
If the context is insufficient, just say "don't know".
Explain in a clear, simple, and human-friendly way.

Context:
{context}

Question: {question}
""",
    input_variables=["context", "question"],
)

# === 5. Initialize once ===
video_id = "X0btK9X0Xnk"
transcript_text = get_youtube_transcript(video_id)
chunks = split_text_to_chunks_and_make_documents(transcript_text)
vectorstore = setup_vectorstore(chunks)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")


# structure the context and question for the PromptTemplate
def get_structured_context(inputs):
    return {
        "context": "\n".join([doc.page_content for doc in inputs["context"]]),
        "question": inputs["question"],
    }


# === 6. Build question-answer chain ===
parallel_chain = RunnableParallel(
    {
        "context": RunnableLambda(lambda q: retriever.invoke(q)),
        "question": RunnablePassthrough(),
    }
)
retrieval_chain = (
    parallel_chain
    | RunnableLambda(get_structured_context)
    | prompt
    | llm
    | StrOutputParser()
)

# retrieval_chain.get_graph().print_ascii()
# +---------------------------------+
# | Parallel<context,question>Input |
# +---------------------------------+
#             **         **
#           **             **
#          *                 *
#   +--------+          +-------------+
#   | Lambda |          | Passthrough |
#   +--------+          +-------------+
#             **         **
#               **     **
#                 *   *
# +----------------------------------+
# | Parallel<context,question>Output |
# +----------------------------------+
#                   *
#                   *
#                   *
#              +--------+
#              | Lambda |
#              +--------+
#                   *
#                   *
#                   *
#          +----------------+
#          | PromptTemplate |
#          +----------------+
#                   *
#                   *
#                   *
#      +------------------------+
#      | ChatGoogleGenerativeAI |
#      +------------------------+
#                   *
#                   *
#         +-----------------+
#         | StrOutputParser |
#         +-----------------+
#                   *
#                   *
#                   *
#       +-----------------------+
#       | StrOutputParserOutput |
#       +-----------------------+

# === 7. Interactive Q&A loop ===
while True:
    question = input("Enter your question (or 'exit'): ")
    if question.lower() == "exit":
        break

    answer = retrieval_chain.invoke(question)
    print(f"\nAnswer: {answer}\n")
