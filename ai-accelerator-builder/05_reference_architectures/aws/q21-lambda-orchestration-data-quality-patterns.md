---
type: reference_note
platform: aws
status: draft
source: udemy-question-21
title: 21: Agent Orchestration Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - Amazon Bedrock
related_controls:
  - model_evaluation
  - prompt_policy
topics:
  - agent orchestration patterns
  - bedrock agents
  - lambda orchestration
  - bedrock
  - model evaluation
  - prompt policy
  - data quality
use_cases:
  - routing and orchestration
---

# 21: Agent Orchestration Patterns

## Scenario

An online retail platform is building a customer-support assistant by using a Strands agent with an Amazon Bedrock text model. The agent can call a tool that looks up order status from an internal system by invoking an AWS Lambda function. In production, the agent intermittently fails because it calls the tool with missing or malformed parameters (for example, an empty orderId), which causes Lambda errors and breaks the conversation. The team wants to make the tool integration more reliable without changing the underlying FM or adding significant operational complexity. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Define the tool with the Strands API by using a standardized function signature (explicit parameter names and types). Add strict parameter validation and exception handling in the Lambda handler that returns structured error responses the agent can act on...

## Architecture guidance

- The most reliable way to harden an agent tool is to treat the tool boundary like an API contract: use a standardized function definition so the agent knows exactly what parameters to supply, and enforce correctness with...
- Structured, predictable error responses let the agent recover (for example, by asking the user for a missing orderId) instead of failing the entire workflow.
- Other approaches either focus on content moderation rather than tool correctness, add orchestration that cannot repair invalid inputs, or depend on probabilistic improvements from prompting/model size instead of...

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
