---
type: reference_note
platform: aws
status: draft
source: udemy-question-33
---

# 33: Throughput Patterns

## Scenario

A financial services innovation team wants to pilot an internal “AI search” assistant that answers questions about employee policy PDFs stored in Amazon S3. The team needs a technical proof of concept within 2 weeks, wants to avoid managing servers, and must produce initial measurements of per-question latency and token-related cost before committing to a production rollout. Which combination of actions will meet these requirements with the LEAST operational overhead? (Select TWO.)

## Common implementation patterns

- Create an Amazon Bedrock Knowledge Base that ingests the policy PDFs from Amazon S3 with managed chunking and an embedding model. Implement a simple API backed by AWS Lambda that calls RetrieveAndGenerate to answer pilot user questions. This is the managed or...
- Instrument the proof of concept to estimate and track token usage and latency by using the Amazon Bedrock CountTokens API and Amazon CloudWatch metrics (such as input and output token counts, invocation count, and model latency). This is the managed or...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A low-overhead proof of concept should rely on managed GenAI building blocks and lightweight measurement.
- Using a Bedrock Knowledge Base with documents in S3 provides a fast “chat with your documents” style RAG implementation without building and operating a custom retrieval pipeline.
- Pairing the pilot with token and latency measurement through CountTokens and CloudWatch produces the core feasibility signals (cost per request and responsiveness) needed to decide whether to proceed to a full...

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
