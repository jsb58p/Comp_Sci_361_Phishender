"""
pipeline.py
Connects all four steps of the pipeline.

analyze_protected(email_text):
  1. injection_filter.filter_input()       — removes hijack phrases from email text
  2. secure_prompt_template.build_prompt() — packages cleaned text into a message for Claude
  3. api_client.call_llm()                 — sends the message to the Claude API
  4. output_validator.validate_response()  — checks Claude's response before returning it

analyze_unprotected(email_text):
  — Sends email text to Claude with no filtering and no secure prompt.
  — Used only in test_pipeline.py to show baseline behavior.
"""

import json

from injection_filter import filter_input
from secure_prompt_template import SYSTEM_PROMPT, build_prompt
from api_client import call_llm
from output_validator import validate_response

BASIC_SYSTEM_PROMPT = (
    "Analyze this email for phishing. "
    "Return JSON with verdict (PHISHING|LEGITIMATE|UNCERTAIN), "
    "confidence (integer 0-100), indicators (list of strings), explanation (string)."
)


def analyze_protected(email_text: str) -> dict:
    filter_result = filter_input(email_text)
    messages = build_prompt(filter_result.clean_text)
    raw = call_llm(SYSTEM_PROMPT, messages)
    validated = validate_response(raw)
    return {
        "verdict": validated.verdict,
        "confidence": validated.confidence,
        "indicators": validated.indicators,
        "explanation": validated.explanation,
        "tips": validated.tips,
        "injection_detected": filter_result.injection_detected,
        "matched_patterns": filter_result.matched_patterns,
    }


def analyze_unprotected(email_text: str) -> dict:
    messages = [{"role": "user", "content": email_text}]
    raw = call_llm(BASIC_SYSTEM_PROMPT, messages)
    try:
        clean = raw.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean)
        return {
            "verdict": data.get("verdict", "UNKNOWN"),
            "confidence": data.get("confidence", 0),
            "explanation": data.get("explanation", ""),
            "injection_detected": False,
        }
    except json.JSONDecodeError:
        return {
            "verdict": "PARSE_ERROR",
            "confidence": 0,
            "explanation": raw[:300],
            "injection_detected": False,
        }