---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-64
completeness: full
title: 64: SageMaker Deployment Patterns
pattern_family: evaluation_monitoring
aws_services:
  - Amazon CloudWatch
  - Amazon SageMaker
related_controls:
  - model_evaluation
  - monitoring
  - pii_protection
topics:
  - sagemaker deployment patterns
  - evaluation monitoring
  - monitoring
  - sagemaker
  - model evaluation
  - pii protection
  - evaluation
use_cases:
  - architecture reference
---

# 64: SageMaker Deployment Patterns

## Scenario

A financial services company wants to develop a generative AI (GenAI) application that provides personalized recommendations to users. A GenAI developer uses Amazon SageMaker AI to build the application. The application must process complex financial data and comply with regulations. The GenAI developer must implement a comprehensive fairness evaluation framework. The framework must detect subtle biases in model responses across different socioeconomic groups, age brackets, and geographic regions. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use SageMaker Clarify for automatic bias detection. Use FM evaluations (FMEval) with CrowS-Pairs datasets. Configure Amazon CloudWatch metrics for demographic disparity monitoring.

## Architecture guidance

- Clarify provides comprehensive bias detection capabilities across different demographic groups.
- Clarify can automatically identify potential unfairness in model responses.
- You can use FMEval with CrowS-Pairs datasets to test for stereotypical biases.

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
