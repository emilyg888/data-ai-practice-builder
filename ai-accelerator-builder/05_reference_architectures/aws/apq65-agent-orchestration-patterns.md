---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-65
completeness: full
---

# 65: Agent Orchestration Patterns

## Scenario

A travel company is developing a new AI-powered travel recommendation application by using Amazon Bedrock Agents. Customers can use the application to input travel preferences and receive personalized itinerary suggestions. The company wants to avoid prompt injection attacks that could manipulate the FM to provide unauthorized access or bypass content filters. A GenAI developer must implement security measures to protect against prompt injection attacks. Which combination of actions will meet these requirements? (Select THREE.)

## Common implementation patterns

- Associate an Amazon Bedrock guardrail with the agent to implement content filtering and topic boundaries.
- Enable the default pre-processing prompt for the Amazon Bedrock agent to evaluate if user input is safe to process.

## Common anti-patterns

- Avoid deploy AWS WAF in front of the application to block malicious requests before the requests reach Amazon Bedrock. because aWS WAF can mitigate web application vulnerabilities. However, AWS WAF is not designed to detect or prevent prompt injection attacks. AWS WAF operates...
- Avoid create an Amazon CloudWatch anomaly detection alarm to identify unusual prompt traffic patterns. because cloudWatch anomaly detection provides historical metrics to flag unusual spikes or drops and can notify you about anomalies. This action is a reactive monitoring...
- Avoid create AWS Config custom rules to audit agent configuration settings and ensure that all deployed agents have an associated guardrail policy. because aWS Config can evaluate resource configurations against rules to detect drift or noncompliance. You can use AWS Config...

## Architecture guidance

- Guardrails provide built-in protection against prompt injection.
- Guardrails provide content filtering and enforce topic boundaries.
- This action validates and filters inputs before the inputs reach the FM.
