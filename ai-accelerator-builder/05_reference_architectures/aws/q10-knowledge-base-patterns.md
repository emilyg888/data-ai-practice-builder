---
type: reference_note
platform: aws
status: draft
source: udemy-question-10
---

# 10: Knowledge Base And RAG Patterns

## Scenario

A risk and compliance team is building an internal Q&A assistant by using Amazon Bedrock Knowledge Bases backed by an Amazon OpenSearch Service vector store. Source policy documents are stored in Amazon S3 and are frequently updated throughout the day (new versions, replacements, and deletions). Users report that answers sometimes reference outdated policy language. The team needs an automated data maintenance approach that detects document changes in near real time and keeps the vector store synchronized with the latest content with the LEAST operational overhead. Which solution meets these requirements?

## Common implementation patterns

- Configure Amazon S3 event notifications for object create, overwrite, and delete events to Amazon EventBridge. Create an EventBridge rule that invokes an AWS Lambda function to call StartIngestionJob for the Amazon Bedrock knowledge base whenever relevant S3...

## Common anti-patterns

- Avoid enable Amazon S3 Versioning and Amazon S3 Cross-Region Replication (CRR) for the document bucket. Configure the application to query both Regions’ vector stores and select the most recent response based on the S3 version ID. because replicating S3...

## Architecture guidance

- Keeping a RAG vector store current requires both change detection and an automated synchronization mechanism that updates embeddings/index entries when source content changes.
- Using S3 events routed through EventBridge to trigger a Lambda function provides near-real-time detection of new, updated, or deleted documents and automatically initiates a knowledge base ingestion job to refresh the...
- Alternatives based on periodic batch refreshes increase staleness windows and can waste resources, while replication and access-log-driven pipelines add complexity without directly ensuring that embeddings and vector...

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
