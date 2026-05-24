---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-13
completeness: full
title: 13: RAG Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon OpenSearch Service
related_controls:
  - audit_logging
  - monitoring
  - retrieval_grounding
topics:
  - rag patterns
  - bedrock agents
  - lambda orchestration
  - bedrock
  - monitoring
  - vector search
  - audit logging
  - retrieval grounding
  - rag
use_cases:
  - architecture reference
---

# 13: RAG Patterns

## Scenario

A financial services company operates RAG for an application that answers user questions by using internal market analysis reports. The application uses Amazon Bedrock for the embedding model. The application uses an Amazon OpenSearch Service cluster as the vector store. An AWS Lambda function performs the embedding and search logic. After a recent code update to the Lambda function, the application starts returning generic responses. For example, the application returns “no relevant information found” even for questions that previously returned accurate answers. Amazon CloudWatch Logs shows no errors. AWS X-Ray confirms successful FM invocation. The OpenSearch Service cluster is healthy. Query latency remains normal. What is the cause of this issue?

## Common implementation patterns

- The updated Lambda function uses a different version of the embedding model.

## Architecture guidance

- Embedding drift occurs when query embeddings are generated with a different model than the model used to index documents.
- This issue causes a mismatch in vector space and makes retrieval ineffective.
- In this scenario, the update to the Lambda function likely introduced a new embedding model version or configuration.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
