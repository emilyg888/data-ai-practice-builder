---
type: reference_note
platform: aws
status: draft
source: udemy-question-25
---

# 25: Fine-Tuning Lifecycle Patterns

## Scenario

A financial services engineering team has created a domain-specific LLM by applying a parameter-efficient fine-tuning technique (LoRA) in Amazon SageMaker AI. The team wants to deploy the customized model to production and frequently release improved LoRA versions. The team must maintain a clear version history and approval trail for each release, and must be able to roll back quickly if a newly deployed model increases error rates or produces unacceptable outputs. Which combination of actions will meet these requirements with the LEAST operational overhead? (Select TWO.)

## Common implementation patterns

- Register each LoRA-adapted model version in Amazon SageMaker Model Registry and require an approval step before promoting a version for production deployment. This is the managed or lower-overhead approach called out as correct in the exam explanation.
- Deploy the model behind a SageMaker real-time endpoint that uses deployment guardrails (canary or linear) with automatic rollback based on Amazon CloudWatch alarms. This is the managed or lower-overhead approach called out as correct in the exam explanation.

## Common anti-patterns

- Avoid use Amazon Bedrock Prompt Management to version prompts and prompt variants for each release, and treat prompt version changes as the model deployment lifecycle. because prompt Management governs prompts, not model artifacts and model deployments. It...

## Architecture guidance

- A low-overhead, production-grade lifecycle for customized models requires both governance/versioning and safe release mechanisms.
- A model registry provides a controlled system of record for model versions (including approvals and deployment-ready artifacts).
- Deployment guardrails on the inference endpoint then handle progressive rollout and rollback when monitoring signals indicate a regression, avoiding custom traffic-splitting and rollback tooling.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
