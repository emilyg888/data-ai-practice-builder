---
type: reference_note
platform: aws
status: draft
source: udemy-question-26
---

# 26: Implementation Patterns

## Scenario

A healthcare analytics team is building an internal GenAI assistant that uses Amazon Bedrock to summarize clinical case notes. The assistant retrieves supporting facts from a data lake in Amazon S3 by running Amazon Athena queries. The team must ensure that service-to-service traffic does not traverse the public internet and that the Bedrock invocation can access only approved columns (no PHI) from the data lake. The team also wants to monitor data access with minimal operational overhead. Which solution meets these requirements MOST effectively?

## Common implementation patterns

- Create interface VPC endpoints (AWS PrivateLink) for Amazon Bedrock and Amazon Athena, and create a gateway VPC endpoint for Amazon S3. Run the Lambda function in private subnets with no internet gateway. Use AWS Lake Formation to apply column-level...

## Common anti-patterns

- Avoid place the AWS Lambda function in private subnets and use a NAT gateway for outbound access to Amazon Bedrock and Amazon Athena public endpoints. Restrict access to S3 objects by using S3 bucket policies and encrypt the bucket with SSE-KMS. because a NAT...

## Architecture guidance

- A protected AI environment for FM deployments typically combines private network connectivity, least-privilege access controls, and governed data access.
- Using VPC endpoints (PrivateLink) allows the application components in private subnets to call managed services without traversing the public internet.
- Lake Formation can enforce fine-grained permissions for Athena-accessed data in S3, including restricting sensitive columns such as PHI.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
