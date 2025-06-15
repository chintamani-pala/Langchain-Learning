# Langchain - Prompt
# type: ignore

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
# template = """Write a {tone} mail to {company} expressing interest in the {position} position, mentioning {skills} as a key strength. keep it to 4 lines max"""

template = [
    ("system", "You are a professional email writer."),
    (
        "human",
        "Write a {tone} mail to {company} expressing interest in the {position} position, mentioning {skills} as a key strength. Keep it to 4 lines max.",
    ),
]

prompt_template = ChatPromptTemplate.from_messages(template)

prompt = prompt_template.invoke(
    {
        "tone": "professional",
        "company": "Google",
        "position": "Software Engineer",
        "skills": "problem-solving and coding skills",
    }
)


print(prompt)
