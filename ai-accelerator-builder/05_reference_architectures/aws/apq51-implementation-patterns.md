---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-51
completeness: full
---

# 51: Implementation Patterns

## Scenario

A company is building a generative AI (GenAI) application that uses Amazon Bedrock. The company uses AWS Organizations for its AWS accounts. The company's AWS accounts are divided into two OUs: development and production. The company uses IAM roles to grant the application access to Amazon Bedrock across both development and production accounts. Access to the Amazon Bedrock API from production accounts in the organization must not traverse the public internet. A GenAI developer must enforce this restriction, regardless of IAM role configuration or application behavior. Which solution will meet this requirement?

## Common implementation patterns

- Create an interface VPC endpoint for Amazon Bedrock in each production VPC where the application that requires access is deployed. Create an SCP that denies Amazon Bedrock actions unless the request comes through an approved VPC endpoint. Attach the SCP to the production OU.

## Common anti-patterns

- Avoid create an interface VPC endpoint for Amazon Bedrock in each production VPC where the application that requires access is deployed. Create an IAM policy in each production account that denies Amazon Bedrock actions unless the request comes through an approved VPC endpoint....
- Avoid create a NAT gateway in each production VPC where the application that requires access is deployed. Set the NAT gateway connectivity type to private. Update the route tables associated with the subnets to route Amazon Bedrock traffic to the NAT gateway. because nAT...
- Avoid create an interface VPC endpoint for Amazon Bedrock in each production VPC where the application that requires access is deployed. Attach endpoint policies to the endpoints to allow access from only the approved application. because vPC endpoint policies are resource-based...

## Architecture guidance

- Interface VPC endpoints provide private connectivity to Amazon Bedrock within the AWS network.
- SCPs are an organization policy that you can use to manage permissions across accounts in an organization.
- The SCP enforces this control regardless of the IAM configuration in the accounts.
