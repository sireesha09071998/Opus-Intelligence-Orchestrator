from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .services import get_claude_response

app = FastAPI(title="Opus Intelligence Orchestrator")

# This defines what the incoming data should look like
class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "online", "engine": "Opus 4.6"}

@app.post("/api/chat")
async def chat(request: ChatRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")
    
    # Get the answer from our service file
    response = await get_claude_response(request.prompt)
    
    return {"success": True, "response": response}
