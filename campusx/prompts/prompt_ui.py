# type: ignore
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


st.header("Research Tool")
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.2,
    max_output_token=2,
)

input_text = st.text_input("Enter your query here:", key="query")
if st.button("Submit"):
    result = model.invoke(input_text)
    st.write(result.content)
