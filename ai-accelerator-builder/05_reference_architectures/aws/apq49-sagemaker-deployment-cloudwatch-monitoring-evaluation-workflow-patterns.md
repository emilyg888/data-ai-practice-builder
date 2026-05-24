---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-49
completeness: full
title: 49: Evaluation Workflow Patterns
pattern_family: evaluation_monitoring
aws_services:
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon SageMaker
related_controls:
  - model_evaluation
  - monitoring
topics:
  - evaluation workflow patterns
  - evaluation monitoring
  - bedrock
  - monitoring
  - sagemaker
  - model evaluation
  - evaluation
use_cases:
  - routing and orchestration
---

# 49: Evaluation Workflow Patterns

## Scenario

A retail company is using Amazon Bedrock to develop a generative AI (GenAI) application that will provide fashion recommendations to customers. The company wants to evaluate the quality of responses from two different FMs to determine which FM provides better fashion advice. Fashion experts who work for the company must perform the evaluations. Which combination of steps will meet these requirements to set up an evaluation process? (Select THREE.)

## Common implementation patterns

- Create an Amazon Cognito user pool to manage the fashion expert workforce. Assign the fashion experts to a work team.
- Create a human-based evaluation job in Amazon Bedrock with custom metrics including "Style Accuracy".

## Architecture guidance

- You must manage human evaluators as a work team.
- You can create a new Amazon Cognito managed work team by using the Amazon Bedrock console.
- For the fashion experts to evaluate the models, you must organize the fashion experts into a work team.

## AWS documentation validation

- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
