---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-72
completeness: full
title: 72: RAG Patterns
pattern_family: rag
aws_services:
  - Amazon S3
  - Amazon SageMaker
related_controls:
  - audit_logging
  - model_evaluation
  - monitoring
  - retrieval_grounding
topics:
  - rag patterns
  - rag
  - s3 data assets
  - sagemaker
  - audit logging
  - model evaluation
  - monitoring
  - retrieval grounding
  - evaluation
use_cases:
  - search and retrieval
  - real-time streaming
---

# 72: RAG Patterns

## Scenario

A large social media company runs multiple RAG pipelines across different applications. Each pipeline uses an FM embedding endpoint deployed on an Amazon SageMaker AI real-time endpoint. A GenAI developer uses the endpoint to generate embeddings. The GenAI developer stores the embeddings in multiple vector databases. The production applications use the vector databases to drive document retrieval for downstream generation and to provide users with content. Recently, multiple users report that the response relevance has been poor. New writing styles are appearing more frequently. The GenAI developer wants to determine if the input drift is degrading embedding quality. The GenAI developer must prepare the model for re-training without disrupting production traffic. Which combination of steps will meet these requirements? (Select TWO.)

## Common implementation patterns

- Schedule SageMaker Model Monitor with a custom Amazon ECR image. Compute all the drift metrics between the endpoint captured data and the baseline training dataset used by the model. Store the final violation reports in Amazon S3.
- Create a new SageMaker AI endpoint configuration based on the production variant with Data Capture enabled. Use the UpdateEndpoint API to shift endpoint traffic to the new endpoint with the updated configuration. Parse captured data in SageMaker Model Monitor to investigate.

## Architecture guidance

- Model Monitor is a fully managed service that provides continuous monitoring of production ML models.
- Model Monitor runs scheduled jobs by using custom images.
- This approach can compute embedding-level drift metrics by comparing captured inference data (the data capture logs) against a baseline dataset.

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
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
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
