---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-46
completeness: full
title: 46: Streaming Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS IAM
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon DynamoDB
related_controls:
  - access_control
topics:
  - streaming patterns
  - bedrock agents
  - iam access control
  - lambda orchestration
  - api gateway
  - bedrock
  - state store
  - access control
use_cases:
  - real-time streaming
---

# 46: Streaming Patterns

## Scenario

A GenAI developer is implementing a real-time AI assistant application. The application uses Amazon API Gateway WebSocket APIs to stream responses from an AWS Lambda function that calls an Amazon Bedrock FM with response streaming. The application must support connection management, including session state across multi-step interactions, retries, and disconnect cleanup. Which combination of steps will provide this functionality with MINIMAL operational overhead? (Select THREE.)

## Common implementation patterns

- Configure an IAM role for the Lambda function with permissions that include bedrock:InvokeModelWithResponseStream and execute-api:ManageConnections. Add resource ARNs that include the API Gateway WebSocket API ID.
- Set up a WebSocket API in API Gateway with route selection expressions. Integrate the API with a Lambda function that handles connection management and streams responses back to clients using the API Gateway Management API.
- Set up an Amazon DynamoDB table to persist active WebSocket connection IDs and session metadata. Update the table on $connect and $disconnect and use TTL.

## Architecture guidance

- The Lambda function requires specific IAM permissions to both invoke Amazon Bedrock models with streaming and to manage WebSocket connections.
- The resource ARNs must include the specific API Gateway WebSocket API ID to properly scope the permissions.
- You need a WebSocket API in API Gateway to maintain persistent client connections.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
