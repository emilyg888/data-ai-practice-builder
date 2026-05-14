---
type: reference_note
platform: aws
status: draft
source: udemy-question-47
---

# 47: Knowledge Base And RAG Patterns

## Scenario

A SaaS provider runs an interactive RAG assistant for internal help desk agents. The request path is Amazon API Gateway to AWS Lambda, where the function performs a vector similarity search in Amazon OpenSearch Service and then calls an Amazon Bedrock FM by using the Converse API. Users report that responses feel slow, and profiling shows frequent connection setup overhead between Lambda and downstream services and high query fan-out across many OpenSearch shards during vector searches. The provider wants to reduce p95 end-to-end latency for the chat experience without changing the FM or the underlying document corpus and with the LEAST operational overhead. Which combination of actions should the provider take? (Select TWO.)

## Common implementation patterns

- Reindex the OpenSearch vector index with fewer, larger shards sized for semantic search workloads to reduce cross-shard coordination during k-NN queries. This is the managed or lower-overhead approach called out as correct in the exam explanation.
- Refactor the Lambda function to reuse HTTP/AWS SDK clients across invocations (for example, initialize clients outside the handler) and configure connection pooling/keep-alive for calls to OpenSearch and Amazon Bedrock. This is the managed or lower-overhead...
- Enable Amazon Bedrock global cross-Region inference to route all model invocations to the least busy Region for faster responses. This is the managed or lower-overhead approach called out as correct in the exam explanation.
- Turn on Amazon Bedrock prompt caching by placing the retrieved OpenSearch context into the cached prompt prefix so future queries can reuse it. This is the managed or lower-overhead approach called out as correct in the exam explanation.

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- The largest latency gains come from optimizing the two proven bottlenecks in the workflow: service-to-service communication and vector retrieval execution.
- Reusing clients with connection pooling reduces repeated connection establishment overhead between Lambda and downstream services, lowering end-to-end latency without changing the FM or architecture.
- Separately, tuning OpenSearch for vector search by reducing shard fan-out (fewer, larger shards sized appropriately for semantic search) reduces coordination overhead and speeds retrieval, which is a major contributor...

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
