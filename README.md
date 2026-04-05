# Phishender

**Domain:** AI for Cyber Defense  
**Term:** Spring 2026

## Overview

Phishender is an LLM-powered phishing detection and explanation tool targeting end users and organizations that need a fast way to evaluate suspicious emails and URLs. Unlike traditional spam filters that block threats silently, Phishender returns a structured verdict alongside a plain-language explanation of detected phishing indicators — improving both detection and security literacy simultaneously.

## Features

- Accept raw email text or URL as input via web interface
- Analyze input through an LLM pipeline with a structured prompt
- Return a verdict with confidence rationale
- Generate a plain-language explanation of detected phishing indicators
- Evaluate detection accuracy using a labeled phishing dataset
- Document techniques defending against prompt injection via email content

## Project Objective

Build and evaluate a working LLM-powered phishing detection tool that achieves confident classification accuracy on a labeled test set while producing clear, easy-to-understand explanations.

## Team

| Name | Role |
|------|------|
| Kevin Zhang | Project Lead |
| Risk/Threat Analyst | 
| Technical Implementation Lead |
| Documentation/Presentation Lead |

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
phishender/
├── README.md
├── src/
├── data/
└── docs/
```
