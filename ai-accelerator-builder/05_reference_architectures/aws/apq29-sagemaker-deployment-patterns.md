---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-29
completeness: full
---

# 29: SageMaker Deployment Patterns

## Scenario

A GenAI developer is designing a customer-facing application for a company. The GenAI developer uses an FM that is deployed on Amazon SageMaker AI. The application will deliver automated advisory services to customers. The company requires AI governance controls to ensure compliance with internal policies and external regulations. For compliance, the application must meet the following requirements: Enforce content restrictions and usage policies during model inference. Ensure that all model limitations and compliance risks are documented and centrally accessible. Automate compliance checks on model outputs by using programmatic workflows to flag violations. Which combination of steps will meet these requirements? (Select TWO.)

## Common implementation patterns

- Use Amazon Bedrock Guardrails with customized denied topics and blocked keywords based on usage policies. Create an Amazon EventBridge rule to invoke an AWS Lambda function for post-inference policy validation.
- Create model cards by using SageMaker Model Registry. Use Amazon EventBridge to trigger compliance workflows that invoke AWS Lambda functions to validate policies at runtime.

## Common anti-patterns

- Avoid integrate SageMaker Clarify with SageMaker Model Monitor to gather metrics across inference endpoints. Export the reports to Amazon S3 for policy compliance audits and governance insights. because you can use Clarify and Model Monitor for bias detection, explainability,...
- Avoid apply IAM policy conditions and AWS CloudTrail Insights on SageMaker AI model invocations. Detect runtime violations through log analysis pipelines. because iAM and CloudTrail are effective for access control and visibility into account activity. However, IAM policy...
- Avoid use AWS Glue Data Catalog to tag model training datasets with compliance metadata tags, including training provenance and policy classification for downstream documentation. because data Catalog is a metadata repository that you can use to organize and discover datasets....

## Architecture guidance

- You can use guardrails to define denied topics and blocked keywords to enforce content during model inference.
- You can use Guardrails for models that you deploy on SageMaker AI.
- This step reduces the risk of policy violations in AI-generated responses.
