---
type: reference_note
platform: aws
status: draft
source: udemy-question-57
---

# 57: Implementation Patterns

## Scenario

A financial services firm is building an internal policy assistant that answers employee questions by using an Amazon Bedrock text model. The source policy documents are stored in Amazon S3. During testing, users report that the assistant sometimes invents policy details that are not present in the source documents. The firm needs a solution that grounds responses in the policy corpus, produces a machine-readable confidence signal that the application can use to return “insufficient evidence” when answers are not supported, and returns results in a consistent JSON structure for downstream processing. The firm wants the solution with the LEAST operational overhead. Which approach meets these requirements?

## Common implementation patterns

- Create an Amazon Bedrock Knowledge Base over the policy documents in Amazon S3. Use a retrieve-and-generate pattern so the FM answers only with retrieved context. Enable Amazon Bedrock Guardrails contextual grounding checks to score grounding and relevance,...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- To reduce hallucinations, the most reliable pattern is to ground the FM on authoritative content at inference time and to verify that the response aligns with that content.
- Using an Amazon Bedrock Knowledge Base implements managed retrieval over the policy corpus so the model can answer using retrieved context instead of guessing.
- Adding Amazon Bedrock Guardrails contextual grounding checks provides an automated grounding/relevance signal that the application can interpret as a confidence indicator and use to return an “insufficient evidence”...

## Domain

- Content Domain 3: AI Safety, Security, and Governance
