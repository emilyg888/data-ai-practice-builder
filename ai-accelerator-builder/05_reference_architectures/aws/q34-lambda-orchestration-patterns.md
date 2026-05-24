---
type: reference_note
platform: aws
status: draft
source: udemy-question-34
title: 34: Prompt Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon Comprehend
related_controls:
  - pii_protection
  - prompt_policy
topics:
  - prompt patterns
  - bedrock agents
  - lambda orchestration
  - bedrock
  - pii protection
  - prompt policy
use_cases:
  - customer-facing assistant
  - internal assistant
  - claims processing
---

# 34: Prompt Patterns

## Scenario

A customer support SaaS provider is building an internal assistant that uses Amazon Bedrock to draft replies to incoming support tickets. Tickets are ingested from email and chat and often include noisy text such as email signatures, legal disclaimers, and inconsistent formatting. The assistant’s outputs are inconsistent because key details such as product names and case identifiers are not always clearly presented in the prompt. The team wants to improve response quality and consistency by enhancing the input text before invoking the FM, without building a custom model. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Add an AWS Lambda preprocessing step that calls Amazon Comprehend to extract key entities (such as product names and case identifiers) and normalize or redact noisy/sensitive content. Then use an Amazon Bedrock text model to reformat the cleaned ticket into a...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- When an FM receives inconsistent, noisy prompts, output quality and consistency often degrade because important details are buried in irrelevant text.
- A low-overhead way to address this is to add a preprocessing layer: use AWS Lambda to orchestrate input cleaning, use Amazon Comprehend to extract key entities and help normalize/redact problematic content, and then use...
- The primary FM then receives a clearer, more consistent prompt, which improves response quality without the additional complexity and cost of model customization.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
