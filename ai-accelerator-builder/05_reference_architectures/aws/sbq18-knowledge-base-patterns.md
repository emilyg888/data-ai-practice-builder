---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-18
completeness: partial
---

# 18: Knowledge Base Patterns

## Scenario

A company uses an AI assistant to answer customer questions based on internal company documents. The company wants to include new documents in the assistant's responses as soon as possible. The company wants to exclude deleted documents from the AI assistant's responses as soon as possible. The documents are stored in Amazon S3. The AI assistant uses Amazon Bedrock Knowledge Bases. Amazon S3 is the data source of the vector store that the company uses for RAG. A GenAI developer must create a scalable, event-driven, and resilient solution. Which solution will meet these requirements?

## Common implementation patterns

- Use an event-driven document synchronization workflow that reacts to object creation and deletion events instead of periodic polling.

## Common anti-patterns

- Avoid configure Amazon EventBridge Scheduler to schedule a rule that runs every 5 minutes and invokes an AWS Lambda function. Configure the Lambda function to track changes in Amazon S3 and invoke IngestKnowledgeBaseDocuments for new objects and DeleteKnowledgeBaseDocuments for deleted objects....

## Architecture guidance

- EventBridge Scheduler provides time-based actions for different AWS services.
- Running the sync action every 5 minutes is not suitable for near real-time updates to the knowledge base.
- This solution introduces delays in including new documents in the knowledge base.

## Source Notes

- The source export is partial for this question, so the endorsed pattern is inferred from the preserved prompt, answer key, and visible explanation text.
