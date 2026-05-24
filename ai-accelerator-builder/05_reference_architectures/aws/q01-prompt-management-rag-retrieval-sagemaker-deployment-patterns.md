---
type: reference_note
platform: aws
status: draft
source: udemy-question-1
completeness: partial
title: 1: RAG Evaluation And User Feedback Patterns
pattern_family: bedrock_knowledge_bases
aws_services:
  - Amazon Bedrock
  - Amazon SageMaker
related_controls:
  - evidence_retention
  - model_evaluation
  - prompt_policy
  - retrieval_grounding
topics:
  - rag evaluation user feedback patterns
  - bedrock knowledge bases
  - bedrock
  - sagemaker
  - evidence retention
  - model evaluation
  - prompt policy
  - retrieval grounding
  - rag
  - evaluation
use_cases:
  - internal assistant
  - policy assistance
  - search and retrieval
---

# 1: RAG Evaluation And User Feedback Patterns

## Pattern summary

Use Amazon Bedrock RAG evaluations, citation trace capture, and structured feedback events to evaluate policy-assistant answer faithfulness, citation quality, retrieval quality, and prompt-release readiness before promoting model or prompt changes.

## Scenario

An internal policy assistant uses Amazon Bedrock knowledge-base retrieval. The team needs low-overhead evaluation for answer faithfulness to retrieved context, citation quality, and ongoing user-feedback capture before promoting prompt or model-configuration changes.

## Common implementation patterns

- Use a managed LLM evaluation workflow that can score groundedness, citation quality, and answer usefulness against a fixed prompt dataset.
- Persist prompt, retrieval context, answer, citation metadata, and evaluation results together so prompt changes can be compared across releases.
- Capture end-user feedback as structured events instead of ad hoc notifications so it can be aggregated and analyzed later.
- Treat retrieval quality and generation quality as separate signals so teams can tell whether failures come from chunking/search or model behavior.
- Gate promotion of prompt-template and inference changes on repeatable offline evaluation results rather than subjective spot checks.

## Common anti-patterns

- Using Amazon SageMaker Model Monitor or SageMaker Clarify as the main RAG answer-faithfulness evaluator.
- Sending user feedback to SNS for manual review as the primary feedback-analysis workflow.
- Measuring only generic response drift without evaluating whether answers are supported by retrieved context.
- Promoting prompt changes without preserving the retrieval evidence and citation trace used during evaluation.

## Architecture guidance

- Use Amazon Bedrock RAG evaluation jobs as the managed evaluation path for Knowledge Bases or other RAG sources. Choose retrieve-only evaluation when validating retrieval relevance, and retrieve-and-generate evaluation when validating both retrieved evidence and generated answers.
- Build the evaluation dataset as a stable prompt set in Amazon S3. Include expected retrieved passages or expected responses where available so releases can be compared against the same baseline.
- Persist the `RetrieveAndGenerate` response payload for each test case, including generated output, citations, retrieved references, source locations, metadata, prompt version, knowledge-base version, and model inference settings.
- Track retrieval and generation as separate quality gates. Retrieval metrics should detect missing or irrelevant policy passages, while generation metrics should assess faithfulness, correctness, completeness, helpfulness, citation precision, and citation coverage.
- Store RAG evaluation reports and custom metric definitions in the configured S3 output location so audit, risk, and model-governance reviewers can compare evaluation runs across prompt or model releases.
- Treat user feedback as production telemetry, not as the primary release gate. Capture structured feedback reason codes and join them later with prompt version, retrieval context, citations, and model settings to prioritize new offline evaluation cases.
- Do not rely on SageMaker Model Monitor or Clarify as the primary RAG-faithfulness mechanism. They can support adjacent model monitoring or explainability workflows, but Bedrock RAG evaluations are the lower-overhead fit for knowledge-base retrieval and generated-answer assessment.

## Practical design notes

- For BFSI-style policy assistants, evaluation data should include the exact retrieved passages, policy version, prompt version, and model settings.
- User feedback should be normalized into reason codes such as `useful`, `not_grounded`, `missing_citation`, or `incomplete`.

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

## Reference sources

- Amazon Bedrock evaluations for models, Knowledge Bases, and RAG sources: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html
- Amazon Bedrock RAG evaluation jobs: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-kb.html
- Amazon Bedrock RAG evaluation reports and metrics: https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-evaluation-report.html
- Retrieve and generate responses with Knowledge Bases: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-retrieve-generate.html
