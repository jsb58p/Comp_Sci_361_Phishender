# Phishender — Expanded Asset Inventory

| Asset | Description | Priority | Risk if Compromised |
|-------|-------------|----------|---------------------|
| Email submission input | Raw email text and headers submitted by the user. | Critical | Malicious input could manipulate LLM output. |
| LLM analysis engine | Claude/GPT API pipeline performing phishing classification. | Critical | Compromise results in incorrect verdicts. |
| API credentials | Anthropic/OpenAI API keys and authentication tokens. | Critical | Unauthorized API usage and financial exposure. |
| Structured prompt | The prompt template used to instruct the LLM. | High | Prompt manipulation leads to incorrect classification. |
| Explanation output | Plain-language reasoning returned to the user. | High | Incorrect explanation misleads user security decisions. |
| Phishing dataset | Labeled dataset used for testing and evaluation. | High | Corrupted dataset produces unreliable evaluation results. |
| Audit / decision logs | Record of inputs, verdicts, and explanations. | Medium | Log exposure reveals sensitive user-submitted email content. |
| Web interface | Front-end through which users submit input. | Medium | Compromise allows injection of malicious input. |
| Source code / repository | GitHub repository containing all project code and documentation. | Medium | Exposed credentials or logic vulnerabilities if repository is public. |
