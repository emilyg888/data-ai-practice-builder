---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-69
completeness: full
---

# 69: Data Quality Patterns

## Scenario

A retail company needs to process product catalog data from multiple sources to enhance an AI-powered recommendation system. The data includes product descriptions, specifications, and customer reviews in various formats and languages. The system must improve data quality and ensure consistent inputs for the company's FMs. Which solution will meet these requirements?

## Common implementation patterns

- Extract product attributes by using Amazon Comprehend entity recognition through an AWS Lambda function. Normalize product categories and specifications. Use Amazon Bedrock to reformat product descriptions for optimal FM processing.

## Common anti-patterns

- Avoid process the input data through Amazon Comprehend to extract product entities and sentiment. Store the extracted features in Amazon DynamoDB to achieve a consistent structure that is optimized for FM consumption. Use Amazon CloudWatch to monitor data quality metrics before...
- Avoid create an AWS Lambda function to normalize product data formats. Use Amazon Comprehend custom classification to categorize products. Implement custom validation rules that check data consistency for product categories and specifications before sending the data to the...
- Avoid create an AWS Step Functions workflow that processes input data through Amazon Comprehend for entity extraction. Configure the workflow to use an AWS Lambda function for data validation and to implement custom filtering logic. Send the validated data to the Amazon Bedrock...

## Architecture guidance

- Lambda is a serverless compute service that you can use for data processing tasks.
- Amazon Comprehend has entity recognition capabilities that extract structured information from text and help standardize product attributes.
- Amazon Bedrock has text reformatting capabilities that ensure consistent input structure for FMs.
