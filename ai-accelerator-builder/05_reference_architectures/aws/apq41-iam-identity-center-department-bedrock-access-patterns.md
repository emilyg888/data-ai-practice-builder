---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-41
completeness: full
title: 41: IAM Identity Center Federation for Department-Scoped Bedrock Model Access
pattern_family: identity_federation_model_access
aws_services:
  - AWS IAM
  - Amazon Bedrock
related_controls:
  - access_control
topics:
  - iam identity center federation
  - department-scoped bedrock model access
  - iam access control
  - bedrock
  - access control
  - identity federation model access
use_cases:
  - architecture reference
---

# 41: IAM Identity Center Federation for Department-Scoped Bedrock Model Access

## Pattern summary

Federate corporate Active Directory through IAM Identity Center and map department-specific permission sets to approved Bedrock model access across accounts.

## Scenario

A financial services company creates a multi-account generative AI (GenAI) development environment by using Amazon Bedrock FMs. Employees must authenticate through the corporate Microsoft Active Directory. Employees should only be able to access FMs based on their department assignments. The company requires consistent permissions across AWS accounts. The company requires control over which models each department can use. The solution must ensure Regional resilience for the authentication service. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure AWS IAM Identity Center as the identity federation service and connect to Active Directory. Create permission sets with model access policies that map to departments. Configure multi-account access with Regional failover.

## Architecture guidance

- IAM Identity Center provides centralized identity federation with Active Directory.
- IAM Identity Center provides consistent permissions across multiple accounts through permission sets.
- This solution supports department-based access control to AWS resources including Amazon Bedrock models.

## AWS documentation validation

- Validated: IAM and endpoint-policy controls can be combined with Bedrock access paths; the pattern should be implemented with identity federation, permission sets, model-access policies, and CloudTrail auditability.
- Documentation source: Bedrock PrivateLink endpoints: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html
- Documentation source: Bedrock CloudTrail logging: https://docs.aws.amazon.com/bedrock/latest/userguide/logging-using-cloudtrail.html

## AWS-supported alternative patterns

- For private production workloads, pair identity federation with Bedrock VPC endpoints and endpoint policies to constrain network path as well as principal permissions.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
