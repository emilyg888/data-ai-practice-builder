---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-44
completeness: full
---

# 44: Audit Logging Patterns

## Scenario

A financial services company needs to access Amazon Bedrock from an application that runs in a private subnet. For security and compliance reasons, the application must make Amazon Bedrock API calls without traversing the public internet. The solution needs to enable logging through VPC Flow Logs and AWS CloudTrail. The solution must operate without internet gateway access. Which solution will meet these requirements?

## Common implementation patterns

- Create a VPC interface endpoint for the Amazon Bedrock Runtime service. Configure the private subnet route tables to direct Amazon Bedrock API traffic through the endpoint.

## Common anti-patterns

- Avoid configure an Application Load Balancer (ALB) in a public subnet to proxy Amazon Bedrock API requests from the private subnet to the Amazon Bedrock public endpoints. because aLBs can proxy requests. However, placing an ALB in a public subnet sends Amazon Bedrock calls to...
- Avoid deploy a NAT gateway in a public subnet. Configure the private subnet route tables to direct Amazon Bedrock API traffic through the NAT gateway. because a NAT gateway is a managed AWS service that allows instances in private subnets to access the internet while preventing...
- Avoid create a VPC gateway endpoint for the Amazon Bedrock Runtime service. Configure the private subnet route tables to direct Amazon Bedrock API traffic through the endpoint. because a VPC gateway endpoint is a gateway that you specify as a target for a route in your route...

## Architecture guidance

- You can create a VPC endpoint for the Runtime service to provide secure, private access to Amazon Bedrock directly through the AWS network.
- This solution provides API calls without internet access.
- This solution maintains security through private networking.
