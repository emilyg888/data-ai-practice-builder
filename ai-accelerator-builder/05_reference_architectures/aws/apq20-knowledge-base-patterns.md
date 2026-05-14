---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-20
completeness: full
---

# 20: Knowledge Base Patterns

## Scenario

A GenAI developer at a media company is building a question-answering AI assistant by using Amazon Bedrock Knowledge Bases. The AI assistant needs to answer user questions accurately based on only the most recent documents. The GenAI developer must ensure that the AI assistant ignores older documents. Which solution will meet these requirements?

## Common implementation patterns

- Add a metadata filter for modification time.

## Common anti-patterns

- Avoid use a prompt template to instruct the model to ignore outdated documents. because prompt templates control how the model responds. However, prompt templates do not control what documents the model retrieves. You must handle retrieval filtering through metadata filters.
- Avoid set the search type to semantic. because semantic search helps match user queries with semantically similar content based on meaning rather than exact keywords. However, semantic search does not filter based on document recency. Without a metadata filter, the model can...
- Avoid enable query modification. because query modifications improve the handling of complex or multi-part questions. However, query modifications do not affect which documents the model retrieves based on recency.

## Architecture guidance

- You can use the metadata filter modification_time to restrict the source documents based on timestamps.
- You can add a metadata filter to ensure that the model retrieves only recently updated documents.
