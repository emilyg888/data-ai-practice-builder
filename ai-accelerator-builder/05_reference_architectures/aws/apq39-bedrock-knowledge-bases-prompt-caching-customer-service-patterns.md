---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-39
completeness: full
title: 39: Scalable Bedrock Knowledge Bases with Prompt Caching for Customer Service
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Bedrock Knowledge Bases
related_controls:
  - access_control
  - audit_logging
  - model_evaluation
  - prompt_policy
  - retrieval_grounding
topics:
  - scalable bedrock knowledge bases
  - prompt caching
  - customer service
  - bedrock knowledge bases
  - bedrock
  - knowledge bases
  - access control
  - audit logging
  - model evaluation
  - prompt policy
  - retrieval grounding
  - rag
use_cases:
  - customer-facing assistant
---

# 39: Scalable Bedrock Knowledge Bases with Prompt Caching for Customer Service

## Pattern summary

Use Bedrock Knowledge Bases with RAG over product and customer data, refresh stale data, and cache common prompts to scale customer-service responses.

## Scenario

A retail company is implementing a generative AI (GenAI) powered customer service system by using Amazon Bedrock. The system must handle product inquiries and answer various customer questions through the company's website. The system will have significant traffic load level variations throughout the year. The system must access the company's extensive product catalog and customer data. The company wants to improve performance while maintaining response quality and accuracy. Which combination of configurations will meet these requirements? (Select TWO.)

## Common implementation patterns

- Create Amazon Bedrock knowledge bases with RAG that incorporate the product catalog and customer data. Remove outdated product data regularly.
- Enable prompt caching for frequently asked questions and common inquiry patterns.

## Architecture guidance

- You can create knowledge bases with RAG so that the system can incorporate an up-to-date product catalog and customer data.
- This configuration improves response accuracy and relevance by providing context from the company's specific information.
- Regularly removing outdated product data ensures that the knowledge base remains current.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
