---
type: reference_note
platform: aws
status: draft
source: udemy-question-30
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

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
