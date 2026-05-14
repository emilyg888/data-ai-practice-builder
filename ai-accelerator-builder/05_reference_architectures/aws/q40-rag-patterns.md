---
type: reference_note
platform: aws
status: draft
source: udemy-question-40
---

# 40: Knowledge Base And RAG Patterns

## Scenario

A manufacturing company is building an internal GenAI assistant on AWS by using Amazon Bedrock and a RAG architecture. Engineering specifications are stored in a SharePoint Online document library, and design decision records are maintained in an Atlassian Confluence wiki. The customer support team maintains troubleshooting articles in Salesforce. For compliance reasons, a copy of the Salesforce articles must also be stored in Amazon S3. The company wants to integrate these sources into a single retrieval layer with the LEAST operational overhead. Which combination of actions will meet these requirements? (Select TWO.)

## Common implementation patterns

- Create an Amazon Bedrock Knowledge Base and configure Confluence and SharePoint as data sources. Use an embedding model (for example, Amazon Titan embeddings) and a managed vector store integration to support semantic retrieval for the RAG application. This...
- Use Amazon AppFlow to replicate Salesforce knowledge articles into an Amazon S3 bucket on a schedule or on demand. Configure the Amazon Bedrock Knowledge Base to ingest the S3 content so the RAG application can retrieve from it. This is the managed or...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- The lowest-operations approach is to use managed integration components rather than building custom crawlers and ingestion pipelines.
- Amazon Bedrock Knowledge Bases can connect directly to enterprise knowledge sources such as Confluence and SharePoint and provide a managed path from source documents to semantic retrieval for RAG.
- For Salesforce content, Amazon AppFlow provides a managed way to replicate SaaS data into Amazon S3 to satisfy the requirement to keep an S3 copy, and the Knowledge Base can then ingest from S3 to make that content...

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
