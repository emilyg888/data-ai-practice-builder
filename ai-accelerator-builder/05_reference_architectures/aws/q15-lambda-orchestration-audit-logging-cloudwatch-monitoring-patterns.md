---
type: reference_note
platform: aws
status: draft
source: udemy-question-15
title: 15: Throughput Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon API Gateway
  - Amazon Bedrock
  - Amazon CloudWatch
related_controls:
  - access_control
  - audit_logging
  - monitoring
  - prompt_policy
topics:
  - throughput patterns
  - bedrock agents
  - lambda orchestration
  - api gateway
  - bedrock
  - monitoring
  - access control
  - audit logging
  - prompt policy
  - data quality
use_cases:
  - model governance
---

# 15: Throughput Patterns

## Scenario

An enterprise platform team at a financial institution is building a centralized “GenAI gateway” that internal applications must use to access Amazon Bedrock models. The gateway must enforce consistent request validation and throttling, record an audit trail of model access, and be deployed through an automated CI/CD pipeline that includes security checks. If a new release causes increased errors or latency, the deployment must automatically roll back. Which solution meets these requirements with the LEAST operational overhead?

## Common implementation patterns

- Deploy the gateway as Amazon API Gateway integrated with AWS Lambda that invokes Amazon Bedrock. Use AWS CodePipeline to orchestrate deployments from source control. Run automated tests and security scans in AWS CodeBuild, deploy with AWS CodeDeploy using...

## Architecture guidance

- A centralized GenAI gateway is best implemented with API Gateway in front of a Lambda layer that invokes Bedrock so the organization can standardize request validation, throttling, and access patterns.
- A managed CI/CD pipeline uses CodePipeline for orchestration and CodeBuild to run automated tests (for example, contract tests for request/response formats and prompt regression tests) and security scans before...
- For safe releases, CodeDeploy can perform canary traffic shifting for a Lambda alias and automatically roll back when CloudWatch alarms detect increased error rates or latency.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
