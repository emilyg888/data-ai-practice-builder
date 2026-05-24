---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-44
completeness: full
title: 44: Audit Logging Patterns
pattern_family: private_network_security
aws_services:
  - AWS CloudTrail
  - Amazon Bedrock
related_controls:
  - access_control
  - audit_logging
  - private_networking
topics:
  - audit logging patterns
  - private network security
  - audit logging
  - bedrock
  - access control
  - private networking
use_cases:
  - model governance
---

# 44: Audit Logging Patterns

## Scenario

A financial services company needs to access Amazon Bedrock from an application that runs in a private subnet. For security and compliance reasons, the application must make Amazon Bedrock API calls without traversing the public internet. The solution needs to enable logging through VPC Flow Logs and AWS CloudTrail. The solution must operate without internet gateway access. Which solution will meet these requirements?

## Common implementation patterns

- Create a VPC interface endpoint for the Amazon Bedrock Runtime service. Configure the private subnet route tables to direct Amazon Bedrock API traffic through the endpoint.

## Architecture guidance

- You can create a VPC endpoint for the Runtime service to provide secure, private access to Amazon Bedrock directly through the AWS network.
- This solution provides API calls without internet access.
- This solution maintains security through private networking.

## AWS documentation validation

- Validated: AWS documents interface VPC endpoints for private Amazon Bedrock connectivity, including private DNS and endpoint policies to control access through the endpoint.
- Validated: Bedrock supports model invocation logging to CloudWatch Logs or S3 for runtime request/response metadata, and CloudTrail records Bedrock API activity for audit trails.
- Documentation source: Bedrock interface VPC endpoints / PrivateLink: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html
- Documentation source: Bedrock model invocation logging: https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For regulated environments, combine Bedrock interface endpoints with endpoint policies, IAM conditions, and organization SCPs; validate supported endpoint names for runtime, agent runtime, and control-plane calls.
- Use CloudTrail for control-plane and API activity auditability; use model invocation logging when teams need request/response payload metadata for operational review, subject to privacy and retention controls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
