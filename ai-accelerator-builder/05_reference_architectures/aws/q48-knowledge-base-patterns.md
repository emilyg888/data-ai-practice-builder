---
type: reference_note
platform: aws
status: draft
source: udemy-question-48
---

# 48: Knowledge Base And RAG Patterns

## Scenario

A SaaS provider is building a customer-support chat application that uses the Amazon Bedrock Converse API with a single FM. The application stores full conversation history in Amazon DynamoDB and uses an Amazon Bedrock Knowledge Base for RAG. As usage grows, the company’s Bedrock spend increases sharply, and some requests fail when the prompt exceeds the model’s context window. The company wants to reduce token-related costs while preserving answer quality. Which combination of actions will meet these requirements? (Select TWO.)

## Common implementation patterns

- Before each model invocation, call the Amazon Bedrock CountTokens API to estimate total input size. If the request exceeds a token budget, prune older conversation turns and reduce the number of retrieved chunks from the knowledge base. Publish input and...
- Implement prompt compression by using a smaller FM to summarize older conversation history into a short running summary that is stored in DynamoDB. Include only the summary plus the most recent turns in each request and set maxTokens to limit response size....

## Common anti-patterns

- Avoid increase the knowledge base chunk size so that fewer chunks are retrieved, and disable metadata-based filtering to avoid excluding potentially relevant content. Send the larger chunks to the FM to preserve answer quality. because increasing chunk size...

## Architecture guidance

- The most effective token-efficiency approaches reduce how many tokens are included in each request while preserving the information needed for accurate answers.
- Estimating tokens before invocation enables enforcing a token budget and applying deterministic reductions such as pruning conversation history and limiting retrieved RAG context.
- Prompt compression through summarization is another high-impact technique: it replaces long histories with a compact summary plus recent turns, and response limiting prevents large completions from driving up cost.

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
