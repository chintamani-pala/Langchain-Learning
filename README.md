# LangChain CampusX AI Projects

Welcome to the **LangChain CampusX AI Projects** repository!  
This repo contains hands-on projects, experiments, and code samples for building advanced AI applications using [LangChain](https://github.com/langchain-ai/langchain), Google Gemini, OpenAI, Anthropic, HuggingFace, and more.  
It is designed for learners and developers who want to explore LLMs, prompt engineering, tool use, retrieval-augmented generation, and practical AI workflows.

---

## 📂 Project Structure

- **models/**: Demos for using OpenAI, Google Gemini, and Anthropic chat models.
- **chains/**: Sequential, parallel, and conditional chains for multi-step LLM workflows.
- **prompts/**: Prompt engineering, dynamic prompts, and Streamlit prompt UIs.
- **outputParser/**: Structured output parsing with Pydantic, JSON, and custom schemas.
- **structuredOutput/**: TypedDict, Pydantic, and JSON schema-based structured outputs.
- **retriever/**: Vector store retrieval, multi-query, MMR, and Wikipedia retrievers.
- **rag/**: Retrieval-Augmented Generation (RAG) pipelines (e.g., YouTube video chatbot).
- **DocumentLoader/**: Loading and splitting text, PDF, and web documents.
- **toolcall/**: Tool-calling with LLMs, including currency conversion with real APIs.
- **tools/**: Custom tools, toolkits, and integrations (e.g., DuckDuckGo, shell).
- **textspliter/**: Text splitting strategies for chunking documents.

---

## 🚀 Key Features

- **LLM Integration**: Use Google Gemini, OpenAI GPT, Anthropic Claude, and HuggingFace models.
- **Prompt Engineering**: Templates, dynamic prompts, and chat prompt workflows.
- **Tool Use**: Call external tools/APIs from LLMs (e.g., currency conversion, search).
- **RAG Pipelines**: Retrieval-augmented generation with vector stores and custom retrievers.
- **Structured Output**: Parse LLM outputs into JSON, Pydantic, or TypedDict formats.
- **Document Loading**: Load and split text, PDF, and web data for AI processing.
- **Streamlit Apps**: Interactive UIs for prompt testing and research tools.

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
   - Edit `campusx/.env` and add your API keys for OpenAI, Anthropic, Google, and ExchangeRate-API.

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

## 📚 Learning Goals

- Understand how to build LLM-powered apps with LangChain.
- Learn prompt engineering and output parsing.
- Integrate external tools and APIs with LLMs.
- Build retrieval-augmented and multi-step reasoning pipelines.
- Experiment with document loaders and vector stores.

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