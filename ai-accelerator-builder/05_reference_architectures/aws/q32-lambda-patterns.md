---
type: reference_note
platform: aws
status: draft
source: udemy-question-32
---

# 32: Serverless Integration Patterns

## Scenario

A fintech company is building a customer self-service chatbot that runs behind Amazon API Gateway and AWS Lambda. The chatbot uses Amazon Bedrock to answer questions such as “What were my last 5 card transactions?” by querying an Amazon Aurora PostgreSQL database. The company is concerned that abusive user messages could cause the chatbot to respond with profane or otherwise harmful language. The company also wants to avoid any fabricated transaction amounts and ensure that data-backed answers are deterministic and auditable. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure Amazon Bedrock Guardrails to filter model responses (for example, profanity and topic filters) and return a blocked message when content violates policy. For transaction questions, implement a text-to-SQL flow where the model produces a SQL query...

## Common anti-patterns

- Avoid deploy a custom toxicity classification model in Amazon SageMaker AI and use SageMaker Model Monitor and SageMaker Clarify to detect unsafe outputs and block responses when toxicity or bias metrics exceed a threshold. because this introduces significant...

## Architecture guidance

- A robust content safety framework for a customer-facing chatbot should combine managed output controls with deterministic data access patterns.
- Guardrails help enforce policy on the model’s generated responses by filtering profanities and disallowed topics and by returning a consistent blocked message when violations occur.
- For questions that require exact values (such as financial transactions), a text-to-SQL approach reduces the risk of hallucinated numbers by forcing the system to retrieve the answer from the database and to generate...

## Domain

- Content Domain 3: AI Safety, Security, and Governance
