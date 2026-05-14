---
type: reference_note
platform: aws
status: draft
source: udemy-question-58
---

# 58: Knowledge Base And RAG Patterns

## Scenario

A healthcare provider is building an internal “policy assistant” that answers employee questions by using Amazon Bedrock Agents with an Amazon Bedrock Knowledge Base that is populated from documents in Amazon S3. The compliance team requires the application to be transparent by showing users which policy sources were used for each answer and by providing auditors with a trace of how the agent reached the response (including knowledge base retrievals and action group calls). The operations team also wants a per-response confidence signal recorded in Amazon CloudWatch so they can investigate low-confidence answers. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Enable Amazon Bedrock agent tracing for the agent and log the returned trace payloads. Configure the application to include source attribution in the response by presenting the retrieved document metadata (for example, document title and S3 URI) as evidence....

## Common anti-patterns

- Avoid store the full prompt, retrieved context chunks, and action group parameters for each request in Amazon DynamoDB. Return the stored prompt and context to end users so they can verify the model’s reasoning and use the stored context size as a confidence...

## Architecture guidance

- The lowest-overhead way to build transparency into an agent-based GenAI application is to use native agent tracing to obtain an auditable reasoning trace, while presenting evidence by surfacing the identifiers of the...
- Operational confidence should be captured as a metric in CloudWatch so it can be visualized and alarmed on; this is best done by emitting a per-request score produced during processing (for example, a...
- Alternatives that rely on audit logs, workflow histories, or returning full prompts/context either fail to provide true reasoning traces and source attribution or introduce unnecessary security and operational risk.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
