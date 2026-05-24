---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-52
completeness: full
title: 52: Agent Orchestration Patterns
pattern_family: bedrock_guardrails
aws_services:
  - AWS Lambda
  - Amazon Bedrock
related_controls:
  - retrieval_grounding
topics:
  - agent orchestration patterns
  - bedrock guardrails
  - lambda orchestration
  - bedrock
  - retrieval grounding
  - data quality
use_cases:
  - routing and orchestration
---

# 52: Agent Orchestration Patterns

## Scenario

A company is using an Amazon Bedrock agent that assists customers. The company must implement comprehensive observability capabilities. The company wants to understand and track the agent's reasoning process in making decisions. The solution must provide detailed visibility into the agent's reasoning process. The solution must provide quick identification of potential hallucinations. Which solution will meet these requirements?

## Common implementation patterns

- Enable PreProcessingTrace, OrchestrationTrace, and PostProcessingTrace components with golden dataset validation and systematic trace analysis.

## Architecture guidance

- This solution provides end-to-end visibility into the agent's reasoning process.
- Each step in the console or trace in the API includes these three essential components.
- Together these components provide complete coverage of the agent's processing pipeline.

## AWS documentation validation

- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html

## AWS-supported alternative patterns

- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
