# Phishender — Initial Risk Matrix

| Risk | Likelihood | Impact | Risk Level | Notes |
|------|------------|--------|------------|-------|
| Prompt injection via email body | High | High | Critical | No input sanitization in baseline. |
| Phishing evasion | High | High | Critical | LLM has no secondary verification. |
| LLM hallucination / false negative | Medium | High | High | Inherent LLM limitation. |
| Sensitive data leakage via logs | Medium | Medium | Medium | Log files contain raw email content. |
| API key exposure | Low | Medium | Medium | Key must be stored securely. |

---

## Risk Register (After Controls)

| ID | Threat | Description | Likelihood | Impact | Risk Level | Control Implemented | File | Current Status |
|----|--------|-------------|------------|--------|------------|--------------------|----- |----------------|
| R1 | Prompt Injection via Email Body | Attacker embeds instructions inside email content to manipulate Claude into returning a false verdict | High | High | Critical | Regex pattern filtering redacts injection phrases before input reaches the LLM. XML delimiter wrapping isolates user content. System prompt instructs Claude to ignore directives found inside email content. | `injection_filter.py`, `secure_prompt_template.py` | Mitigated |
| R2 | Phishing Evasion | Crafted emails to bypass LLM detection, such as encoded text, unusual formatting, or indirect language | High | High | Critical | Evaluation against labeled dataset shows 100% recall. UNCERTAIN verdict normalized to PHISHING as conservative default. | `evaluate.py`, `pipeline.py` | Monitored |
| R3 | LLM Hallucination / False Negatives | Claude returns an incorrect verdict | Medium | High | High | Output validator strictly checks verdict values, field types, confidence range, and schema before result is returned. Invalid responses are rejected entirely. | `output_validator.py` | Reduced |
| R4 | API Key Exposure | Anthropic API key is accidentally committed to the GitHub repository or exposed in code | Low | Medium | Medium | API key stored in `.env` file. `.env` excluded from version control via `.gitignore`. Key never appears in source code. Team shares key via private message only. | `.env`, `.gitignore` | Mitigated |
| R5 | Sensitive Data Leakage via Logs | Full email contents logged or exposed through API logs, violating user privacy | Medium | Medium | Medium | Audit log stores only the first 100 characters of input as a preview. Full email content is never written to disk. API calls are made server-side only, never from the browser. | `audit_log.py` | Mitigated |
| R6 | Output Manipulation | Attacker crafts email content that causes Claude to return a manipulated JSON response bypassing the schema | Low | High | High | Output validator enforces strict JSON schema validation. Any response with incorrect verdict values, wrong field types, or missing keys raises a ValidationError and is rejected. | `output_validator.py` | Mitigated |
| R7 | Denial of Service via Large Input | User submits extremely large input to overload the pipeline or exhaust API credits | Low | Medium | Medium | Input length capped at 20,000 characters. Request rejected with HTTP 400 if exceeded. | `main.py` | Mitigated |

---

## Risk Summary

| Risk Level | Baseline Count | Current Count | Change |
|------------|---------------|---------------|--------|
| Critical | 2 | 0 | -2 |
| High | 1 | 1 | 0 (Monitored) |
| Medium | 2 | 0 | -2 |
| **Total Open** | **5** | **1** | **-4** |

## After controls

| Severity | Total | Mitigated | Monitored | Open |
|----------|-------|-----------|-----------|------|
| Critical | 2 | 2 | 0 | 0 |
| High | 4 | 3 | 1 | 0 |
| Medium | 1 | 1 | 0 | 0 |
| **Total** | **7** | **6** | **1** | **0** |

---

## Residual Risk Notes

**R2 — Phishing Evasion (Monitored):**
R2 — Phishing Evasion (Monitored):
While evaluation shows 100% recall on the test dataset, the dataset used consists of short SMS messages rather than full emails. Evasion techniques specific to email formatting, HTML content, or advanced social engineering may not be fully represented. Needs test through email-specific dataset.
