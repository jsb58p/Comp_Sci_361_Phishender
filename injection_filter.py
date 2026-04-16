"""
injection_filter.py
Step 1 of 4 in the protected pipeline.

Receives raw email text.
Scans it for prompt injection phrases.
Replaces matches with [INJECTION ATTEMPT REDACTED].
Returns cleaned text to pipeline.py.
"""

import re
from dataclasses import dataclass, field

INJECTION_PATTERNS = [
    r"ignore\s+(all\s+)?(previous|prior|above)\s+instructions?",
    r"disregard\s+(all\s+)?(previous|prior|above)\s+instructions?",
    r"forget\s+(all\s+)?(previous|prior|above)\s+instructions?",
    r"override\s+(your\s+)?(previous\s+)?instructions?",
    r"you\s+are\s+now\s+a",
    r"new\s+instructions?:",
    r"system\s*:\s*",
    r"<\s*/?system\s*>",
    r"act\s+as\s+(if\s+you\s+are\s+)?a",
    r"return\s+(only\s+)?(legitimate|phishing|uncertain)",
    r"classify\s+this\s+as\s+(legitimate|phishing|uncertain)",
    r"your\s+(new\s+)?role\s+is",
    r"pretend\s+(that\s+)?you",
    r"from\s+now\s+on",
    r"do\s+not\s+analyze",
    r"stop\s+analyzing",
]

COMPILED_PATTERNS = [re.compile(p, re.IGNORECASE) for p in INJECTION_PATTERNS]
REDACTION_MARKER = "[INJECTION ATTEMPT REDACTED]"


@dataclass
class FilterResult:
    clean_text: str
    injection_detected: bool
    matched_patterns: list[str] = field(default_factory=list)


def filter_input(raw_text: str) -> FilterResult:
    clean = raw_text
    matched = []
    for pattern in COMPILED_PATTERNS:
        found = pattern.findall(clean)
        if found:
            matched.extend([str(f) for f in found])
            clean = pattern.sub(REDACTION_MARKER, clean)
    return FilterResult(
        clean_text=clean,
        injection_detected=len(matched) > 0,
        matched_patterns=matched,
    )