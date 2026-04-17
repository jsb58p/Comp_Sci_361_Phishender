"""
api_client.py
Step 3 of 4 in the protected pipeline.

Receives the system prompt and message list from pipeline.py.
Sends them to the Claude API.
Returns Claude's raw response text to pipeline.py.

Requires environment variable ANTHROPIC_API_KEY to be set before running.
"""

import os
import anthropic
from dotenv import load_dotenv

load_dotenv()

def call_llm(system_prompt: str, messages: list[dict]) -> str:
    client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1000,
        system=system_prompt,
        messages=messages,
    )
    return response.content[0].text