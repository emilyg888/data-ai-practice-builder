---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-48
completeness: full
title: 48: Bedrock Intelligent Prompt Routing for Tiered Customer Service Models
pattern_family: prompt_management
aws_services:
  - Amazon Bedrock
related_controls:
  - pii_protection
  - prompt_policy
topics:
  - bedrock intelligent prompt routing
  - tiered customer service models
  - prompt management
  - bedrock
  - pii protection
  - prompt policy
use_cases:
  - customer-facing assistant
  - cost optimization
  - routing and orchestration
---

# 48: Bedrock Intelligent Prompt Routing for Tiered Customer Service Models

## Pattern summary

Use Bedrock intelligent prompt routing to send simple customer-service prompts to a smaller model and complex reasoning prompts to a stronger fallback model.

## Scenario

A large ecommerce company is developing a customer service AI-powered chat assistant by using Amazon Bedrock. The company needs the chat assistant to be able to support both simple product questions and more complex reasoning tasks. Simple product questions are 80% of the queries. Complex reasoning tasks are 20% of the queries. The solution must be cost-effective and require minimal operational overhead while maintaining response quality. Which solution will meet these requirements?

## Common implementation patterns

- Use Amazon Bedrock intelligent prompt routing. Use Anthropic Claude Haiku as the primary model. Use Claude Sonnet as the fallback model. Configure the routing policy to send simple queries to Claude Haiku and to send complex queries to Claude Sonnet.

## Architecture guidance

- Amazon Bedrock intelligent prompt routing provides dynamic model selection based on query characteristics.
- Using Claude Haiku for simple product questions provides faster, more cost-effective processing.
- Routing complex reasoning tasks to Claude Sonnet ensures high-quality responses for sophisticated queries.

## AWS documentation validation

- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html

## AWS-supported alternative patterns

- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
