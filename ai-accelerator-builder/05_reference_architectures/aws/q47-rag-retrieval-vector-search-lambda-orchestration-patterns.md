---
type: reference_note
platform: aws
status: draft
source: udemy-question-47
title: 47: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon OpenSearch Service
related_controls:
  - prompt_policy
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - lambda orchestration
  - api gateway
  - bedrock
  - vector search
  - prompt policy
  - retrieval grounding
  - rag
  - cross-region inference
use_cases:
  - real-time streaming
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

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock inference profiles support cross-Region inference for higher throughput and resilience; geographic profiles are the documented option when data residency boundaries matter.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Cross-Region inference: https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html
- Documentation source: Inference profiles: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html
- Documentation source: Global cross-Region inference: https://docs.aws.amazon.com/bedrock/latest/userguide/global-cross-region-inference.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For maximum throughput and eligible models, evaluate Global cross-Region inference; for compliance-constrained workloads, prefer geographic inference profiles and update SCP/IAM policies for all destination Regions.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 4: Operational Efficiency and Optimization fo
