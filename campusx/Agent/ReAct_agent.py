# type: ignore
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langsmith import Client
from langchain_google_genai import ChatGoogleGenerativeAI
import os

from dotenv import load_dotenv

load_dotenv()

client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))
prompt = client.pull_prompt("hwchase17/react:d15fe3c4", include_model=True)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

search_tool = DuckDuckGoSearchRun()

agent = create_react_agent(llm=llm, tools=[search_tool], prompt=prompt)

agent_executor = AgentExecutor(agent=agent, tools=[search_tool], verbose=True)

response = agent_executor.invoke(
    {"input": "What are the 3 ways to reach chennai from banglore"}
)
print(response)
