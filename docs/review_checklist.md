# Checkpoint 3 — Review Checklist

## 1. Repository
- Updated GitHub repository submitted

## 2. Control implementation or evaluation summary
- Each control linked to the threat it addresses: `control_list.md`
- Reasoning documented for each control selection

## 3. Defensive evidence
- Filtering logic: `injection_filter.py`
- Validation workflow: `output_validator.py`
- Access-control design: `baseline_condition.md` Section 6
- Policy enforcement mapping: `baseline_condition.md` Section 5
- Logging design: `audit_log.py`
- Secure prompt template: `secure_prompt_template.py`
- Guardrail design: `injection_filter.py`, `secure_prompt_template.py`, `output_validator.py`
- Retrieval hardening: addressed (noted N/A according to `baseline_condition.md`)
- Least-privilege matrix: `baseline_condition.md` Section 8
- Review checklist: this document

## 4. Validation evidence
- Before/after comparison: `test_pipeline.py`
- Test table: `test_pipeline.py`
- Observed reduction in unsafe behavior: injection blocked in T3, T4
- Reduced leakage: 100-character preview only in `audit_log.py`
- Improved traceability: `audit_log.py` injection_detected flag
- Improved quality of reviewed outputs: `output_validator.py`

## 5. Updated risk register
- All 7 risks present with current status: `risk_matrix.md`
- Each risk mapped to at least one control file
- Residual risk noted for R2 (phishing evasion: monitored)
- Baseline vs. current risk summary table included

## 6. Draft outline of final report
- Draft outline of final report created
