---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-73
completeness: full
---

# 73: Knowledge Base Patterns

## Scenario

A legal services company wants to integrate diverse document management systems with an AI solution to enhance contract generation. The company needs to connect an existing contract template repository, internal legal knowledge bases, historical case documentation, and compliance wikis. The solution must maintain consistent access patterns. The solution must provide comprehensive data integration across all sources. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon Bedrock Knowledge Bases to create unified access to all document sources. Configure data source connectors for the template repository and knowledge bases. Set up automated synchronization to maintain the current content.

## Common anti-patterns

- Avoid deploy Amazon OpenSearch Service with vector search capabilities. Create standardized connectors by using AWS Lambda functions to index content from each source. Implement custom authentication handlers. Maintain separate backup procedures for each system. because...
- Avoid create a hybrid integration. Use Amazon AppFlow for software as a service (SaaS) based sources. Use AWS Transfer Family for on-premises sources. Deploy Amazon OpenSearch Service for unified search. Implement AWS Step Functions workflows to orchestrate data synchronization...
- Avoid implement Amazon Kendra with custom data source connectors. Set up incremental synchronization by using Amazon EventBridge rules. Create AWS Glue ETL jobs to standardize document formats across sources. Use Amazon S3 as the central document repository. because amazon...

## Architecture guidance

- Knowledge Bases provides built-in capabilities to integrate multiple document sources through standardized connectors.
- Knowledge Bases handles authentication, synchronization, and content updates automatically.
- Therefore, this solution requires the least operational overhead.
