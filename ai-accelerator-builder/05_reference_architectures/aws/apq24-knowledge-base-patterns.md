---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-24
completeness: full
---

# 24: Knowledge Base Patterns

## Scenario

A legal company is developing an AI-powered contract analysis system by using Amazon Bedrock. The system must analyze legal documents to provide responses and recommendations for complex legal questions. All responses must come from an authoritative legal source. All responses must cite the authoritative legal source. The system must prevent the generation of inappropriate legal advice and filter sensitive personal information. The legal documents are stored across multiple data sources, including Amazon S3 and internal databases. A GenAI developer has already created an Amazon Bedrock knowledge base with vector embeddings from the company's legal document repositories. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Enable RAG functionality through the RetrieveAndGenerate API. Attach Amazon Bedrock Guardrails policies to the FM endpoint. Include content filters and topic restrictions in the policies.

## Common anti-patterns

- Avoid enable RAG functionality through the RetrieveAndGenerate API. Implement content filtering logic within AWS Lambda functions attached to the model endpoint. because the RetrieveAndGenerate API provides RAG functionality with integrated citation tracking. However,...
- Avoid enable document retrieval through the Retrieve API. Attach Amazon Bedrock Guardrails policies to the FM endpoint. Include content filters and topic restrictions in the policies. because guardrails provide content filtering capabilities. However, the Retrieve API returns...
- Avoid enable document retrieval through the Retrieve API. Implement content filtering logic within AWS Lambda functions attached to the model endpoint. because the Retrieve API returns only document chunks without response generation. Therefore, this solution requires additional...

## Architecture guidance

- This solution combines vector embeddings for semantic search capabilities with the RetrieveAndGenerate API.
- This solution provides document retrieval with response generation in a single call.
- Therefore, this solution automatically provides citations that are essential for legal compliance.
