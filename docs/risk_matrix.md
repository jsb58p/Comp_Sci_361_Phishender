# Phishender — Initial Risk Matrix

| Risk | Likelihood | Impact | Risk Level | Notes |
|------|------------|--------|------------|-------|
| Prompt injection via email body | High | High | Critical | No input sanitization in baseline. |
| Phishing evasion | High | High | Critical | LLM has no secondary verification. |
| LLM hallucination / false negative | Medium | High | High | Inherent LLM limitation. |
| Sensitive data leakage via logs | Medium | Medium | Medium | Log files contain raw email content. |
| API key exposure | Low | Medium | Medium | Key must be stored securely. |
