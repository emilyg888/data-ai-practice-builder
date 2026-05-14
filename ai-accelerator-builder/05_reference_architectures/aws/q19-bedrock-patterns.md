---
type: reference_note
platform: aws
status: draft
source: udemy-question-19
---

# 19: Implementation Patterns

## Scenario

A healthcare analytics team is building an internal chat application that uses Amazon Bedrock to answer questions by querying a reporting dataset in Amazon Athena. The team is concerned that the FM could occasionally generate inappropriate language in its answers or accidentally include sensitive information from retrieved context. The team also must ensure the application generates only read-only, deterministic SQL queries (SELECT statements) and never produces free-form SQL that could be unsafe. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure Amazon Bedrock Guardrails to filter and mask unsafe content in model responses. Use an AWS Lambda function to perform a text-to-SQL transformation by mapping user intent to a predefined set of parameterized SELECT-only query templates that are...

## Common anti-patterns

- Avoid place Amazon API Gateway in front of the application and enable AWS WAF managed rules to block profanity and SQL injection strings in incoming requests. Allow the FM to generate SQL and final answers without additional controls. because wAF can help...

## Architecture guidance

- The safest low-operations approach combines managed output controls with deterministic query generation.
- Amazon Bedrock Guardrails help prevent harmful responses by filtering or masking unsafe content in the model’s output.
- Separately, generating SQL through a controlled text-to-SQL transformation that maps user intent to allowlisted, parameterized SELECT templates prevents the FM from emitting arbitrary SQL and ensures the database...

## Domain

- Content Domain 3: AI Safety, Security, and Governance
