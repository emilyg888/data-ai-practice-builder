---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-17
completeness: full
title: 17: Evaluation Workflow Patterns
pattern_family: bedrock_agents
aws_services:
  - AWS Lambda
  - AWS Step Functions
  - Amazon Bedrock
  - Amazon CloudWatch
related_controls:
  - model_evaluation
  - monitoring
topics:
  - evaluation workflow patterns
  - bedrock agents
  - lambda orchestration
  - step functions
  - bedrock
  - monitoring
  - model evaluation
  - evaluation
  - data quality
use_cases:
  - routing and orchestration
---

# 17: Evaluation Workflow Patterns

## Scenario

A company is implementing a systematic evaluation process for a newly deployed FM in Amazon Bedrock. The company wants to replace an existing model in production with a new model. The change to the new model is dependent on the new model demonstrating better performance than the existing model. The company must follow a sequential validation process. To ensure evaluation rigor, each step must be reviewed and approved before proceeding to the next step. Select and order each step from the following list to implement the evaluation workflow. Select each step one time. (Select and order FIVE.) Analyze the results and generate a comprehensive evaluation report. Conduct A/B testing to compare the new model against the existing production model. Create a test dataset with diverse scenarios and edge cases. Define evaluation metrics for relevance, factual accuracy, and fluency. Implement automated quality gates by using AWS Step Functions.

## Common implementation patterns

- Define evaluation metrics for relevance, factual accuracy, and fluency. This step is part of the endorsed evaluation sequence and should be executed in order.
- Create a test dataset with diverse scenarios and edge cases. This step is part of the endorsed evaluation sequence and should be executed in order.
- Conduct A/B testing to compare the new model against the existing production model. This step is part of the endorsed evaluation sequence and should be executed in order.
- Implement automated quality gates by using AWS Step Functions. This step is part of the endorsed evaluation sequence and should be executed in order.
- Analyze the results and generate a comprehensive evaluation report. This step is part of the endorsed evaluation sequence and should be executed in order.

## Common anti-patterns

- Avoid starting A/B testing before defining evaluation metrics and building an approved test dataset.
- Avoid generating final approval reports before automated quality gates and validation checkpoints have completed.
- Avoid treating evaluation as an unstructured activity; sequence control is part of the architecture, not just process documentation.

## Architecture guidance

- Sequential validation and approval provides a rigorous evaluation process where each step builds upon validated components of the previous steps.
- This sequential workflow is essential to maintain evaluation rigor.
- You can use this approach to make an informed decision about model replacement.

## AWS documentation validation

- Validated: Bedrock Agents support action groups for tool/API fulfillment, and AWS documents supervisor/collaborator multi-agent patterns for complex task decomposition.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock multi-agent collaboration: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html
- Documentation source: Bedrock action groups: https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html
- Documentation source: AgentCore Runtime overview: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
- Documentation source: AgentCore Gateway: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For complex multi-domain workflows, consider Amazon Bedrock multi-agent collaboration with a supervisor agent and specialized collaborator agents instead of a single broad agent.
- For enterprise tool integration or custom agent frameworks, consider Amazon Bedrock AgentCore Runtime and AgentCore Gateway with MCP-compatible tools.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
