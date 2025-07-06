# type: ignore
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from langsmith import Client
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import requests
from dotenv import load_dotenv

load_dotenv()


client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))
prompt = client.pull_prompt("hwchase17/react:d15fe3c4", include_model=True)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

search_tool = DuckDuckGoSearchRun()


@tool
def get_wheather_data(city: str) -> str:
    """
    This function fetches the current wheather data for a given city and return the wheather information
    """
    url = f"https://api.weatherstack.com/current?access_key=7f02f1dc0057d1b6a23f73935f51f05a&query={city}"
    response = requests.get(url)
    data = response.json()
    return data


agent = create_react_agent(
    llm=llm, tools=[search_tool, get_wheather_data], prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent, tools=[search_tool, get_wheather_data], verbose=True
)

response = agent_executor.invoke(
    {"input": "What is the capital of odisha, then find it's current weather condition"}
)
print(response)
