---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-13
completeness: full
title: 13: Identity Federation Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS IAM
  - AWS Lambda
  - Amazon Bedrock
related_controls:
  - access_control
topics:
  - identity federation patterns
  - bedrock agents
  - iam access control
  - lambda orchestration
  - bedrock
  - access control
use_cases:
  - architecture reference
---

# 13: Identity Federation Patterns

## Scenario

An airline company uses AWS Organizations to manage multiple AWS accounts. The company wants to use generative AI (GenAI) and Amazon Bedrock to enhance a computerized maintenance management system (CMMS). The company has an existing identity provider (IdP) based on Microsoft Entra ID. The company needs to ensure that only authorized employees can access Amazon Bedrock based on their job roles. The solution must provide centralized access control and integration with the existing IdP. Which combination of steps will meet these requirements? (Select TWO.)

## Common implementation patterns

- Configure AWS IAM Identity Center with Microsoft Entra ID as an external IdP. Use custom permission sets to control access to Amazon Bedrock.
- Set up SAML-based federation between Entra ID and IAM. Create IAM roles mapped to Entra ID groups with appropriate permissions to access Amazon Bedrock.

## Architecture guidance

- You can use IAM Identity Center as a centralized way to manage access to multiple AWS accounts and applications.
- IAM Identity Center supports federation with external IdPs, including SCIM or Entra ID through SAML.
- This step provides centralized access control.

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
