---
type: reference_note
platform: aws
status: draft
source: udemy-question-73
title: 73: Bedrock Agent Evaluation And Trace Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - AWS Lambda
  - Amazon Bedrock
  - Amazon CloudWatch
  - Amazon SageMaker
related_controls:
  - audit_logging
  - model_evaluation
  - monitoring
  - prompt_policy
  - retrieval_grounding
topics:
  - bedrock agent evaluation trace patterns
  - bedrock knowledge bases
  - lambda orchestration
  - bedrock
  - monitoring
  - sagemaker
  - audit logging
  - model evaluation
  - prompt policy
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - search and retrieval
---

# 73: Bedrock Agent Evaluation And Trace Patterns

## Scenario

An internal IT-support assistant uses an Amazon Bedrock agent, knowledge-base retrieval, and Lambda-backed action groups. The team needs a repeatable way to detect tool loops and verify that the agent completes tasks efficiently.

## Common implementation patterns

- Use managed Bedrock agent evaluations against a representative prompt dataset to measure task completion and tool-use effectiveness.
- Enable trace capture for both test and production invocations so multi-step agent behavior can be inspected later.
- Analyze trace logs with CloudWatch Logs Insights to quantify repeated action-group calls, failed tool sequences, and unnecessary hops.
- Define agent-quality metrics around outcome completion, tool efficiency, and loop frequency rather than latency alone.
- Test instruction and tool-description changes with the same dataset before release so regressions are measurable.

## Common anti-patterns

- Building a fully custom judge-and-orchestrate evaluation pipeline before using managed Bedrock evaluation features.
- Using SageMaker Model Monitor as the primary control for Bedrock agent task-completion quality.
- Measuring only HTTP success and latency with synthetic canaries while ignoring whether the agent actually solved the task.
- Failing to persist traces, which makes repeated-tool-call problems hard to diagnose.
- Updating tool descriptions or instructions without re-running repeatable agent-evaluation scenarios.

## Architecture guidance

- Agent observability should combine score-based evaluation with trace-based inspection.
- Loop detection should be treated as a first-class operational metric for multi-tool agents.
- In regulated environments, traces should preserve the sequence of retrievals, action invocations, and reasoning steps needed for post-incident review.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
