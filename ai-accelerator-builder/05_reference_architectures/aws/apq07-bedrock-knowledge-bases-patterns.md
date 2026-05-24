---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-7
completeness: full
title: 7: Knowledge Base Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Bedrock Knowledge Bases
related_controls:
  - audit_logging
  - prompt_policy
topics:
  - knowledge base patterns
  - bedrock knowledge bases
  - bedrock
  - knowledge bases
  - audit logging
  - prompt policy
use_cases:
  - document summarization
---

# 7: Knowledge Base Patterns

## Scenario

A GenAI developer is developing a document summarization system by using Amazon Bedrock Knowledge Bases. Users upload large technical research papers that the system must summarize accurately. The GenAI developer receives reports that generated summaries frequently omit critical sections from longer documents, even when the full source text was successfully uploaded and tokenized. Logs show no API errors or truncation messages. However, summaries frequently miss information near the middle or end of documents. Which solution will resolve this issue?

## Common implementation patterns

- Configure semantic chunking in Amazon Bedrock. Submit each segment to Amazon Bedrock for summarization. Use prompt chaining to combine the partial summaries into a final consolidated summary.

## Architecture guidance

- Amazon Bedrock supports semantic chunking.
- Semantic chunking resolves the issue of missing information from longer documents by intelligently segmenting the text into coherent parts.
- Then, the model can summarize the segments individually.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
