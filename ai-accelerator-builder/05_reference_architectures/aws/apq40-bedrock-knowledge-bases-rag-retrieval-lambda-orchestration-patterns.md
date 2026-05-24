---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-40
completeness: full
title: 40: RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Bedrock Knowledge Bases
related_controls:
  - retrieval_grounding
topics:
  - rag patterns
  - bedrock knowledge bases
  - lambda orchestration
  - bedrock
  - knowledge bases
  - retrieval grounding
  - rag
use_cases:
  - search and retrieval
---

# 40: RAG Patterns

## Scenario

A company has a large collection of HTML documents. The documents contain articles with varying lengths and complex hierarchical structures. Headers identify each article. Each article contains multiple paragraphs that can range from a few sentences to several pages in length. A GenAI developer must build a RAG solution that preserves the relationships between articles and the articles' contained paragraphs. The solution must retrieve relevant content for user inquiries. The solution must minimize irrelevant or inaccurate responses. Which solution will meet these requirements?

## Common implementation patterns

- Create an AWS Lambda function that implements a custom hierarchical chunking strategy. Use the LangChain framework for the HTML documents. Deploy LangChain through a Lambda function layer. Create an Amazon Bedrock knowledge base with the documents. Use the Lambda function as the...

## Architecture guidance

- Amazon Bedrock Knowledge Bases supports custom chunking through Lambda functions.
- This solution can process documents with highly variable lengths.
- A custom Lambda function with LangChain provides a specialized chunking strategy.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
