---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-73
completeness: full
title: 73: Knowledge Base Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon Kendra
  - Bedrock Knowledge Bases
related_controls:
  - access_control
topics:
  - knowledge base patterns
  - bedrock knowledge bases
  - bedrock
  - amazon kendra
  - knowledge bases
  - access control
use_cases:
  - model governance
---

# 73: Knowledge Base Patterns

## Scenario

A legal services company wants to integrate diverse document management systems with an AI solution to enhance contract generation. The company needs to connect an existing contract template repository, internal legal knowledge bases, historical case documentation, and compliance wikis. The solution must maintain consistent access patterns. The solution must provide comprehensive data integration across all sources. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Knowledge Bases to create unified access to all document sources. Configure data source connectors for the template repository and knowledge bases. Set up automated synchronization to maintain the current content.

## Architecture guidance

- Knowledge Bases provides built-in capabilities to integrate multiple document sources through standardized connectors.
- Knowledge Bases handles authentication, synchronization, and content updates automatically.
- Therefore, this solution requires the least operational overhead.

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
