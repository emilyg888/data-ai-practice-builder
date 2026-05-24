---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-51
completeness: full
title: 51: PrivateLink and SCP Controls for Production Bedrock Access
pattern_family: private_network_security
aws_services:
  - AWS IAM
  - AWS PrivateLink
  - Amazon Bedrock
related_controls:
  - access_control
  - private_networking
topics:
  - privatelink scp controls
  - production bedrock access
  - private network security
  - iam access control
  - private networking
  - bedrock
  - access control
use_cases:
  - architecture reference
---

# 51: PrivateLink and SCP Controls for Production Bedrock Access

## Pattern summary

Require production Bedrock traffic to use approved VPC endpoints by combining interface endpoints with organization-level service control policies.

## Scenario

A company is building a generative AI (GenAI) application that uses Amazon Bedrock. The company uses AWS Organizations for its AWS accounts. The company's AWS accounts are divided into two OUs: development and production. The company uses IAM roles to grant the application access to Amazon Bedrock across both development and production accounts. Access to the Amazon Bedrock API from production accounts in the organization must not traverse the public internet. A GenAI developer must enforce this restriction, regardless of IAM role configuration or application behavior. Which solution will meet this requirement?

## Common implementation patterns

- Create an interface VPC endpoint for Amazon Bedrock in each production VPC where the application that requires access is deployed. Create an SCP that denies Amazon Bedrock actions unless the request comes through an approved VPC endpoint. Attach the SCP to the production OU.

## Architecture guidance

- Interface VPC endpoints provide private connectivity to Amazon Bedrock within the AWS network.
- SCPs are an organization policy that you can use to manage permissions across accounts in an organization.
- The SCP enforces this control regardless of the IAM configuration in the accounts.

## AWS documentation validation

- Validated: AWS documents interface VPC endpoints for private Amazon Bedrock connectivity, including private DNS and endpoint policies to control access through the endpoint.
- Documentation source: Bedrock interface VPC endpoints / PrivateLink: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html

## AWS-supported alternative patterns

- For regulated environments, combine Bedrock interface endpoints with endpoint policies, IAM conditions, and organization SCPs; validate supported endpoint names for runtime, agent runtime, and control-plane calls.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
