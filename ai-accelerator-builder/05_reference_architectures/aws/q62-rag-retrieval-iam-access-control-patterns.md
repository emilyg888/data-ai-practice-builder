---
type: reference_note
platform: aws
status: draft
source: udemy-question-62
title: 62: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS IAM
  - Amazon Bedrock
related_controls:
  - access_control
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - iam access control
  - bedrock
  - access control
  - retrieval grounding
use_cases:
  - architecture reference
---

# 62: Knowledge Base And RAG Patterns

## Scenario

A financial services firm wants to allow its internal developers to build proof-of-concept applications that call Amazon Bedrock directly from local Python scripts. The firm uses Okta for workforce identity and requires single sign-on with short-lived credentials (no long-term access keys). Security requirements state that developers must be able to perform inference against approved FMs but must not be able to manage models, agents, or knowledge bases. Which solution meets these requirements with the MOST secure, least-privilege access model?

## Common implementation patterns

- Configure IAM Identity Center with Okta as the identity provider. Create a permission set for the developer group with a custom IAM policy that allows only Amazon Bedrock Runtime actions (for example, InvokeModel and Converse) for approved models. Have...

## Architecture guidance

- The most secure approach is to federate workforce identities from the enterprise identity provider into AWS and issue temporary credentials, then apply role-based access control with least-privilege IAM policies.
- Using IAM Identity Center with Okta satisfies the federation and short-lived credential requirements, while a custom permission set policy can restrict access to only Bedrock Runtime inference operations (such as...
- Approaches that rely on long-term access keys, shared credentials, or unsupported token types either violate the security requirements or cannot authorize requests to Amazon Bedrock.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
