---
type: reference_note
platform: aws
status: draft
source: udemy-question-23
title: 23: Prompt Governance Patterns
pattern_family: prompt_management
aws_services:
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon SageMaker
related_controls:
  - model_evaluation
  - monitoring
  - pii_protection
  - prompt_policy
topics:
  - prompt governance patterns
  - prompt management
  - bedrock
  - monitoring
  - sagemaker
  - model evaluation
  - pii protection
  - prompt policy
  - evaluation
use_cases:
  - internal assistant
  - model governance
---

# 23: Prompt Governance Patterns

## Scenario

An HR analytics team is building an internal assistant that drafts employee performance feedback by using Amazon Bedrock. The team stores standardized prompts in Amazon Bedrock Prompt Management. During a pilot, leadership raised concerns that the generated feedback might contain subtly different tone and recommendations for employees who are described with different demographic attributes in otherwise equivalent scenarios. The team wants to automatically evaluate and compare prompt variants for fairness, and track fairness results over time with minimal custom tooling. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon SageMaker Clarify to calculate pre-training bias metrics, and automatically fail the deployment if the bias metrics exceed thresholds. This is the managed or lower-overhead approach called out as correct in the exam explanation.

## Architecture guidance

- To apply fairness evaluations for foundation model outputs, the solution needs a repeatable way to compare alternatives and quantify bias-related behavior across a representative dataset.
- Using prompt variants and prompt orchestration enables controlled A/B testing, while automated model evaluation with an LLM-as-a-judge provides scalable scoring of outputs for fairness criteria without building a...
- Publishing those scores to CloudWatch makes fairness observable over time and supports governance reporting.

## AWS documentation validation

- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
