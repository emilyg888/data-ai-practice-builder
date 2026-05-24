---
type: reference_note
platform: aws
status: draft
source: udemy-question-70
title: 70: Well-Architected GenAI Lens Review and Reusable Bedrock IaC
pattern_family: well_architected_genai_iac
aws_services:
  - Amazon Bedrock
  - AWS Well-Architected Tool
related_controls:
  - audit_logging
topics:
  - well-architected genai lens review reusable bedrock iac
  - bedrock
  - audit logging
  - well architected genai iac
use_cases:
  - cost optimization
---

# 70: Well-Architected GenAI Lens Review and Reusable Bedrock IaC

## Pattern summary

Use the Well-Architected Generative AI Lens plus approved IaC modules to standardize multi-account Bedrock application architectures.

## Scenario

A healthcare platform team is enabling multiple product groups to build GenAI applications on AWS by using Amazon Bedrock. The applications will be deployed in different AWS accounts and environments (dev, test, and production). The platform team must provide a consistent, repeatable way for teams to implement GenAI architectures that align with organizational best practices across security, reliability, and cost. Which approach will achieve this with the LEAST operational overhead?

## Common implementation patterns

- Use the AWS Well-Architected Tool with the AWS Well-Architected Generative AI Lens to define and review a standard GenAI architecture. Provide approved reusable infrastructure-as-code components (for example, AWS CDK or AWS CloudFormation templates) that...

## Architecture guidance

- The most effective low-overhead way to standardize GenAI implementations across many teams and deployment scenarios is to combine a repeatable architecture review process with reusable building blocks.
- The AWS Well-Architected Tool and the Generative AI Lens provide a consistent best-practices framework aligned to the Well-Architected pillars, and publishing approved infrastructure-as-code templates or constructs...
- Other approaches either rely on post-hoc auditing, add significant custom tooling overhead, or focus on restrictive governance controls without standardizing how solutions are designed and implemented.

## AWS documentation validation

- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Validated: The AWS Well-Architected Generative AI Lens documents lifecycle phases and best practices across operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability for Bedrock and SageMaker AI workloads.
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html
- Documentation source: Generative AI Lens: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html
- Documentation source: Generative AI lifecycle: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html

## AWS-supported alternative patterns

- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- Use the Generative AI Lens as the review framework and pair it with IaC modules such as CDK or CloudFormation so recurring Bedrock application patterns are reviewed and deployed consistently.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
