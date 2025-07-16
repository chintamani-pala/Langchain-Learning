# LangChain CampusX AI Projects

Welcome to the **LangChain CampusX AI Projects** repository!  
This repo contains hands-on projects, experiments, and code samples for building advanced AI applications using [LangChain](https://github.com/langchain-ai/langchain), Google Gemini, OpenAI, Anthropic, HuggingFace, and more.  
It is designed for learners and developers who want to explore LLMs, prompt engineering, tool use, retrieval-augmented generation, and practical AI workflows.

---

## 📂 Project Structure

- [**models/**](campusx/models/)(campusx/models/): Demos for using OpenAI, Google Gemini, and Anthropic chat models.
- [**prompts/**](campusx/prompts/): Prompt engineering, dynamic prompts, and Streamlit prompt UIs.
- [**structuredOutput/**](campusx/structuredOutput/): TypedDict, Pydantic, and JSON schema-based structured outputs.
- [**outputParser/**](campusx/outputParser/): Structured output parsing with Pydantic, JSON, and custom schemas.
- [**chains/**](campusx/chains/): Sequential, parallel, and conditional chains for multi-step LLM workflows.
- [**runnables/**](campusx/runnables/): Core LangChain components (LLMs, prompts, functions) that can be invoked, composed, streamed, or chained declaratively.
- [**DocumentLoader/**](campusx/DocumentLoader/): Loading and splitting text, PDF, and web documents.
- [**textspliter/**](campusx/textspliter/): Text splitting strategies for chunking documents.
- [**retriever/**](campusx/retriever/): Vector store retrieval, multi-query, MMR, and Wikipedia retrievers.
- [**rag/**](campusx/rag/): Retrieval-Augmented Generation (RAG) pipelines (e.g., YouTube video chatbot).
- [**tools/**](campusx/tools/): Custom tools, toolkits, and integrations (e.g., DuckDuckGo, shell).
- [**toolcall/**](campusx/toolcall/): Tool-calling with LLMs, including currency conversion with real APIs.
- [**Agent/**](campusx/Agent/): Agent-based workflows, including ReAct agent.

---

## 🚀 Key Features

- **LLM Integration**: Use Google Gemini, OpenAI GPT, Anthropic Claude, and HuggingFace models.
- **Prompt Engineering**: Templates, dynamic prompts, and chat prompt workflows.
- **Tool Use**: Call external tools/APIs from LLMs (e.g., currency conversion, search).
- **RAG Pipelines**: Retrieval-augmented generation with vector stores and custom retrievers.
- **Structured Output**: Parse LLM outputs into JSON, Pydantic, or TypedDict formats.
- **Document Loading**: Load and split text, PDF, and web data for AI processing.
- **Streamlit Apps**: Interactive UIs for prompt testing and research tools.
- **Agent Workflows**: Implement ReAct and other agent-based reasoning with tool use.

---

## 🛠️ Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/langchain-campusx-ai-projects.git
   cd langchain-campusx-ai-projects
   ```
2. **Install dependencies**
   ```sh
   pip install -r campusx/requirements.txt
   ```
3. **Configure API keys**

   - Copy the example environment file and fill in your API keys:
     ```sh
     cp campusx/.env.example campusx/.env
     ```
   - Edit `campusx/.env` and add your API keys for OpenAI, Anthropic, Google,ExchangeRate-API, langsmith and [weatherstack](https://weatherstack.com/dashboard).

   > **Note:** Get your [ExchangeRate-API key](https://app.exchangerate-api.com/dashboard) for currency conversion demos.

---

## 📖 Example Projects

### Currency Conversion Tool

This project includes a tool-using LLM agent that can:

- Fetch real-time currency conversion rates using ExchangeRate-API.
- Convert amounts between currencies using up-to-date rates.
- Demonstrates multi-step tool use and reasoning.

See [`campusx/toolcall/currency_conversion_project.py`](campusx/toolcall/currency_conversion_project.py) for details.

---

### YouTube Video Chatbot (RAG)

This project demonstrates a Retrieval-Augmented Generation (RAG) chatbot that:

- Fetches and processes YouTube video transcripts.
- Splits transcripts into chunks and creates a vector store for semantic search.
- Uses a retriever to find relevant transcript parts for a user's question.
- Answers questions using Google Gemini, grounded in the actual video content.

See [`campusx/rag/youtube_video_chatbot.py`](campusx/rag/youtube_video_chatbot.py) for the full implementation.

---

### ReAct Agent

This project demonstrates the use of a **ReAct agent** (Reasoning and Acting) with LangChain and Google Gemini:

- Uses the ReAct paradigm to combine reasoning steps with tool use.
- Integrates external tools like DuckDuckGo search for real-time information retrieval.
- Utilizes LangSmith for prompt management and experiment tracking.
- Example: The agent can answer questions like "What are the 3 ways to reach Chennai from Bangalore?" by searching the web and reasoning step by step.

See [`campusx/Agent/ReAct_agent.py`](campusx/Agent/ReAct_agent.py) for the implementation and usage.

---

### ReAct Agent 2

This project extends the ReAct agent workflow by allowing the agent to use **multiple tools** in a single reasoning chain, including both web search and weather data retrieval.

- Uses the ReAct paradigm to combine reasoning steps with tool use.
- Integrates external tools like DuckDuckGo search for real-time information retrieval.
- Adds a custom tool to fetch current weather data for any city using the Weatherstack API.
- Utilizes LangSmith for prompt management and experiment tracking.
- Example: The agent can answer questions like  
  _"What is the capital of Odisha, then find its current weather condition?"_  
  by searching for the capital and then fetching the weather for that city.

See [`campusx/Agent/ReAct_agent_2.py`](campusx/Agent/ReAct_agent_2.py) for the implementation and usage.

---

## 📚 Learning Goals

- Understand how to build LLM-powered apps with LangChain.
- Learn prompt engineering and output parsing.
- Integrate external tools and APIs with LLMs.
- Build retrieval-augmented and multi-step reasoning pipelines.
- Experiment with document loaders and vector stores.
- Explore agent-based workflows like ReAct for advanced reasoning.

---

## 🤝 Contributing

Pull requests, issues, and suggestions are welcome!  
Feel free to fork and adapt for your own AI experiments.

---

## 📄 License

This repository is for educational purposes.  
See [LICENSE](LICENSE) for details.

---

**Happy Learning!**
