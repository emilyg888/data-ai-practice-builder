---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-1
completeness: full
---

# 1: Throughput Patterns

## Scenario

An ecommerce company has an application that uses Amazon Bedrock to generate product descriptions and recommendations. Currently, the application resides in a single AWS Region. When invoking a model in Amazon Bedrock during peak periods, the application receives an error. The error message says, "Too many requests, please wait before trying again." The company must increase the throughput for invocations during peak periods without introducing additional operational overhead. The company must maintain compatibility with the existing Amazon Bedrock API. The company must use the same FM. Which solution will meet these requirements in the MOST cost-effective way?

## Common implementation patterns

- Use cross-Region inference to distribute traffic across multiple Regions within a geographic area.

## Common anti-patterns

- Avoid create an AWS Lambda function to invoke the model in Amazon Bedrock with the original Region as the default. Configure the Lambda function to fall back to Amazon Bedrock in a secondary Region. because you can create a Lambda function to invoke an Amazon Bedrock model. The Lambda function is...
- Avoid use prompt routing to distribute traffic across multiple FMs from the same family. because amazon Bedrock intelligent prompt routing provides a single endpoint to efficiently route requests between different FMs within the same model family. This solution requires at least two different...
- Avoid use provisioned throughput to provision a higher level of throughput for the FM. because provisioned throughput will provide higher throughput for the number of I/O rates that a model can process. However, the application needs a solution for peak periods, not for consistent usage. Learn more...

## Architecture guidance

- Cross-Region inference automatically distributes traffic across multiple Regions within your geographic area to process your inference request.
- Learn more about cross-Region inference.
