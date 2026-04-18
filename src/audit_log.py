import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
LOG_FILE = "audit_log.jsonl"

#log analysis request to audit_log.json1
def log_decision(input_type: str, content: str, result: dict):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "input_type": input_type,
        "input_preview": content[:100],
        "verdict": result.get("verdict"),
        "confidence": result.get("confidence"),
        "injection_detected": result.get("injection_detected", False),
    }
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except Exception as e:
        logger.error(f"Failed to write audit log: {e}")