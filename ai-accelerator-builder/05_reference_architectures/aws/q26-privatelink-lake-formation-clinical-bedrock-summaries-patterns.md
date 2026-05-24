---
type: reference_note
platform: aws
status: draft
source: udemy-question-26
title: 26: PrivateLink and Lake Formation Controls for Clinical Bedrock Summaries
pattern_family: lambda_orchestration
aws_services:
  - AWS Lake Formation
  - AWS Lambda
  - AWS PrivateLink
  - Amazon Athena
  - Amazon Bedrock
  - Amazon S3
related_controls:
  - access_control
  - pii_protection
  - private_networking
topics:
  - privatelink lake formation controls
  - clinical bedrock summaries
  - lambda orchestration
  - lake formation governance
  - private networking
  - amazon athena
  - bedrock
  - s3 data assets
  - access control
  - pii protection
use_cases:
  - internal assistant
  - document summarization
  - search and retrieval
---

# 26: PrivateLink and Lake Formation Controls for Clinical Bedrock Summaries

## Pattern summary

Run Lambda in private subnets with VPC endpoints for Bedrock, Athena, and S3 while Lake Formation enforces access to clinical source data.

## Scenario

A healthcare analytics team is building an internal GenAI assistant that uses Amazon Bedrock to summarize clinical case notes. The assistant retrieves supporting facts from a data lake in Amazon S3 by running Amazon Athena queries. The team must ensure that service-to-service traffic does not traverse the public internet and that the Bedrock invocation can access only approved columns (no PHI) from the data lake. The team also wants to monitor data access with minimal operational overhead. Which solution meets these requirements MOST effectively?

## Common implementation patterns

- Create interface VPC endpoints (AWS PrivateLink) for Amazon Bedrock and Amazon Athena, and create a gateway VPC endpoint for Amazon S3. Run the Lambda function in private subnets with no internet gateway. Use AWS Lake Formation to apply column-level...

## Architecture guidance

- A protected AI environment for FM deployments typically combines private network connectivity, least-privilege access controls, and governed data access.
- Using VPC endpoints (PrivateLink) allows the application components in private subnets to call managed services without traversing the public internet.
- Lake Formation can enforce fine-grained permissions for Athena-accessed data in S3, including restricting sensitive columns such as PHI.

## AWS documentation validation

- Validated: Lambda is appropriate for short serverless integration logic; Step Functions is the AWS-documented orchestration option for multi-step workflows across Lambda and other AWS services.
- Validated: AWS documents interface VPC endpoints for private Amazon Bedrock connectivity, including private DNS and endpoint policies to control access through the endpoint.
- Documentation source: Lambda best practices: https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html
- Documentation source: Step Functions orchestration for Lambda: https://docs.aws.amazon.com/lambda/latest/dg/with-step-functions.html
- Documentation source: EventBridge integration with Step Functions: https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html
- Documentation source: Bedrock interface VPC endpoints / PrivateLink: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html

## AWS-supported alternative patterns

- Use Step Functions when the workflow needs visible state, retries, error handling, human approval, or multi-service coordination; keep direct Lambda for simple request/response or event handlers.
- Use EventBridge for event-driven decoupling and routing when multiple downstream consumers or asynchronous integration patterns are required.
- For regulated environments, combine Bedrock interface endpoints with endpoint policies, IAM conditions, and organization SCPs; validate supported endpoint names for runtime, agent runtime, and control-plane calls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
