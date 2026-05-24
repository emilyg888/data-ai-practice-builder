---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-45
completeness: full
title: 45: Knowledge Base Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Bedrock Knowledge Bases
related_controls:
  - audit_logging
  - retrieval_grounding
topics:
  - knowledge base patterns
  - bedrock knowledge bases
  - bedrock
  - knowledge bases
  - audit logging
  - retrieval grounding
use_cases:
  - document summarization
---

# 45: Knowledge Base Patterns

## Scenario

A medical diagnostics company runs a chat-based AI application to help customers find appropriate tests from a catalog of diagnostic tests. Each test contains detailed descriptions, target conditions, specimen types, and specimen collection guidelines. The application uses Amazon Bedrock Knowledge Bases supported by Amazon OpenSearch Serverless to search the catalog of available diagnostic tests. Initially, the search provides sufficient recall. However, the search is unable to prioritize the most relevant documents. As a result, the company decides to continue using hybrid search. To achieve the desired accuracy, the company increases response results to 50 to pass to the LLM for summarization. The company experiences an increase in customer use of the application. The company notices an increase in token usage. Now, the company wants to reduce token usage for each customer interaction without impacting accuracy. Which solution will meet these requirements with the LEAST effort?

## Common implementation patterns

- Configure the knowledge base to invoke a reranker model. Pass only the top five ranked documents to the LLM for summarization.

## Architecture guidance

- Knowledge bases support reranker models that can reorder retrieval results to improve precision.
- You can enable reranking and limit the retrieval set to the top five ranked documents.
- This solution maintains accuracy while reducing the tokens that pass to the LLM.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
