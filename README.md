 Agentic-AI-project
 🚀 StartupPilot AI

An Agentic AI application that acts as an intelligent Startup Consultant.

Instead of answering like a chatbot, StartupPilot AI coordinates multiple AI agents that collaborate to analyze a startup idea, perform market research, evaluate competitors, generate SWOT analysis, recommend a business model, create marketing strategies, and produce an investor-ready business report.

---

 ✨ Features

- Multi-Agent Workflow
- Market Research
- Competitor Analysis
- SWOT Analysis
- Business Model Canvas
- Marketing Strategy Generator
- Investor Pitch Generator
- PDF Business Report
- Interactive Streamlit Dashboard
- LangGraph Agent Orchestration
- Gemini API Integration

---

 🏗️ Architecture

User Idea

↓

Planner Agent

↓

Market Research Agent

↓

Competitor Agent

↓

SWOT Agent

↓

Business Model Agent

↓

Marketing Agent

↓

Pitch Deck Agent

↓

Report Generator

↓

Final Business Report

---

## 🛠️ Tech Stack

Python

LangGraph

LangChain

Google Gemini

Streamlit

FAISS

Sentence Transformers

Plotly

Pydantic

ReportLab

---

## Installation

Install dependencies

```bash
pip install -r requirements.txt
```

Create .env

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run

```bash
streamlit run app.py
```

---

 Folder Structure

```
agents/
services/
prompts/
models/
workflows/
utils/
reports/
```

---

## Future Improvements

Web Search Agent

Financial Forecast Agent

Investment Scoring

RAG Knowledge Base

Voice Assistant

Docker Deployment

CI/CD Pipeline

---

## License

MIT
