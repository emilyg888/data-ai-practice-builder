---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-43
completeness: full
title: 43: Streaming Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
  - Amazon Bedrock Data Automation
related_controls:
topics:
  - streaming patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - bedrock
  - bedrock data automation
use_cases:
  - real-time streaming
  - multimodal extraction
  - routing and orchestration
---

# 43: Streaming Patterns

## Scenario

A company receives large merged PDF files from employees. Each PDF file includes multiple pages with distinct content types, including images and text. The images and text can be categorized into a predefined list. A GenAI developer creates an Amazon Bedrock Data Automation (BDA) project. The GenAI developer uses the BDA project in an AWS Step Functions workflow. The GenAI developer defines custom outputs and provides relevant blueprints as expected. However, the extraction results are inconsistent. The first two pages are correct. However, most of the other pages are missed entirely. Downstream systems receive incomplete metadata. Which combination of steps will resolve this issue with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Enable PDF page splitting in the BDA project.
- Refine the blueprint names and definitions. Include only one blueprint for each content type.

## Architecture guidance

- Enabling PDF page splitting in the BDA project provides proper processing for multipage PDF files.
- This built-in feature automatically handles page segmentation.
- Therefore, all pages are processed correctly, without requiring additional custom code or services.

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
