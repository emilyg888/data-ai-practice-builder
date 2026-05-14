---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-9
completeness: full
---

# 9: Implementation Patterns

## Scenario

A global academic publishing company is developing a comprehensive research system that will store millions of scientific papers in Amazon S3. The system will use FMs in Amazon Bedrock to generate insights, recommend related papers, and provide natural language querying. The system must do the following: Record when authors publish, submit, and update papers. Store complete authorship information including name and contact details. Classify papers across multiple scientific disciplines, sub-disciplines, and methodologies. Provide search and filter capabilities by using complex criteria that combines metadata elements. Provide FMs with rich contextual information about each paper to improve response quality. Which metadata framework design will meet these requirements with the FASTEST query response?

## Common implementation patterns

- Store timestamps as S3 system-defined metadata. Store authorship details as S3 user-defined metadata. Create a hierarchical S3 object tag structure for scientific classifications. Integrate with Amazon OpenSearch Service enhanced with document vectors from Amazon Bedrock for...

## Common anti-patterns

- Avoid store timestamps as S3 user-defined metadata. Store authorship details and classifications in Amazon DynamoDB. Use S3 object keys as partition keys. Use S3 object tags for disciplines. Deploy Amazon OpenSearch Service for indexing and search. because storing timestamps as...
- Avoid store timestamps as S3 system-defined metadata. Store authorship details and classifications in an Amazon RDS for PostgreSQL database that links to S3 object keys. Use Amazon Kendra with custom document attributes for search. because rDS for PostgreSQL can store complex...
- Avoid store all metadata in Amazon DynamoDB. Use composite keys to enable various access patterns. Store the papers in Amazon S3 with minimal metadata. Set up S3 Event Notifications to maintain synchronization between services. Implement Amazon SageMaker Feature Store to prepare...

## Architecture guidance

- You can use S3 system-defined metadata for timestamps to provide reliable tracking.
- User-defined metadata efficiently stores authorship information.
- The hierarchical S3 object tags structure provides multi-level scientific classification.
