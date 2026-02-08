

# Opus-Intelligence-Orchestrator 🤖🚀

## 🌟 Overview
The **Opus-Intelligence-Orchestrator** is designed to leverage the **1M token context** and **Adaptive Thinking** of Claude Opus 4.6. It acts as a central engine for autonomous chatbot workflows.

## 🛠️ Tech Stack
- **Language:** Python 3.11+
- **Framework:** FastAPI
- **Model:** Anthropic Claude Opus 4.6
- **Tooling:** Claude Code CLI

## 🚀 Getting Started
1. Clone the repo.
2. Install requirements: `pip install -r requirements.txt`.
3. Set your `ANTHROPIC_API_KEY` in a `.env` file.
4. Run the server: `uvicorn app.main:app --reload`.

## 📡 API Example
Send a POST to `/api/chat`:
```json
{
  "prompt": "How can I optimize this multi-agent system?"
}
