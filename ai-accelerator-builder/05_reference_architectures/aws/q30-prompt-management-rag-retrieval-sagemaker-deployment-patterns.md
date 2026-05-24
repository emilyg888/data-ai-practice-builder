---
type: reference_note
platform: aws
status: draft
source: udemy-question-30
title: 30: Knowledge Base And RAG Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon S3
  - Amazon SageMaker
related_controls:
  - model_evaluation
  - monitoring
  - prompt_policy
  - retrieval_grounding
topics:
  - knowledge base rag patterns
  - bedrock knowledge bases
  - bedrock
  - s3 data assets
  - sagemaker
  - model evaluation
  - monitoring
  - prompt policy
  - retrieval grounding
  - rag
  - prompt management
  - evaluation
use_cases:
  - document summarization
  - policy assistance
  - model governance
---

# 30: Knowledge Base And RAG Patterns

## Scenario

A compliance engineering team is building an internal summarization service that uses an Amazon Bedrock text FM to produce 1-paragraph summaries of long policy documents. The team needs an evaluation approach that can be rerun for every prompt template change to detect regressions. The approach must assess the quality of summaries across multiple dimensions, including relevance to the source content, factual accuracy, consistency across runs, and fluency, while keeping the evaluation process largely automated. Which approach will meet these requirements with the LEAST manual effort?

## Common implementation patterns

- Store a prompt dataset in Amazon S3 that includes source documents and reference summaries. Run Amazon Bedrock Model Evaluations using an LLM-as-a-judge configuration to score each generated summary on relevance, correctness (factual accuracy), consistency,...
- Enable Amazon SageMaker Model Monitor on the summarization workload to detect data drift and feature attribution drift. Block deployments when drift exceeds a predefined threshold. This is the managed or lower-overhead approach called out as correct in the...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- A comprehensive FM output assessment framework needs explicit quality-oriented metrics (such as relevance, factual accuracy/correctness, consistency, and fluency) and must be repeatable for regression testing when...
- An automated evaluation workflow that uses a curated prompt dataset with reference outputs, and applies an LLM-as-a-judge evaluator to score multiple dimensions, provides actionable quality scores at scale with minimal...
- Operational metrics like latency and token counts support cost/performance optimization but do not measure output quality, and traditional n-gram overlap metrics alone are not sufficient to capture hallucinations,...

## AWS documentation validation

- Validated: Bedrock Knowledge Bases support Retrieve and RetrieveAndGenerate patterns, including cited source chunks and retrieved reference metadata for RAG responses.
- Validated: Bedrock Prompt management supports reusable prompts, variables, variants, versioning, testing, and integration into model invocation or flows.
- Validated: SageMaker real-time endpoints are suited to low-latency custom model inference, batch transform is suited to offline or large-batch inference, and data capture supports model monitoring workflows.
- Validated: Amazon Bedrock evaluations support model, Knowledge Base, and RAG-source evaluation, including LLM-as-judge metrics such as correctness, completeness, faithfulness, helpfulness, relevance, and instruction following.
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html
- Documentation source: RetrieveAndGenerate citations and reranking: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
- Documentation source: Bedrock RAG evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Documentation source: RAG evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-eval-llm-results.html
- Documentation source: Bedrock Prompt management: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html
- Documentation source: Intelligent prompt routing: https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html
- Documentation source: SageMaker real-time endpoints: https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html
- Documentation source: SageMaker Batch Transform: https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html
- Documentation source: SageMaker data capture and Model Monitor: https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Documentation source: Bedrock evaluation metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-metrics.html

## AWS-supported alternative patterns

- Use Retrieve-only when the application needs custom orchestration or generation logic; use RetrieveAndGenerate when the managed Bedrock response-generation path and citation payload are sufficient.
- For higher retrieval quality, evaluate metadata filtering and reranking where supported, then verify with Bedrock RAG evaluation jobs.
- For model cost and quality tradeoffs across similar models, evaluate Bedrock intelligent prompt routing rather than maintaining only custom routing logic.
- For release control, store prompt versions and compare prompt variants before promotion instead of relying on ad hoc prompt text in application code.
- Use Bedrock managed foundation models when custom model hosting is not required; use SageMaker endpoints when the workload requires custom containers, custom model artifacts, or lower-level hosting control.
- For offline scoring or scheduled inference, prefer SageMaker Batch Transform over a persistent endpoint.
- Use Bedrock RAG evaluations when retrieval and generated-answer quality need to be assessed together; use model evaluation jobs when comparing model or prompt behavior independent of retrieval.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
