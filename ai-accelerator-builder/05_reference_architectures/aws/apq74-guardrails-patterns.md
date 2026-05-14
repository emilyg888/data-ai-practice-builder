---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-74
completeness: full
---

# 74: Guardrails Patterns

## Scenario

A software company is launching an AI assistant by using Amazon Bedrock. The AI assistant will help users troubleshoot issues by quickly exploring logs and documentation, and then recommending actions for remediation. A GenAI developer wants to set up Amazon Bedrock Guardrails. The GenAI developer wants to add protection against SQL injection. The GenAI developer wants to add a post-generation factuality check to prevent recommendations based on inaccurate information. Which combination of actions will meet these requirements? (Select TWO.)

## Common implementation patterns

- Add a prompt attack filter.
- Add a contextual grounding check.

## Common anti-patterns

- Avoid add a misconduct content filter. because guardrails provide safeguards for GenAI applications. Misconduct content filters in guardrails prevent the GenAI application from engaging in criminal activity or providing information that could be potentially harmful. This filter...
- Avoid use an LLM-as-a-judge job to check for factuality. because amazon Bedrock evaluations support LLM-as-a-judge jobs. These jobs use an LLM to score the responses from another model. You can use LLM-as-a-judge jobs to check for factuality. However, LLM-as-a-judge jobs run as...
- Avoid add a denied topic to prevent the chatbot from discussing SQL queries. because guardrails provide safeguards for GenAI applications. Guardrails support denied topics. Denied topics check that the prompt and completion do not engage in a particular topic. For SQL queries,...

## Architecture guidance

- Guardrails provide safeguards for GenAI applications.
- You can configure guardrails to protect against prompt attacks, including jailbreaks and prompt injection.
- Guardrails support contextual grounding checks to detect and filter hallucinations in model responses.
