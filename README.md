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

# Phishender — Setup & Running Guide

## Prerequisites

- Python 3.11+
- An Anthropic API key from [console.anthropic.com](https://console.anthropic.com)
- A web browser (Firefox or Chrome)

---

## 1. Clone the Repository

```bash
git clone https://github.com/jsb58p/Comp_Sci_361_Phishender.git
cd Comp_Sci_361_Phishender
```

---

## 2. Install Dependencies

Navigate into the `src/` folder and install requirements:

```bash
cd src
pip install -r requirements.txt
```

---

## 3. Set Up Your API Key

Edit `.env` file inside the `src/` folder:

```bash
ANTHROPIC_API_KEY=?
```

Replace ? with your actual key from **console.anthropic.com → API Keys**.

Important:
- No spaces around the `=` sign
- Never commit this file to GitHub — it is already excluded via `.gitignore`

---

## 4. Start the Backend

Make sure you are inside the `src/` folder, then run:

```bash
uvicorn main:app --reload
```

You should see:

```
INFO: Uvicorn running on http://127.0.0.1:8000
```

Leave this terminal open while using the app.

---

## 5. Open the Frontend

Open your browser and go to:

```
http://localhost:8000
```

The frontend loads automatically, do not open `index.html` directly as a file

---

## 6. Using the App

- Click **Email** tab and paste a full email, or click **URL** tab and paste a suspicious link
- Click **Analyze** to run the analysis
- Click **Load Example** to pre-fill a sample phishing email for demo purposes
- Click **Copy Results** to copy the full analysis to clipboard

---

## 7. Run the Injection Defense Test (Optional)

To verify the prompt injection defenses work, run from inside `src/`:

```bash
python test_pipeline.py
```

This runs 4 test cases through both the unprotected and protected pipeline and prints a before/after comparison table showing the defenses in action.

---

## 8. Run the Evaluation (Optional)

To evaluate classification accuracy against the labeled dataset:

Navigate into the evaluation folder:
```bash
cd src/evaluation
python evaluate.py
```

Results print to the terminal and are saved to `evaluation_results.jsonl`.

---

## Stopping the Server

Go back to the terminal running uvicorn and press **Ctrl+C**.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Backend won't start | Make sure you are running uvicorn from inside `src/`, not the project root |
| API key error | Check `.env` is inside `src/` and has no spaces around the `=` sign |
| Frontend shows network error | Make sure backend is running first, then go to `http://localhost:8000` |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` from inside `src/` |
| `evaluate.py` crashes on import | Python 3.14 has library compatibility issues — the main app still works fine |
| Port 8000 already in use | Another process is using the port — restart your terminal and try again |

---

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
