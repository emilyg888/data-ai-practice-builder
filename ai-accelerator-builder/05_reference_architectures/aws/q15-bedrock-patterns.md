---
type: reference_note
platform: aws
status: draft
source: udemy-question-15
---

# 15: Throughput Patterns

## Scenario

An enterprise platform team at a financial institution is building a centralized “GenAI gateway” that internal applications must use to access Amazon Bedrock models. The gateway must enforce consistent request validation and throttling, record an audit trail of model access, and be deployed through an automated CI/CD pipeline that includes security checks. If a new release causes increased errors or latency, the deployment must automatically roll back. Which solution meets these requirements with the LEAST operational overhead?

## Common implementation patterns

- Deploy the gateway as Amazon API Gateway integrated with AWS Lambda that invokes Amazon Bedrock. Use AWS CodePipeline to orchestrate deployments from source control. Run automated tests and security scans in AWS CodeBuild, deploy with AWS CodeDeploy using...

## Common anti-patterns

- Avoid front the gateway with an Application Load Balancer that routes to Amazon ECS tasks running a custom proxy service. Use AWS CodePipeline to build and push container images to Amazon ECR. Perform blue/green deployments in the ECS service without...

## Architecture guidance

- A centralized GenAI gateway is best implemented with API Gateway in front of a Lambda layer that invokes Bedrock so the organization can standardize request validation, throttling, and access patterns.
- A managed CI/CD pipeline uses CodePipeline for orchestration and CodeBuild to run automated tests (for example, contract tests for request/response formats and prompt regression tests) and security scans before...
- For safe releases, CodeDeploy can perform canary traffic shifting for a Lambda alias and automatically roll back when CloudWatch alarms detect increased error rates or latency.

## Domain

- Content Domain 2: Implementation and Integration
