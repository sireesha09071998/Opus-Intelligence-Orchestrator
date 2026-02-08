#!/bin/bash

echo "🚀 Starting setup for Opus-Intelligence-Orchestrator..."

# 1. Create a Python Virtual Environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# 2. Activate the Virtual Environment
echo "🔄 Activating environment..."
source venv/bin/activate

# 3. Upgrade Pip (Python's package manager)
echo "🆙 Upgrading pip..."
pip install --upgrade pip

# 4. Install requirements
if [ -f requirements.txt ]; then
    echo "📥 Installing libraries from requirements.txt..."
    pip install -r requirements.txt
else
    echo "❌ requirements.txt not found! Installing basics..."
    pip install fastapi uvicorn anthropic python-dotenv
fi

# 5. Create a .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env template..."
    echo "ANTHROPIC_API_KEY=your_key_here" > .env
    echo "PORT=8000" >> .env
fi

echo "✅ Setup Complete!"
echo "👉 To start your server, run: source venv/bin/activate && uvicorn app.main:app --reload"
