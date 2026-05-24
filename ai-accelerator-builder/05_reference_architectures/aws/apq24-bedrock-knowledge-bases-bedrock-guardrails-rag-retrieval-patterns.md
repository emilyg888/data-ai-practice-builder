---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-24
completeness: full
title: 24: Knowledge Base Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon S3
  - Bedrock Guardrails
related_controls:
  - guardrails
  - pii_protection
  - retrieval_grounding
topics:
  - knowledge base patterns
  - bedrock knowledge bases
  - bedrock
  - s3 data assets
  - guardrails
  - pii protection
  - retrieval grounding
  - rag
use_cases:
  - architecture reference
---

# 24: Knowledge Base Patterns

## Scenario

A legal company is developing an AI-powered contract analysis system by using Amazon Bedrock. The system must analyze legal documents to provide responses and recommendations for complex legal questions. All responses must come from an authoritative legal source. All responses must cite the authoritative legal source. The system must prevent the generation of inappropriate legal advice and filter sensitive personal information. The legal documents are stored across multiple data sources, including Amazon S3 and internal databases. A GenAI developer has already created an Amazon Bedrock knowledge base with vector embeddings from the company's legal document repositories. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Enable RAG functionality through the RetrieveAndGenerate API. Attach Amazon Bedrock Guardrails policies to the FM endpoint. Include content filters and topic restrictions in the policies.

## Architecture guidance

- This solution combines vector embeddings for semantic search capabilities with the RetrieveAndGenerate API.
- This solution provides document retrieval with response generation in a single call.
- Therefore, this solution automatically provides citations that are essential for legal compliance.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
