"""
output_validator.py
Step 4 of 4 in the protected pipeline.

Receives Claude's raw response text from pipeline.py.
Checks that it is valid JSON with the correct fields and values.
Returns a ValidatedResponse object if it passes.
Raises ValidationError if it fails.
"""

import json
from dataclasses import dataclass

VALID_VERDICTS = {"PHISHING", "LEGITIMATE", "UNCERTAIN"}
REQUIRED_KEYS = {"verdict", "confidence", "indicators", "explanation"}


class ValidationError(Exception):
    pass


@dataclass
class ValidatedResponse:
    verdict: str
    confidence: int
    indicators: list[str]
    explanation: str


def validate_response(raw: str) -> ValidatedResponse:
    try:
        clean = raw.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean)
    except json.JSONDecodeError as e:
        raise ValidationError(f"Response is not valid JSON: {e}") from e

    if not isinstance(data, dict):
        raise ValidationError("Response JSON is not an object.")

    missing = REQUIRED_KEYS - data.keys()
    if missing:
        raise ValidationError(f"Response missing required keys: {missing}")

    if data["verdict"] not in VALID_VERDICTS:
        raise ValidationError(
            f"Invalid verdict '{data['verdict']}'. Must be one of {VALID_VERDICTS}."
        )

    if not isinstance(data["confidence"], int) or not (0 <= data["confidence"] <= 100):
        raise ValidationError(
            f"Invalid confidence '{data['confidence']}'. Must be integer 0-100."
        )

    if not isinstance(data["indicators"], list) or not all(
        isinstance(i, str) for i in data["indicators"]
    ):
        raise ValidationError("'indicators' must be a list of strings.")

    if not isinstance(data["explanation"], str) or not data["explanation"].strip():
        raise ValidationError("'explanation' must be a non-empty string.")

    return ValidatedResponse(
        verdict=data["verdict"],
        confidence=data["confidence"],
        indicators=data["indicators"],
        explanation=data["explanation"],
    )