from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pipeline import analyze_protected
from audit_log import log_decision

app = FastAPI(title="Phishender API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailInput(BaseModel):
    content: str
    input_type: str = "email"

@app.get("/")
async def root():
    return FileResponse("index.html")

@app.post("/analyze")
async def analyze(input: EmailInput):
    if not input.content.strip():
        raise HTTPException(status_code=400, detail="No content provided")

    if len(input.content) > 20000:
        raise HTTPException(status_code=400, detail="Input too long (max 20,000 characters)")

    result = analyze_protected(input.content)

    result["verdict"] = result["verdict"].lower()
    if result["verdict"] == "uncertain":
        result["verdict"] = "suspicious"

    log_decision(input.input_type, input.content, result)

    return result


@app.get("/health")
async def health():
    return {"status": "ok"}