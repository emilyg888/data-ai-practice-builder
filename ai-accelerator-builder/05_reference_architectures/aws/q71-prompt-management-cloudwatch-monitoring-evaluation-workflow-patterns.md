---
type: reference_note
platform: aws
status: draft
source: udemy-question-71
title: 71: Prompt Governance Patterns
pattern_family: prompt_management
aws_services:
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon S3
related_controls:
  - audit_logging
  - model_evaluation
  - monitoring
  - prompt_policy
topics:
  - prompt governance patterns
  - prompt management
  - bedrock
  - monitoring
  - s3 data assets
  - audit logging
  - model evaluation
  - prompt policy
  - evaluation
use_cases:
  - model governance
---

# 71: Prompt Governance Patterns

## Scenario

A SaaS provider runs a customer-support assistant that uses an Amazon Bedrock text model and a prompt template stored in Amazon Bedrock Prompt Management. The team wants to release an updated prompt version and occasionally switch to a newer model version. Before promoting changes, the team must automatically validate that answers remain consistent with previously accepted behavior and that hallucinations or semantic drift do not increase. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create an Amazon Bedrock Model Evaluations job that runs a prompt dataset (synthetic user workflows) stored in Amazon S3 against the candidate prompt/model and a baseline. Use an LLM-as-a-judge evaluation to score quality and AI-specific metrics, and use the...

## Architecture guidance

- A low-overhead deployment validation system for GenAI updates should run repeatable synthetic user workflows and automatically score the candidate release for AI-specific regressions such as hallucinations and semantic...
- Using Amazon Bedrock Model Evaluations with a prompt dataset in Amazon S3 provides a managed way to evaluate candidate prompt/model changes against a baseline by using an evaluator model, producing objective scores that...
- Log analysis is post-deployment and manual, exact string matching is brittle for non-deterministic outputs, and human-in-the-loop reviews are higher operational overhead than managed automated evaluation.

## AWS documentation validation

- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
