# Phishender — Control List 1.0

| Control | Threat Addressed | Type | File | Status |
|---------|-----------------|------|------|--------|
| Regex prompt injection filtering | Prompt injection via email body | Preventive | `injection_filter.py` | Implemented |
| XML delimiter wrapping of user input | Prompt injection via email body | Preventive | `secure_prompt_template.py` | Implemented |
| Hardened system prompt | Prompt injection via email body | Preventive | `secure_prompt_template.py` | Implemented |
| Structured output schema validation | LLM hallucination / false negatives | Detective | `output_validator.py` | Implemented |
| API key environment variable storage | API key exposure | Preventive | `.env`, `api_client.py` | Implemented |
| .env excluded from version control | API key exposure | Preventive | `.gitignore` | Implemented |
| Audit log redaction — 100 char preview only | Sensitive data leakage via logs | Preventive | `audit_log.py` | Implemented |
| Input length limit — 20,000 characters | Denial of service via large input | Preventive | `main.py` | Implemented |
| UNCERTAIN verdict normalized to PHISHING | Phishing evasion / false negatives | Preventive | `pipeline.py` | Implemented |
| Labeled dataset evaluation | Phishing evasion / false negatives | Detective | `evaluate.py` | Implemented |
| Before/after injection test suite | Prompt injection via email body | Detective | `test_pipeline.py` | Implemented |
| Server-side only API calls | Sensitive data leakage | Preventive | `api_client.py` | Implemented |
