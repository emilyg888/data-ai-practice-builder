---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-14
completeness: full
---

# 14: BDA Transformation Patterns

## Scenario

A GenAI developer is building a serverless application. The application uses AWS Lambda functions that are deployed in private subnets to process sensitive customer data. The Lambda functions need to invoke Amazon Bedrock FMs for AI-powered analytics. All API communication must remain within the AWS private network without internet exposure. The GenAI developer tests the Lambda function. The Lambda function consistently times out when attempting to call Amazon Bedrock APIs. The Lambda function has proper IAM permissions for Amazon Bedrock access. Which solution will resolve this connectivity issue?

## Common implementation patterns

- Create interface VPC endpoints for the Amazon Bedrock Runtime service in the VPC. Ensure that the endpoints are associated with the private subnets where Lambda functions are deployed. Verify that security groups allow HTTPS traffic on port 443 between Lambda and the VPC...

## Common anti-patterns

- Avoid configure Amazon Route 53 private hosted zones for the Amazon Bedrock service endpoints that resolve to the internal VPC CIDR range. Enable custom DNS resolution in the VPC settings. Ensure that the Lambda execution role has Route 53 Resolver permissions for private DNS...
- Avoid deploy dedicated proxy Lambda functions in the private subnets that handle all Amazon Bedrock API communications. Configure the proxy functions with enhanced networking permissions. Set up an internal Application Load Balancer between the application Lambda functions and...
- Avoid create an AWS Client VPN endpoint in the VPC. Configure the Lambda functions to route Amazon Bedrock API calls through the VPN connection. Add a route table entry to direct traffic to Amazon Bedrock through the Client VPN endpoint. because client VPN is designed for secure...

## Architecture guidance

- Interface VPC endpoints allow Lambda functions in private subnets to access Amazon Bedrock APIs without internet connectivity.
- The Runtime service requires the com.amazonaws.region.bedrock-runtime endpoint for model invocation operations.
- Security groups must allow outbound HTTPS traffic on port 443 from Lambda to the VPC endpoint.
