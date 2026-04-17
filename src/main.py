from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from analyzer import analyze_email_safe
import os

app = FastAPI(title="Phishender API")

#frontend to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#serve frontend static files
class EmailInput(BaseModel):
    content: str
    input_type: str = "email"  # "email" or "url"

@app.get("/")
async def root():
    return FileResponse("../frontend/index.html")

@app.post("/analyze")
async def analyze(input: EmailInput):
    if not input.content.strip():
        raise HTTPException(status_code=400, detail="No content provided")

    if len(input.content) > 20000:
        raise HTTPException(status_code=400, detail="Input too long (max 20,000 characters)")

    result = analyze_email_safe(input.content, input.input_type)
    return result

@app.get("/health")
async def health():
    return {"status": "ok"}