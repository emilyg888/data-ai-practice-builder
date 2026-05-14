---
type: reference_note
platform: aws
status: draft
source: udemy-question-1
completeness: partial
---

# 1: RAG Evaluation And User Feedback Patterns

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

## Practical design notes

- For BFSI-style policy assistants, evaluation data should include the exact retrieved passages, policy version, prompt version, and model settings.
- User feedback should be normalized into reason codes such as `useful`, `not_grounded`, `missing_citation`, or `incomplete`.