---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-8
completeness: full
title: 8: Bedrock Continued Pretraining for Niche Domain Search
pattern_family: bedrock_continued_pretraining
aws_services:
  - Amazon Bedrock
related_controls:
  - audit_logging
topics:
  - bedrock continued pretraining
  - niche domain search
  - bedrock
  - audit logging
use_cases:
  - search and retrieval
---

# 8: Bedrock Continued Pretraining for Niche Domain Search

## Pattern summary

Use continued pretraining on proprietary domain data when a Bedrock model underperforms on a specialized search or knowledge domain.

## Scenario

A research company is using a customizable FM on Amazon Bedrock to develop an internal generative AI (GenAI) powered search interface. During testing, a GenAI developer discovers that the model's performance is suboptimal for a specific niche topic. The company has 3 TB of unlabeled proprietary research papers, technical documentation, and historical reports that cover the niche topic. The company wants the model to develop a deeper understanding of the niche topic's domain terminology, concepts, and relationships. The GenAI developer must improve the model's accuracy for the niche topic by using the proprietary data. Which solution will meet these requirements?

## Common implementation patterns

- Use the proprietary data to perform continued pre-training of the model in Amazon Bedrock.

## Architecture guidance

- With continued pre-training, a model can learn from large amounts of unlabeled domain-specific data.
- This solution continues general language model training on new content.
- The model can develop a deeper understanding of the domain's terminology, concepts, and relationships from the 3 TB of proprietary data.

## AWS documentation validation

- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Validated: Bedrock model customization supports continued pre-training with unlabeled domain data to improve domain knowledge, with jobs submitted through the console or API and artifacts stored in S3.
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html
- Documentation source: Bedrock model customization: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html
- Documentation source: Submit continued pre-training job: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-submit-api.html
- Documentation source: Knowledge Base retrieval APIs: https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-retrieval.html

## AWS-supported alternative patterns

- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- Consider RAG with Knowledge Bases first when freshness, citation, or governance of source documents is more important than changing model weights; use continued pre-training when the model needs deeper domain terminology and concept familiarity.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
