---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-5
completeness: full
title: 5: Search And Retrieval Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon S3
related_controls:
  - retrieval_grounding
topics:
  - search retrieval patterns
  - bedrock agents
  - lambda orchestration
  - s3 data assets
  - retrieval grounding
use_cases:
  - search and retrieval
  - cost optimization
  - multimodal extraction
---

# 5: Search And Retrieval Patterns

## Scenario

A company is building a diagnostic imaging application. The application needs to perform similarity searches across 50 million images to assist with diagnosing and treating patients. The application must process new images daily. The application will perform similarity searches infrequently when users need to find similar cases for reference. The company wants a cost-effective solution that provides responsive search performance without requiring infrastructure management. Which solution will meet these requirements MOST cost-effectively?

## Common implementation patterns

- Create an Amazon S3 vector bucket with vector indexes to store image embeddings and perform similarity searches.

## Architecture guidance

- S3 Vectors is a fully managed, serverless feature of Amazon S3 that provides scalable vector search capabilities.
- S3 Vectors can store and search vector data.
- S3 Vectors can support up to billions of vectors.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock Data Automation supports asynchronous processing through projects and blueprints, with output written to S3 and status retrieved through the data automation runtime APIs.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock Data Automation async invocation: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_data-automation-runtime_InvokeDataAutomationAsync.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For multimodal or document-heavy RAG, use Bedrock Data Automation to normalize PDFs, images, or audio into structured outputs before indexing or prompt assembly.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
