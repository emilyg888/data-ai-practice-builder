---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-65
completeness: full
title: 65: Agent Orchestration Patterns
pattern_family: bedrock_guardrails
aws_services:
  - Amazon Bedrock
  - Bedrock Agents
related_controls:
  - access_control
  - guardrails
  - prompt_policy
topics:
  - agent orchestration patterns
  - bedrock guardrails
  - bedrock
  - agents
  - access control
  - guardrails
  - prompt policy
  - evaluation
use_cases:
  - routing and orchestration
---

# 65: Agent Orchestration Patterns

## Scenario

A travel company is developing a new AI-powered travel recommendation application by using Amazon Bedrock Agents. Customers can use the application to input travel preferences and receive personalized itinerary suggestions. The company wants to avoid prompt injection attacks that could manipulate the FM to provide unauthorized access or bypass content filters. A GenAI developer must implement security measures to protect against prompt injection attacks. Which combination of actions will meet these requirements? (Select THREE.)

## Common implementation patterns

- Associate an Amazon Bedrock guardrail with the agent to implement content filtering and topic boundaries.
- Enable the default pre-processing prompt for the Amazon Bedrock agent to evaluate if user input is safe to process.

## Architecture guidance

- Guardrails provide built-in protection against prompt injection.
- Guardrails provide content filtering and enforce topic boundaries.
- This action validates and filters inputs before the inputs reach the FM.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Guardrails support content filters, denied topics, sensitive-information handling, contextual grounding checks, and automated reasoning checks for policy validation.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Guardrail components: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html
- Documentation source: Guardrail content filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters.html
- Documentation source: Sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html
- Documentation source: ApplyGuardrail API: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html
- Documentation source: Automated Reasoning checks: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For pre-retrieval or post-generation checks outside model invocation, use the standalone ApplyGuardrail API so user input or generated output can be assessed independently.
- For policy-heavy workflows, consider Automated Reasoning checks in Guardrails to validate outputs against formalized natural-language policies; account for detect-mode behavior and added latency.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
