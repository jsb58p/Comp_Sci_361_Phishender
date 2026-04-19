# Phishender

**Domain:** AI for Cyber Defense  
**Term:** Spring 2026

## Overview

Phishender is an LLM-powered phishing detection and explanation tool targeting end users and organizations that need a fast way to evaluate suspicious emails and URLs. Unlike traditional spam filters that block threats silently, Phishender returns a structured verdict alongside a plain-language explanation of detected phishing indicators — improving both detection and security literacy simultaneously.

## Architecture

![Architecture Diagram](https://github.com/jsb58p/Comp_Sci_361_Phishender/blob/main/docs/architecture.png)

## Features

- Accept raw email text or URL as input via web interface
- Analyze input through an LLM pipeline with a structured prompt
- Return a verdict with confidence rationale
- Generate a plain-language explanation of detected phishing indicators
- Provide security tips to users for future attacks
- Evaluate detection accuracy using a labeled phishing dataset
- Document techniques defending against prompt injection via email content

## Project Objective

Build and evaluate a working LLM-powered phishing detection tool that achieves confident classification accuracy on a labeled test set while producing clear, easy-to-understand explanations.

## Team

| Name | Role |
|------|------|
| Kevin Zhang | Project Lead |
| Jayanth Kumar Mallireddy | Risk/Threat Analyst | 
| Jacob Biddinger | Technical Implementation Lead |
| Antionio Lacio | Documentation/Presentation Lead |

## Assets

| Asset | Description | Priority |
|-------|-------------|----------|
| Email Submission Input | Raw email text and headers for analysis | Critical |
| LLM Analysis Engine | Claude/GPT API pipeline performing phishing classification | Critical |
| API Credentials | Anthropic/OpenAI keys and app authentication tokens | Critical |
| Explanation Output | Plain-language reasoning returned to the user | High |
| Phishing Dataset | Labeled for testing and evaluation | High |
| Audit / Decision Logs | Record of inputs, verdicts, and explanations | Medium |

## Threat Assumptions

| Threat Category | Type | Potential Impact |
|----------------|------|-----------------|
| Prompt Injection via Email Body | AI Integrity | LLM manipulated into approving phishing |
| Phishing Evasion | Evasion | Crafted emails bypass LLM detection |
| LLM Hallucination / False Negatives | AI Reliability | Phishing emails classified as legitimate |
| API Key Exposure | Access Control | Unauthorized use of LLM pipeline |
| Sensitive Data Leakage via Prompt | Privacy | Email contents exposed through API logs |

## Repository Structure

```
Phishender/
├── data/
│   └── log_samples.md
├── docs/
│   ├── architecture.png
│   ├── asset_inventory.md
│   ├── baseline_condition.md
│   ├── control_list.md
│   ├── risk_matrix.md
│   ├── risk_register.md
│   ├── threat_model.md
│   └── prompt_injection_defense.md
└── src/                  
    ├── main.py
    ├── index.html
    ├── pipeline.py
    ├── api_client.py
    ├── injection_filter.py
    ├── output_validator.py
    ├── secure_prompt_template.py
    ├── audit_log.py     
    ├── requirements.txt
    ├── test_pipeline.py
    └── evaluation/
        ├── evaluate.py
        ├── email.csv
        └── evaluation_results.jsonl
```
