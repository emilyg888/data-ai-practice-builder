---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-14
completeness: full
title: 14: BDA Transformation Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS IAM
  - AWS Lambda
  - Amazon Bedrock
related_controls:
  - access_control
  - pii_protection
  - private_networking
topics:
  - bda transformation patterns
  - bedrock agents
  - iam access control
  - lambda orchestration
  - bedrock
  - access control
  - pii protection
  - private networking
use_cases:
  - architecture reference
---

# 14: BDA Transformation Patterns

## Scenario

A GenAI developer is building a serverless application. The application uses AWS Lambda functions that are deployed in private subnets to process sensitive customer data. The Lambda functions need to invoke Amazon Bedrock FMs for AI-powered analytics. All API communication must remain within the AWS private network without internet exposure. The GenAI developer tests the Lambda function. The Lambda function consistently times out when attempting to call Amazon Bedrock APIs. The Lambda function has proper IAM permissions for Amazon Bedrock access. Which solution will resolve this connectivity issue?

## Common implementation patterns

- Create interface VPC endpoints for the Amazon Bedrock Runtime service in the VPC. Ensure that the endpoints are associated with the private subnets where Lambda functions are deployed. Verify that security groups allow HTTPS traffic on port 443 between Lambda and the VPC...

## Architecture guidance

- Interface VPC endpoints allow Lambda functions in private subnets to access Amazon Bedrock APIs without internet connectivity.
- The Runtime service requires the com.amazonaws.region.bedrock-runtime endpoint for model invocation operations.
- Security groups must allow outbound HTTPS traffic on port 443 from Lambda to the VPC endpoint.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: AWS documents interface VPC endpoints for private Amazon Bedrock connectivity, including private DNS and endpoint policies to control access through the endpoint.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock interface VPC endpoints / PrivateLink: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For regulated environments, combine Bedrock interface endpoints with endpoint policies, IAM conditions, and organization SCPs; validate supported endpoint names for runtime, agent runtime, and control-plane calls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
