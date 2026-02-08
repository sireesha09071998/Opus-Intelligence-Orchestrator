import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load the API key from your .env file
load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

async def get_claude_response(user_prompt: str):
    """
    Connects to Opus 4.6 and returns the AI reasoning + response.
    """
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022", # Update to "claude-opus-4-6" when key is active
            max_tokens=4096,
            thinking={
                "type": "enabled",
                "budget_tokens": 1024
            },
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"Error calling Anthropic: {e}")
        return "Sorry, I encountered an error processing that request."
